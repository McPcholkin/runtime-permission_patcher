
debug_lvl=2

log_file='/storage/emulated/0/runtime_perm_magisk_log.txt'
python_bin='/system/usr/share/python/bin/python3.4'
python_script_path='/system/usr/share/runtime-permissions_patcher/runtime-permissionsPatcher.py'

# Wait for boot to complete
until [ "$(getprop sys.boot_completed)" ]
  do
    sleep 2
  done

# I not think i need debug such simple script, 
# but fucking exec drop su after script start...
if [ $debug_lvl -ge 1 ]; then
  date_now=$(date)
  echo "Start script - $date_now" >> $log_file
fi

if [ -f $python_bin ]
  then
    if [ $debug_lvl -ge 1 ]; then
      echo "Python exist - $date_now" >> $log_file
    fi
    # exec drop su after run service.sh, so python run as user
    # if not run su again.
    if [ $debug_lvl -ge 1 ]; then
      exec su -c $python_script_path >> $log_file
    else
      exec su -c $python_script_path
    fi
    
  else
    echo "Python not installed! runtime-permissionsPatcher stop!" >> $log_file
    exit 1
fi

