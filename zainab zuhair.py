#it does not happen because if we change the key we get adifferent result.to solve this qestion we enter the key in the encryption state and another key in the decryption state and compare the result
def encrypt(txt,key):
cipher_text=[]
for len in txt:
    pos= ord(len)
    new_mesg =chr(pos+key)
    cipher_text.append(new_mesg)
    a=''.join(cipher_text)
    print(a)
    text="wasit"
    key=4
    def decrypt(cipher_text,key):
for len in cipher_text:
    pos= ord(len)
    new_mesg=chr(pos-key)
    plain_text.append(new_mesg)
    b=''.join(plain_text)
    print(b)
    text="AEWMX"
    key=2
    encrypt(text,key)
    decrypt(cipher_text,key)
    
from playsound import playsound
playsound('birds.mp3')
