make_magisk_module: 
	zip -r runtime-permission_patcher.zip \
	META-INF \
    LICENSE \
	README.md \
	module.prop \
	customize.sh \
	service.sh \
	system 


clean: 
	rm runtime-permission_patcher.zip
