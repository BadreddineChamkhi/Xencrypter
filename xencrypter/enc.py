#!usr/bin/python
#Coded By Badreddine Chamkhi 
#Xencrypter Sat 21:38
#Don't Change My Copyrights :) 
#ShareOut To All Fallga Team Tunisian Cyber Resistance <3
# -*- coding: utf-8 -*-
#import Zone
import hashlib
import os
from platform import system
##################################
##################################
##########ClearScreen#############
##################################
##################################
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
clear()
#################################
#################################
#########TermaBerda##############
#################################
#################################
banner = ''' \033[1;34m
		                        #     #                                                              
					 #   #  ###### #    #  ####  #####  #   # #####  ##### ###### #####  
					  # #   #      ##   # #    # #    #  # #  #    #   #   #      #    # 
					   #    #####  # #  # #      #    #   #   #    #   #   #####  #    # 
					  # #   #      #  # # #      #####    #   #####    #   #      #####  
					 #   #  #      #   ## #    # #   #    #   #        #   #      #   #  
					#     # ###### #    #  ####  #    #   #   #        #   ###### #    #
													v 1.0
\033[1;m
'''	
print banner
author = ''' 
					   \033[1;42mCoded By Badreddine Chamkhi\033[1;m
'''
print author			
text = str(raw_input('\033[1;37m>Enter Text :\033[1;m'))
hash_type = str(raw_input('\033[1;37m>Enter HASH Type : \033[1;m'))
text = text.encode('utf-8')
hash_hash = hashlib.new(hash_type)
hash_hash.update(text)
print '''\033[1;41m[+] Job Completed !\033[1;m''' 
hasher = hash_hash.hexdigest()
print(hasher)
