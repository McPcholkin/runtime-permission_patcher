#!/system/bin/sh

log_file='/storage/emulated/0/runtime_perm_magisk_log.txt'
python_bin='/system/usr/share/python/bin/python3.4'
python_script_path='/system/usr/share/runtime-permissions_patcher/runtime-permissionsPatcher.py'

# Check if python already installed
if [ -f $python_bin ]
  then
    ui_print "Python installed, all OK"
  else 
    ui_print "Python not installed, ABORT!"
    
    date_now=$(date) 
    echo "Python not installed! stop magisk install - $date_now" >> $log_file
    abort
fi

# Set permissions for scripts
set_perm $MODPATH/service.sh 0 0 755 
set_perm $MODPATH$python_script_path 0 0 755 