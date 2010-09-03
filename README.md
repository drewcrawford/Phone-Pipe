Phone Pipe
==========

Phone Pipe lets you send push notifications to your iPhone/iPod Touch/iPad
from the command line. You'll need to have the Notifo app (its free!) installed
on your device as well as an account on their website (also free!).


Installation
------------

Just copy the script to somewhere on your path.

    $ sudo cp phone /usr/local/bin/

For Python <= 2.4 users, you'll need to have the simplejson package installed
for the JSON support. You can find it [here][simplejson] or install it with
easy_install if you have that handy:

    $ sudo easy_install simplejson

[simplejson]: http://pypi.python.org/pypi/simplejson/


Configuration
-------------

The first time you run Phone Pipe it will prompt you for your credentials. It
will store these in ~/.phonepipe for future use. Alternatively you can also
specify your username and API key on the command line like such:

    $ phone --username=someuser --secret=b52e5fd8b6f14d799798172c1b62c7eb


Usage
-----

phone [options] [--] [msg]

The options are described below.  If you are concerned about the message given
on the command line containing dashes and therefore looking like arguments, you
may include a double dash before the message give on the command line.

    --title - The title of the message.
    --label - A message label, generally the name of the sending service.
    --url - If specified, the Notifo app makes a link from the message to it.
    --username - Override your ~/.phonepipe if you specify a secret as well.
    --secret - Override your ~/.phonepipe when specified with a username.


Messages are taken from unknown command line arguments and stdin. The
following are all equivalent:

    $ phone send a message
    $ phone "send a message"
    $ echo "send a message" | phone

Examples
--------
    
    # First message
    $ phone first message

    # Notify yourself when the compile is done
    $ make; phone

    # Notify yourself of your current IP
    $ ifconfig | grep inet | phone

