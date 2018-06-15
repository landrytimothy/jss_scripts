#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Tim Landry
# This simple script should run on newer MacOS machines and will trigger a jss unenroll from a client. Useful to include with a reimage policy.

import urllib2
import subprocess

jss_url = "Your JSS base url" + "JSSResource/computers/serialnumber/"
api_user = "API Username"
api_token = "API Passphrase"

# Call subprocess to get client serial number
def get_serial_number():
    command = "system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    serial, error = process.communicate()
    return serial.strip()

#Append serial number to api call
full_url = jss_url + get_serial_number()
req = urllib2.Request(full_url)

#Setting http method to 'DELETE'
req.get_method = lambda: 'DELETE'

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, full_url, api_user, api_token)

auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)
urllib2.install_opener(opener)
handler = urllib2.urlopen(req)

print handler.read()
