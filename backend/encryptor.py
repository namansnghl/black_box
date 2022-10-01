from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode


class Manager:
    def __init__(self):
        self.__salt = b'7+W\xa4Ym\xf3/\xbc\x9d\xcd\xae\x1aW\xdfD\x02\x84\xfak>\x86\xbdt\xb4\xd6\xe6\xc6\x8f\xfe\x19\x01'
        self.jingle = self.__jingler('137')

    def __jingler(self, card: str) -> str:  # TO DO
        jingle = card
        christmas_function = lambda x: ('1s[7!Qws' * (int(x[-1]) % 3)) + str((int(x) ** 4) % 1123519)
        for _ in range(10):
            jingle += christmas_function(jingle[-3:])
        return jingle

    def encrypt(self, plaintext: str) -> str:
        # returns encrypted stuff
        __hash = PBKDF2(self.jingle, self.__salt, dkLen=32)
        cipher = AES.new(__hash, AES.MODE_CBC)
        plaintext = bytes(plaintext, encoding='utf-8')
        cyphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        cyphertext = b"".join([cipher.iv, cyphertext])
        cyphertext = b64encode(cyphertext).decode('utf-8')
        del __hash, cipher, plaintext
        return cyphertext

    def decrypt(self, cyphertext: str) -> str:
        # returns decrypted stuff
        __hash = PBKDF2(self.jingle, self.__salt, dkLen=32)
        cyphertext = b64decode(cyphertext)
        cipher = AES.new(__hash, AES.MODE_CBC, iv=cyphertext[:16])
        plaintext = unpad(cipher.decrypt(cyphertext[16:]), AES.block_size).decode()
        del __hash, cipher
        return plaintext