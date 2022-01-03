# Raspberry Pi Gmail Notifier

This script checks the gmail atom feed and turns on a pin if there is new email.

Gmail atom feed url: https://mail.google.com/mail/feed/atom

It looks at the fullcount tag and if it's greater than 0 it turns on the PIN configured in config.ini

There are no dependencies outside of Python Standard Library and RPi.GPIO.

## 1 INSTALL
### Clone The Repo
`git clone https://github.com/pastorhudson/raspberry_pi_gmail_notifier.git`

#### Install Rpi.GPIO if it's not already installed.
- `sudo apt-get update`
- `sudo apt-get install rpi.gpio`

## 2 Edit config.ini
Change the values in config.ini to configure the script.
### Example config.ini
```ini
[DEFAULT]
# Must Be GMAIL!
EMAIL = someemail@gmail.com
PASS = secretpass
# The PIN to toggle
PIN = 14
# How Many Seconds to Wait between Checking Email
SECONDS = 10
```

## 3 Run the script
`python3 check_messages_atom.py` OR `checkgmail.sh`
Both scripts will execute forever until exited with `CTRL+c`

### Errors

```python
  File "check_messages_atom.py", line 39
    print(f"Setting PIN: {config['DEFAULT']['PIN']} to {status}")
                                                               ^
SyntaxError: invalid syntax
```
This error means you are using an unsupported version of python.
FIX: Make sure you are using python >= 3.8