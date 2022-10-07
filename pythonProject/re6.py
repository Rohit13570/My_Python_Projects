import re
pattern="[0-9][a-z][A-Z]"
if re.match(pattern,"8pP"):
    print ("matched")
else:
    print("not matched")