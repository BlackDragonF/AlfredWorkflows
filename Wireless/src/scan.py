#!/usr/bin/python

import os
import sys
from xml.etree.ElementTree import Element, SubElement, tostring

reload(sys)
sys.setdefaultencoding("utf-8")

#Call built-in airport command
cmd_results = os.popen("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s").read().split("\n")
if len(cmd_results)>1:
    header = cmd_results.pop(0)
    cmd_results.pop()
else:
    exit()

#Extract information from output
formatter = {
        'SSID_end':     header.find('SSID')+4,
        'BSSID_beg':    header.find('BSSID'),
        'BSSID_end':    header.find('RSSI')-1,
        'RSSI_beg':     header.find('RSSI'),
        'RSSI_end':     header.find('CHANNEL')-1,
        'SECURITY_beg': header.find('SECURITY')
    }

output_results = []

for item in cmd_results:
    output_result = {}
    output_result['SSID']        =      item[0:formatter['SSID_end']].strip()
    output_result['BSSID']       =      item[formatter['BSSID_beg']:formatter['BSSID_end']].strip()
    output_result['RSSI']        =      item[formatter['RSSI_beg']:formatter['RSSI_end']].strip()
    output_result['SECURITY']    =      item[formatter['SECURITY_beg']:].strip()
    output_results.append(output_result)

#Generate XML
items = Element('items')
for result in output_results:
    item = SubElement(items, 'item', {'autocomplete':result['SSID'], 'uid':result['BSSID'], 'arg':result['SSID']})
    title = SubElement(item, 'title')
    title.text = result['SSID']
    subtitle = SubElement(item, 'subtitle')
    subtitle.text = 'RSSI:'+result['RSSI']+'\t\t\t\t'+'Security:'+result['SECURITY']
    icon = SubElement(item, 'icon')
    icon.text = 'icon.png'

print tostring(items)
