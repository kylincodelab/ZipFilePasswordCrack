#!/usr/bin/env python
#-*- coding: utf-8 -*-
#author:lazynms

import zipfile
import os
import sys

#Zip CrackFunction
def ZipCrackFuc(zipfilename,password):
	try:
		zipFile=zipfile.ZipFile(zipfilename)
		zipFile.extractall(pwd=str(password))
		return True
	except Exception, e:
		return False

clear = lambda: os.system('cls')

def main():

	if len(sys.argv)==3:
		ZipFileName=sys.argv[1]
		PassWordFileName=sys.argv[2]
		if not os.path.isfile(ZipFileName):
			print "[-] "+ZipFileName+" does not exists..."
			exit(0)
		if not os.access(PassWordFileName,os.R_OK):
			print "[-] "+PassWordFileName+" access denied..."
			exit(0)
		#everything ok! let's try to crack it
		print "[+] Cracking ...."
		pwdfilenamefp=open(PassWordFileName,"r") #open the password
		# try every password if succeed and return True
		for linepassword in pwdfilenamefp:
			crackpassword=linepassword.split()[0]

			CrackResult=ZipCrackFuc(ZipFileName,crackpassword)
			# If Ret True and then break
			if CrackResult == True:
				print "[+] "+"Crack Success!"+" PassWord: "+crackpassword
				break
			else:
				continue
		pwdfilenamefp.close()
	else:
		print "[-]\t "+"Usage:"
		print "[-]\t "+sys.argv[0]+" Crack.zip(Your Zipfile) "+" pass.txt(Your Password File)"

	print "[+] "+"Cracking End..."
if __name__=="__main__":
	main()