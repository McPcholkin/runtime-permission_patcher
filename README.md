# Fix permissions for old apps systemization on Android 10

Magisk module to fix permissions for:

* AFWall+
* GmsCore-v0.2.11.202414
* UnifiedNlp
* DejaVu-v1.1.12

Requiered [Python 3.4 magisk module](https://github.com/McPcholkin/python_installer_for_android) to work

## How to make magisk module:
- Clone repo (or download as zip)
- Add repo files inside zip archive to get structure as described in [Magisk Developer Guides](https://topjohnwu.github.io/Magisk/guides.html)  
- Install module using Magisk Manager
- Reboot device 2 times (to run module at least once)
- You can disable\uninstall module after second reboot, file already patched.

## Thanks:
- **7175** for [python binary](https://forum.xda-developers.com/android/software-hacking/scripting-python-static-2-7-8-3-4-2-t2958679) 
- **GeographicCone** for [permission temporary fix for GmsCore](https://github.com/microg/android_packages_apps_GmsCore/issues/1099#issuecomment-664419033)
- **funnypc** for [Wait for boot to complete example](https://forum.xda-developers.com/showpost.php?p=80023043&postcount=6&__cf_chl_jschl_tk__=724d6e8b8379b1a2f40fd052407acac7cabe5592-1596478744-0-AcUXl-ADKDR7hBZYFjpPvyFP3np4nlu1Qu-M7BvpzmloKo3HJZtn8nlsOUKVzWXbAEjI0bLwx_HYkbYx23LeSaWTkkCvQEZq0S6QYyKEsuhXpSjkLYAW8DxWsn1747ote9UNOzQdZJLclrNvZCEDFjRdOrQRGJSm3Kx38XkANVc-cpFejP4ifbvyeGRVbUiH78CR1jyoX0kFbhGUheHho5H-652OKa0GgY5tAiy_5OB3SXYkIvQFGJlecAtSW_JCy3DLdngeujP3CwlSO1uIlffW8MhtO33-76_buF9R4TW4bRO_TC3nCeXqE0gb_4fjX_nQC_0tG3qUmdZH_9SPotFrDZ5Ptxyk4oJYYNq1rrFLaL3TfSLu-my2YlXR-RBBDg)


