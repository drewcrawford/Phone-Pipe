Phone Pipe Recipes
==================

When the compile's done
-----------------------
	
    $ make; phone

Get your IP addresses
---------------------

	$ ifconfig | grep inet | phone

Get your ethernet addresses
---------------------------
	
    $ ifconfig | grep ether | phone

Rtorrent (0.8.4+) notification on download complete
---------------------------------------------------

Add this line to ~/.rtorrent.rc:

	system.method.set_key = event.download.finished,notify_me,"execute=/usr/local/bin/phone,---title=rtorrent,$d.get_name="

Notify when user logs in on Mac OSX 10.3+
-----------------------------------------

Stick this in /Library/Scripts/login.sh:

    #!/bin/bash
	/usr/local/bin/phone ---username=<username> ---secret=<secret> ---title="`hostname` login" $1

Then run this:	
	
	sudo chmod +x /Library/Scripts/login.sh
    sudo defaults write com.apple.loginwindow LoginHook /Library/Scripts/login.sh
