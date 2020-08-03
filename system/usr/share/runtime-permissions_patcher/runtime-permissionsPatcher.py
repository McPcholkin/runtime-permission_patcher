#!/system/usr/share/python/bin/python3.4
# -*- coding: utf-8 -*-

import xml.etree.ElementTree
import os

# Debug LVL
# 0 - Debug off
# 1 - Only patch info
# 2 - More verbouse
debug = 0

FILE_PATH = '/data/system/users/0/runtime-permissions.xml'
XML_HEADER = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>\n"

# Open input file
file_input = open(FILE_PATH, "r")

# Read original file
et = xml.etree.ElementTree.parse(file_input)

# Close input file
file_input.close()

# Get root tree
et_root = et.getroot()

# Start replace
for child in et_root.iter('pkg'):
  if debug >= 2:
    print('D: ', child.tag, ' = ', child.attrib)
    
  
  # Serach AFWall+ permissions
  if child.get('name') == 'dev.ukanth.ufirewall.donate':
    if debug >= 1:
      print('D: Found: ', child.get('name'))
    
    # Serach needed item
    for item in child.iter('item'):
      if debug >= 2:
        print(item.attrib) 
      
      # Patch WRITE_EXTERNAL_STORAGE
      if item.get('name') == 'android.permission.WRITE_EXTERNAL_STORAGE':
        if debug >= 1:
          print('D: Found: ', item.get('name'), ' with flags = ', item.get('flags'))
        
        # Check if flags not right
        if item.get('flags') != '3320':
          if debug >= 1:
            print('D: Patch flags: ', item.get('name'))
            
          # Set new flags
          item.set('flags', '3320')
          
          # Check if new flags is correct
          if debug >= 1:
            print('D: Flags patched to: ', item.get('flags'))
            
        # Skip it flags already correct  
        else:    
          if debug >= 1:
            print('D: ', item.get('name'), ' Already patched!')
     

     # Patch READ_EXTERNAL_STORAGE
      if item.get('name') == 'android.permission.READ_EXTERNAL_STORAGE':
        if debug >= 1:
          print('D: Found: ', item.get('name'), ' with flags = ', item.get('flags'))
        
        # Check if flags not right
        if item.get('flags') != '3320':
          if debug >= 1:
            print('D: Patch flags: ', item.get('name'))
            
          # Set new flags
          item.set('flags', '3320')
          
          # Check if new flags is correct
          if debug >= 1:
            print('D: Flags patched to: ', item.get('flags'))
            
        # Skip it flags already correct  
        else:    
          if debug >= 1:
            print('D: ', item.get('name'), ' Already patched!')
            
            
            

  # Serach microG GmsCore permissions
  elif child.get('name') == 'com.google.android.gms':
    if debug >= 1:
      print('D: Found: ', child.get('name'))
    
    # Serach needed item
    for item in child.iter('item'):
      if debug >= 2:
        print(item.attrib) 
      
      # Patch WRITE_EXTERNAL_STORAGE
      if item.get('name') == 'android.permission.ACCESS_BACKGROUND_LOCATION':
        if debug >= 1:
          print('D: Found: ', item.get('name'), ' with flags = ', item.get('flags'))
        
        # Check if flags not right
        if item.get('flags') != '3320':
          if debug >= 1:
            print('D: Patch flags: ', item.get('name'))
            
          # Set new flags
          item.set('flags', '3320')
          
          # Check if new flags is correct
          if debug >= 1:
            print('D: Flags patched to: ', item.get('flags'))
            
        # Skip it flags already correct  
        else:    
          if debug >= 1:
            print('D: ', item.get('name'), ' Already patched!')
        

      
      
# To avoid use external lib add header string by hands
# xml lib not support standalone='yes' parameter

# Writr body to temp file
et.write(FILE_PATH + ".patched")

# Open output file
file_output = open(FILE_PATH + ".new", "w")

# Write header
file_output.write(XML_HEADER)

# Open patched file 
file_patched = open(FILE_PATH + ".patched", "r")


# Rewrite xml
for line in file_patched:
    file_output.write(line)
    
    
file_patched.close()
file_output.close()

# Replace files
os.remove(FILE_PATH)
os.remove(FILE_PATH + ".patched")

os.rename(FILE_PATH + ".new", FILE_PATH)

