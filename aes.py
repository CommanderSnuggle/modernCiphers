from Crypto.Cipher import AES
from Crypto import Random


global plain
global cipher
global Success
global obj
Success = False
plain = ""
cipher = ""


class aes:

    def setKey(self, key):
        global Success, obj
        try:
            self.key = key
            if len(self.key) == 16:
                Success = True
                obj = AES.new(self.key, AES.MODE_ECB)
        except:
            pass


    def encrypt(self, plainText):
        global cipher, Success, obj
        self.plainText = plainText

        while len(self.plainText) % 16 != 0:
            self.plainText += '*'
        
        if Success:
            cipher = obj.encrypt(self.plainText)
            return cipher
        else:
            print("Invalid Key")
            return self.plainText
        
        
    def decrypt(self, cipherText):
        global plain, Success, obj
        self.cipherText = cipherText
        if Success:
            plain = obj.decrypt(self.cipherText)
            return plain
        else:
            print("Invalid Key")
            return self.cipherText