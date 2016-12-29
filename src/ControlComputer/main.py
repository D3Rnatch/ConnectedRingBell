import os, sys

sys.path.insert(0,Comm)
sys.path.insert(1,Common)
sys.path.insert(2,Controller)

import SystemLoader
import Controller

if __name__ == "__main__" :
   
   print("[SERVER] - Starting the ringbell server...")

   # Load preferences 
   sl = SystemLoader.SystemLoader()
   pwds = sl.loadPwd()
   if len(pwds) != 0 :
      status = "OK"
   else :
      status = "NOK"

   # start Controller
   ct = Controller.Controller(pwds)
   print("[SERVER] - Status is [" + status + "]")

   # loop until it never ends !
   ct.run_the_magic(pwds)
