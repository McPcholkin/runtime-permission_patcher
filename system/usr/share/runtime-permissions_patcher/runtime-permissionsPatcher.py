#!/system/usr/share/python/bin/python3.4
# -*- coding: utf-8 -*-

import xml.etree.ElementTree
import os

# Debug LVL
# 0 - Debug off
# 1 - Only patch info
# 2 - More verbouse
debug = 1

FILE_PATH = '/data/system/users/0/runtime-permissions.xml'
XML_HEADER = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>\n"
changes_counter = 0

apps_dict = {
  'dev.ukanth.ufirewall.donate': {
    'WRITE_EXTERNAL_STORAGE' : '3320',
    'READ_EXTERNAL_STORAGE' : '3320'
    },
  'com.google.android.gms': {
    'ACCESS_BACKGROUND_LOCATION' : '3320'
    },
  'org.microg.nlp': {
    'ACCESS_BACKGROUND_LOCATION' : '3320'
    },
  'com.google.android.gms': {
    'ACCESS_BACKGROUND_LOCATION' : '3320'
    },
  'org.fitchfamily.android.dejavu': {
    'ACCESS_BACKGROUND_LOCATION' : '3320'
    },
  'org.fitchfamily.android.wifi_backend': {
    'ACCESS_BACKGROUND_LOCATION' : '3320'
    },
  'org.fitchfamily.android.gsmlocation': {
    'ACCESS_BACKGROUND_LOCATION' : '3320',
    'WRITE_EXTERNAL_STORAGE' : '3320',
    'READ_EXTERNAL_STORAGE' : '3320',
    'ACCESS_MEDIA_LOCATION' : '3320',
    'ACCESS_COARSE_LOCATION' : '3320'
    },
  'com.jbak2.JbakKeyboard': {
    'WRITE_EXTERNAL_STORAGE' : '3320',
    'READ_EXTERNAL_STORAGE' : '3320'
    }
    
 }

# Open input file
file_input = open(FILE_PATH, "r")

# Read original file
xml_et = xml.etree.ElementTree.parse(file_input)

# Close input file
file_input.close()

# Get root tree
et_root = xml_et.getroot()

# Main logic
for app_id, app_perms in apps_dict.items():
  if debug >= 2:
    print('D: set app: ', app_id)

  # Start replace
  for child in et_root.iter('pkg'):
    if debug >= 2:
      print('D: ', child.tag, ' = ', child.attrib)
   
    # Serach app in permissions list
    if child.get('name') == app_id:
      if debug >= 1:
        print('D: Found: ', child.get('name'))
    
      # Serach needed item
      for item in child.iter('item'):
        if debug >= 2:
          print('D:  Item: ', item.attrib) 
      
        for perm_id in app_perms:
          if debug >= 2:
            print('D: ', perm_id, ' : ', app_perms[perm_id])
 
          # Patch permission
          perm_id_full = 'android.permission.' + perm_id

          if item.get('name') == perm_id_full:
            if debug >= 1:
              print('D: Found: ', item.get('name'), ' with flags = ', item.get('flags'))

            # Check if flags not correct
            if item.get('flags') != app_perms[perm_id]:
              if debug >= 1:
                print('D: Patch flags: ', perm_id)
            
              # Set new flags
              item.set('flags', app_perms[perm_id])

              # Update Counter
              global changes_counter
              changes_counter = changes_counter + 1
          
              # Check if new flags is correct
              if debug >= 1:
                print('D: Flags patched to: ', item.get('flags')) 

            # Skip if flags already correct  
            else:    
              if debug >= 1:
                print('D: ', perm_id, ' Already patched!')

if debug >= 1:
  print('D: Candges: ', changes_counter)

if changes_counter > 0:
  if debug >= 1:
    print('D: Permissions need update')
     
  # To avoid use external lib need add header string by hands
  # xml lib not support standalone='yes' parameter

  # Write body to temp file
  xml_et.write(FILE_PATH + ".patched")

  # Open output file
  file_output = open(FILE_PATH + ".new", "w")

  # Write header
  file_output.write(XML_HEADER)

  # Open patched file 
  file_patched = open(FILE_PATH + ".patched", "r")

  # Rewrite xml body
  for line in file_patched:
    file_output.write(line)
    
  # Close files
  file_patched.close()
  file_output.close()

  # Replace files
  os.remove(FILE_PATH)
  os.remove(FILE_PATH + ".patched")

  os.rename(FILE_PATH + ".new", FILE_PATH)


