from des import *
from aes import *

import sys

aes = aes()
des = des()


def cipher(cipher_name, secret_key, enc_dec, input_file, output_file):
    intext = ""
    outtext = ""
    
    print("The cipher name is :", cipher_name)
    print("The secret key  is :", secret_key)
    print("The operation is :", enc_dec)
    print("The input file is :", input_file)
    print("The output file is :", output_file)

    options = {"AES" : (aes.setKey, {"ENC" : aes.encrypt, "DEC" : aes.decrypt}),
               "DES" : (des.setKey, {"ENC" : des.encrypt, "DEC" : des.decrypt})}

    file = open(input_file, "r")
    for line in file:
        intext += line
    file.close()

    options[cipher_name][0](secret_key)

    outtext = options[cipher_name][1][enc_dec](intext)

    file = open(output_file, "w+")
    file.write(outtext)
    file.close

if __name__ == "__main__":
    a = str(sys.argv[1])
    b = str(sys.argv[2])
    c = str(sys.argv[3])
    d = str(sys.argv[4])
    e = str(sys.argv[5])
    cipher(a, b, c, d, e) 