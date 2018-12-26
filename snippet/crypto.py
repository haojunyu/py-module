#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pip install pycrypto

# 导入所用模块 -- sys 是常用的模块 
import sys
from Crypto.Cipher import AES
from binascii import a2b_hex,b2a_hex

class AESCrypt():
    def __init__(self, key='0123456789abcdef', iv='iv'):
        # len(key)=16:aes-128; 24:aes-192; 32:aes-256
        self.key = self._align(key,True)
        self.mode = AES.MODE_CBC
        self.iv = self._align(iv)

    def _align(self, string, isKey=False):
        if isKey:
            # len(key)=16
            if len(string) >= 16:
                return string[0:16]
            else:
                return self._align(string)
        else:
            zeroNum = 16-len(string)%16
            string = string + '\0'*zeroNum
            return string

    def encrypt(self, text):
        plain = self._align(text)
        aesCipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        cipher = aesCipher.encrypt(plain)
        return b2a_hex(cipher)

    def decrypt(self, cipher):
        aesCipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        plain = aesCipher.decrypt(a2b_hex(cipher))
        return plain.rstrip('\0')

# 代码写在main()里面
def main():
  aes = AESCrypt()
  fIn = open('data/plain.txt','r')
  fOut = open('data/cipher.txt','w')
  cipher = aes.encrypt(fIn.read())
  fOut.write("%s" % cipher)
  fIn.close()
  fOut.close()


  fIn = open('data/cipher.txt','r')
  fOut = open('data/plain_new.txt','w')
  plain = aes.decrypt(fIn.read())
  #print plain
  fOut.write(plain)
  fIn.close()
  fOut.close()


# 调用main()函数来启动程序的样板
if __name__ == '__main__':
  reload(sys)
  sys.setdefaultencoding('utf-8')
  main()
