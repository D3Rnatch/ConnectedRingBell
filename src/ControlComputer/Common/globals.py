from abc import ABC, abstractmethod


# System Preferences
SYSTEM_PREF_PATH = "/opt/ringbell"
SYSTEM_PREF = SYSTEM_PREF_PATH + "/systempref"

# Comment block definition
COMMENT = '#'

# print 
def printerror(p) :
    print("[ERROR] - " + p)

def printdebug(p) :
    print("[DEBUG] - " + p)

# logging system
# WIP

# @class AbstractData For network classes message abstraction 
class AbstractData(ABC) :
   @abstractmethod
   def dataToFrame(self) :
      pass
   @abstractmethod
   def frameToData(self) :
      pass
