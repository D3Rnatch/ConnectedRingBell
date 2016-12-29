
import os

import globals

#@class SystemLoader : loads system preferences
class SystemLoader :
  
   def __init__(self) :   
       self._confFile = globals.SYSTEM_PREF

   #@brief loadPwd : loads encrypted passwords from configuration file.
   def loadPwd(self) :
      try: 
       fi = open(self._confFile, 'r')
       read = True
      except: 
       print ("[ERROR] - configuration file not found : [" + _confFile + "]")
       read = False

      if read == True :
         li = []

         # read file (line by line)
         for line in fi :
           li.append(line[:-1]) # remove \n caracter
           print  ("[DEBUG] - read line [" + line[:-1] + "]")
         fi.close()
         return li
      else :
         return []
       
