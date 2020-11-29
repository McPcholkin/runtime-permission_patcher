make_magisk_module: 
	zip -r runtime-permission_patcher.zip \
	META-INF \
    LICENSE \
	README.md \
	module.prop \
	customize.sh \
	service.sh \
	system 

push:
	adb push runtime-permission_patcher.zip /sdcard/

clean: 
	rm runtime-permission_patcher.zip
