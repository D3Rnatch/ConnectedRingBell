
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
           # don't keep comments
           if line[0] != globals.COMMENT: 
              # remove inline comments
              nl = line.split(globals.COMMENT, 1)[0]
              li.append(nl) # remove \n caracter
              print  ("[DEBUG] - read line [" + nl + "]")
         fi.close()
         return li
      else :
         return []
       
