from Crypto.Cipher import DES
from Crypto import Random

global plain
global cipher
global done
global x
done = False
plain = ""
cipher = ""


class DES:
    def setKey(self,key):
        global done,x
        try:
            self.key = key
            if len(self.key) == 8:
                done = True
                x = DES.new(self.key,DES.MODE_ECB)
        except:
            pass

    def encrypt(self,plainText):
        global cipher, done, x
        self.plainText = plainText

        while len(self.plainText) % 8 != 0:
            self.plainText += '*'
        
        if Success:
            cipher = obj.encrypt(self.plainText)
            return cipher
        else:
            print("Invalid Key")
            return self.plainText

    def decrypt(self,cipherText):
         global plain, done, x
        self.cipherText = cipherText
        if Success:
            plain = obj.decrypt(self.cipherText)
            return plain
        else:
            print("Invalid Key")
            return self.cipherText