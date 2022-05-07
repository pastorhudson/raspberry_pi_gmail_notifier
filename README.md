# Raspberry Pi Gmail Notifier

This script checks gmail and turns on a pin if there is new email.

This has been updated to use the gmail oauth api.

There is now a requirement to load the gmail api libraries

## 1 INSTALL
### Clone The Repo
`git clone https://github.com/pastorhudson/raspberry_pi_gmail_notifier.git`

### Install Requirements
`pip install requirements.txt`

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

## 3 Add credentials.json
There is too many steps to explain how to get credentials.json, but you can see how here:
https://www.thepythoncode.com/article/use-gmail-api-in-python

Place credentials.json in the directory you are running the script from.
That is probably /home/pi if you are executing from a startup script.

## 4 Run the script
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

### Rpi.GPIO Errors
Install Rpi.GPIO if it's not already installed.
- `sudo apt-get update`
- `sudo apt-get install rpi.gpio`