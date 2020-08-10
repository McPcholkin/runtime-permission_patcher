# Fix permissions for old apps systemization on Android 10

Magisk module to fix permissions for:

* [AFWall+ 3.3.1](https://github.com/McPcholkin/afwall_installer)
* [GmsCore 0.2.11.202414](https://github.com/McPcholkin/microG_installer_Q)
* [UnifiedNlp 1.6.8](https://github.com/McPcholkin/unifiednlp_installer)
* [DejaVu 1.1.12](https://github.com/McPcholkin/dejavu_installer)
* [LocalWifiNlpBackend 1.1.13](https://github.com/McPcholkin/local_wifi_nlp_backend_installer)
* [LocalGsmNlpBackend 0.0.1.4](https://github.com/McPcholkin/local_gsm_nlp_backend_installer)
* [Jbak2 Keyboard](https://github.com/McPcholkin/jbak2_keyboard_installer)

Requiered [Python 3.4 magisk module](https://github.com/McPcholkin/python_installer_for_android) to work

## How to make magisk module:
- Clone repo (or download as zip)
- Add repo files inside zip archive to get structure as described in [Magisk Developer Guides](https://topjohnwu.github.io/Magisk/guides.html)  
- Install module using Magisk Manager
- Reboot device 2-5 times to all apps been patched (it take couple reboots, and after adding other supported modules, usualy first install take 2-5 reboots)
- You can disable\uninstall module after all apps in file already patched.

## Thanks:
- **7175** for [python binary](https://forum.xda-developers.com/android/software-hacking/scripting-python-static-2-7-8-3-4-2-t2958679) 
- **GeographicCone** for [permission temporary fix for GmsCore](https://github.com/microg/android_packages_apps_GmsCore/issues/1099#issuecomment-664419033)
- **funnypc** for [Wait for boot to complete example](https://forum.xda-developers.com/showpost.php?p=80023043&postcount=6&__cf_chl_jschl_tk__=724d6e8b8379b1a2f40fd052407acac7cabe5592-1596478744-0-AcUXl-ADKDR7hBZYFjpPvyFP3np4nlu1Qu-M7BvpzmloKo3HJZtn8nlsOUKVzWXbAEjI0bLwx_HYkbYx23LeSaWTkkCvQEZq0S6QYyKEsuhXpSjkLYAW8DxWsn1747ote9UNOzQdZJLclrNvZCEDFjRdOrQRGJSm3Kx38XkANVc-cpFejP4ifbvyeGRVbUiH78CR1jyoX0kFbhGUheHho5H-652OKa0GgY5tAiy_5OB3SXYkIvQFGJlecAtSW_JCy3DLdngeujP3CwlSO1uIlffW8MhtO33-76_buF9R4TW4bRO_TC3nCeXqE0gb_4fjX_nQC_0tG3qUmdZH_9SPotFrDZ5Ptxyk4oJYYNq1rrFLaL3TfSLu-my2YlXR-RBBDg)


