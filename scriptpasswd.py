#! python 3
import sys
import pyperclip
PASSWORDS = {
        "Gmail":"SUPERpuperSEcetpasswd@!#",
        "Youtube":"MEGA_Super_PS+$+=123",

        "Netflix":"THE_BEst_passwd_you_can_ever_see"
}


if len(sys.argv) < 2:
    print("Using: script  name acc  - copy pass in buffer")
    sys.exit()
account = sys.argv[1] # first  argument in script name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("pass for account is copy" + account + "in buffer")
else:
    print("pass for account is not copy" + account + "is not in the list")