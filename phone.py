#!/usr/bin/env python
"""This program is free software. It comes without any warranty, to
 * the extent permitted by applicable law. You can redistribute it
 * and/or modify it under the terms of the Do What The Fuck You Want
 * To Public License, Version 2, as published by Sam Hocevar. See
 * http://sam.zoy.org/wtfpl/COPYING for more details.
 
 If you do find a use for it, please consider submitting patches to http://github.com/drewcrawford/Phone-Pipe
 or just shooting me an e-mail at drew@sealedabstract.com"""


import urllib
import sys
import json


    
def install():
    import os
    print("Install dir [/usr/local/bin/]:"),
    dir = raw_input()
    if len(dir)==0:
        print "Installing... (you might need to be root for this to work...)"
        dir = "/usr/local/bin/"
    from shutil import copy
    dest_name = os.path.join(dir,"phone")
    copy(os.path.join(sys.path[0],sys.argv[0]),dest_name)
    os.system ("chmod +x %s" % dest_name)
    print "installed."
def super_open(file):
    import sys, os
    if sys.platform=="darwin":
        os.system("open %s" % file)
    elif sys.platform=="linux2":
        os.system("xdg-open %s" % file)
    else:
        os.startfile(file)
def get_settings_file():
    import os.path
    return os.path.expanduser("~/.phonepipe")
def get_credentials():
    import os.path
    if not os.path.exists(get_settings_file()):
        set_credentials()
    settingsfile = open(get_settings_file())
    settings = json.loads(settingsfile.read())
    return (settings["username"],settings["apisecret"])
def set_credentials():
    print "Username: ",
    username = raw_input()
    while True:
        import getpass
        secret = getpass.getpass("APISecret: (Leave blank to launch browser) ")
        if len(secret.strip())!=0:
            settingsfile = open(get_settings_file(),"w")
            settingsfile.write(json.dumps({"username":username,"apisecret":secret}))
            settingsfile.close()
            break
        else:
            super_open("http://notifo.com/user/settings")
    
    
def alert(msg,url=None,title="phonepipe",label="phonepipe"):  
    msg = msg.strip()
    data = {"title":title,"msg":msg,"label":label,"url":url==None and "" or url}
    try:
        file = urllib.urlopen("https://%s:%s@api.notifo.com/v1/send_notification"% get_credentials(),urllib.urlencode(data))
    except IOError: 
       print "An error ocurred making the HTTP request.  Maybe your credentials are wrong?"
       print "Error details: %s" % sys.exc_info()[1]
       set_credentials()
       alert(msg,url,title)
    result = file.read()
    
    result = json.loads(result)
    if result["status"]!="success" or result["response_message"] != "OK":
        print "Notifo reported an error."
        print result
        sys.exit(1)
    
        
        
msg = ""
url = None
title = "phonepipe"
label = "phonepipe"
if len(sys.argv) >1:
    for arg in sys.argv:
        if arg==sys.argv[0]: continue
        if arg.startswith("---"):
            if arg.startswith("---url="):
                url = arg[7:]
            elif arg.startswith("---title="):
                title=title=arg[9:]
            elif arg.startswith("---install"):
                install()
        else:
            msg += arg + " "
if not sys.stdin.isatty():
    msg += sys.stdin.read()
if msg=="":
    msg = "Phone Pipe Alert"
alert(msg,url=url,title=title,label=label)

