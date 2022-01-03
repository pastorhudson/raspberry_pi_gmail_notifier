# gmail_pi_notifier
Script that checks gmail and turns on pin if there is new email.

This script pulls the atom feed from: https://mail.google.com/mail/feed/atom

It looks at the <fullcount>int</fullcount> tag and if it's greater than 0 it turns on the PIN configured in config.ini

## 1 INSTALL
`git clone https://github.com/pastorhudson/raspberry_pi_gmail_notifier.git`

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


```

## 3 Run the script
`python3 check_messages_atom.py`

### Errors

```python
  File "check_messages_atom.py", line 39
    print(f"Setting PIN: {config['DEFAULT']['PIN']} to {status}")
                                                               ^
SyntaxError: invalid syntax
```
This error means you are using an unsupported version of python.
FIX: Make sure you are using python >= 3.8