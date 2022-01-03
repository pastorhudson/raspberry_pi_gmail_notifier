import sys
from xml.etree import ElementTree
import configparser
from http.client import HTTPSConnection
from base64 import b64encode
import RPi.GPIO as GPIO




config = configparser.ConfigParser()
config.read('config.ini')


def get_inbox_count():
    # This sets up the https connection
    c = HTTPSConnection("mail.google.com")
    # we need to base 64 encode it
    # and then decode it to acsii as python 3 stores it as a byte string
    userAndPass = b64encode(bytes(config['DEFAULT']['EMAIL'] + ':' + config['DEFAULT']['PASS'], "utf-8")).decode("ascii")

    headers = {'Authorization': 'Basic %s' % userAndPass}
    # then connect
    c.request('GET', '/mail/feed/atom', headers=headers) # The GMAIL RSS FEED
    # get the response back
    res = c.getresponse()
    # at this point you could check the status etc
    # this gets the page text
    data = res.read()
    root = ElementTree.fromstring(data)
    try:
        return int(root[2].text)
    except Exception as e:
        print('Could not check gmail. Please Check config.ini file.')


def set_gpio(status):
    print(f"Setting PIN: {config['DEFAULT']['PIN']} to {status}")

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) # tell the Pi what headers to use
    GPIO.setup(int(config['DEFAULT']['PIN']), GPIO.OUT) # tell the Pi this pin is an output

    # there are unread emails, turn light on
    GPIO.output(int(config['DEFAULT']['PIN']), status)
    ##Flash Screen if order exists
    #subprocess.call("DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority /usr/bin/xset -display :0 dpms force off; sleep 0.5; DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority /usr/bin/xset -display :0 dpms force on; sleep 0.5; DISPLAY=:0.0 XA$


if __name__ == '__main__':
    if not (sys.version_info.major == 3 and sys.version_info.minor >= 8):
        print("This script requires Python 3.8 or higher!")
        print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
        sys.exit(1)
    inbox_count = get_inbox_count()
    print(f"INBOX COUNT: {inbox_count}")

    if inbox_count > 0:
        set_gpio(True)
    else:
        set_gpio(False)
