#!/usr/bin/env python

#################################################################
##\file
#
# \note
# Copyright (c) 2013 \n
# Fraunhofer Institute for Manufacturing Engineering
# and Automation (IPA) \n\n
#
#################################################################
#
# \note
# Project name: Care-O-bot Research
# \note
# ROS package name:
#
# \author
# Author: Thiago de Freitas Oliveira Araujo,
# email:thiago.de.freitas.oliveira.araujo@ipa.fhg.de
# \author
# Supervised by: Florian Weisshardt, email:florian.weisshardt@ipa.fhg.de
#
# \date Date of creation: April 2013
#
# \brief
# Battery Characterization for the IPA robots
#
#################################################################
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# - Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer. \n
# - Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution. \n
# - Neither the name of the Fraunhofer Institute for Manufacturing
# Engineering and Automation (IPA) nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission. \n
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License LGPL as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License LGPL for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License LGPL along with this program.
# If not, see < http://www.gnu.org/licenses/>.
#
#################################################################

from math import *
import numpy as np

import rospy
import savitzky
from std_msgs.msg import Float64
from cob_msgs.msg import EmergencyStopState, PowerState

class volts_filter():

    def __init__(self):
        self.volts_raw = 0.0
        self.volts_filtered = None
        self.temperature = None
        self.wsize = 61
        self.filter_order = 3
        self.theta = rospy.get_param("~theta")
        self.off_y = rospy.get_param("~off_y")
        self.abcd = rospy.get_param("~abcd")
        self.maximum_time = rospy.get_param("~maximum_time")
        self.sg = savitzky.savitzky_golay(window_size=self.wsize, order=self.filter_order)
        size = 2*self.wsize+1
        self.volt_filt = 48000*np.ones(size)

        rospy.Subscriber("~voltage", Float64, self.voltage_callback)
        rospy.Subscriber("~temperature", Float64, self.temperature_callback)

        self.pub_power = rospy.Publisher('/power_state', PowerState, queue_size=1)
        self.msg_power = PowerState()

    def voltage_callback(self, msg):

        self.volts_raw = msg.data
        self.volts_filtered = self.volts_raw * 1000

        if(self.volts_filtered <= 44000):
            self.volts_filtered = 44000
            time_r = 0.
        elif(self.volts_filtered >= 48000):
            self.volts_filtered = 48000

    def temperature_callback(self, msg):

        self.temperature = msg.data

    def process_voltage(self):

        self.msg_power.header.stamp = rospy.Time.now()

        if (self.volts_filtered != None):
            self.volt_filt = np.insert(self.volt_filt, 0, self.volts_filtered)
            self.volt_filt = np.delete(self.volt_filt, -1)

            vfilt = self.sg.filter(self.volt_filt)

            old_settings = np.seterr(all='raise')

            self.t_est = np.polyval(self.abcd, vfilt[self.wsize])

            self.t_est = vfilt[self.wsize]*sin(self.theta) + self.t_est*cos(self.theta)
            self.t_est = self.t_est + self.off_y

            if(self.t_est <0):
                self.t_est = 0

            self.msg_power.voltage = self.volts_raw
            self.msg_power.time_remaining = self.t_est
            #self.msg_power.prediction_method = '3rd_order_polynom'
            self.msg_power.relative_remaining_capacity = (self.t_est/self.maximum_time) * 100

        if (self.temperature != None):
            self.msg_power.temperature = self.temperature

        self.msg_power.charging = 0

        self.pub_power.publish(self.msg_power)

if __name__ == '__main__':
    rospy.init_node('volt_filt')
    vf = volts_filter()

    while not rospy.is_shutdown():
        vf.process_voltage()
        rospy.sleep(1.0)
