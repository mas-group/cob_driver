^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package cob_sound
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.6.5 (2015-08-31)
------------------
* fix dependencies
* Contributors: ipa-fxm

0.6.4 (2015-08-25)
------------------
* boost revision
* do not install headers in executable-only packages
* explicit dependency to boost
* alsa-oss dependency
* fixing dependencies
* remove obsolete autogenerated mainpage.dox files
* remove trailing whitespaces
* add_dependencies EXPORTED_TARGETS
* migrate to package format 2
* merge
* deleted name argument and added a comment
* update cob_sound
* sort dependencies
* critically review dependencies
* play sound
* Contributors: ipa-fxm, ipa-nhg

0.6.3 (2015-06-17)
------------------
* merge with ipa320
* adapt test script for sound
* use component namespaces for light, mimic and say
* add visualization marker to sound
* use Timer for diagnostics
* add hardware_id to sound
* reduce diagnostics frequency to 1Hz
* use new Trigger from std_srvs
* move cob_sound launch file to cob_bringup
* Contributors: ipa-fmw, ipa-fxm

0.6.2 (2014-12-15)
------------------
* Merge branch 'indigo_dev' into indigo_release_candidate
* missed dependency
* missed dependency
* Contributors: Florian Weisshardt, ipa-cob4-2, ipa-nhg

0.6.1 (2014-09-17)
------------------

0.6.0 (2014-09-09)
------------------

0.5.7 (2014-08-26)
------------------
* Merge pull request `#163 <https://github.com/ipa320/cob_driver/issues/163>`_ from ipa320/hydro_dev
  updates from hydro_dev
* 0.5.6
* update changelog
* merge
* Cleaned up cob_driver with reduced deps to compile on indigo
* Merge pull request `#135 <https://github.com/ipa320/cob_driver/issues/135>`_ from ipa320/hydro_release_candidate
  bring back changes from Hydro release candidate
* New maintainer
* Contributors: Alexander Bubeck, Florian Weisshardt, Nadia Hammoudeh García, ipa-nhg

0.5.6 (2014-08-26)
------------------
* Merge pull request `#163 <https://github.com/ipa320/cob_driver/issues/163>`_ from ipa320/hydro_dev
  updates from hydro_dev
* merge
* Cleaned up cob_driver with reduced deps to compile on indigo
* Merge pull request `#135 <https://github.com/ipa320/cob_driver/issues/135>`_ from ipa320/hydro_release_candidate
  bring back changes from Hydro release candidate
* New maintainer
* Contributors: Alexander Bubeck, Florian Weisshardt, Nadia Hammoudeh García, ipa-nhg

0.5.3 (2014-03-31)
------------------
* install tags
* Contributors: ipa-fxm

0.5.2 (2014-03-20)
------------------

0.5.1 (2014-03-20)
------------------
* remove duplication
* remove duplication
* add dependency to sound_play
* fix dependencies
* workaround for cepstral on ubuntu 12.04
* Installation stuff
* Some small dependency tweaks.
* fix timing bug
* timing big fix
* cleaned up CMakeLists and added install directives
* further modifications for catkin, now everything is compiling and linking
* futher include and linkpath modifications
* add message dependencies
* compiling but still some linker errors
* Second catkinization push
* First catkinization, still need to update some CMakeLists.txt
* add diagnostics to sound
* add mute and unmute service to sound
* cleanup in sound
* action handle fix
* handle return value
* changes for fuerte compatibility
* merge
* update deps
* added roslaunch tests
* fetch and carry on cob3-3
* cepstral voice as mode
* rearranging cob_camera_sensors launch files
* del files
* sound with cpp
* cob_sound package added
* Contributors: Alexander Bubeck, Richard Bormann, abubeck, cpc-pk, ipa-cob3-3, ipa-fmw, ipa-fxm
