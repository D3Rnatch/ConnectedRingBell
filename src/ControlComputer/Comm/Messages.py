import os, sys, struct

sys.path.insert(0, os.environ('commonPath'))

import globals

# @class StatusMessageData : implementation of received Status Message
class StatusMessageData(globals.AbstractData) :

   # Internal data declaration
   __ArduinoInternStatus = 0
   __ArduinoExternStatus = 0
   __CanBusStatus        = 0

   # @brief dataToFrame transform inner data to proper frame structure
   # Does only perform transformation for data segment of frame
   def dataToFrame(self):
     printdebug("don't call this function this is a received data frame")

   # @brief frameToData transform given frame to inner data
   # @input dataFrame : only data segment of network frame is given here
   def frameToData(dataFrame):
     index = 0
     # check data length (little endian)
     tmp = dataFrame[1]
     tmp <<= 2
     tmp += dataFrame[0]
     dataLength = struct.unpack('<H', tmp)

     if dataLength != 3 :
        printerror("received frame is of size=" + dataLength + "instead of 3")
        return False

     index = index + 2

     # internalStatus
     __ArduinoInternStatus = struct.unpack('<H', dataFrame[index])
     index = index + 1

     # externalStatus
     __ArduinoExternStatus = struct.unpack('<H', dataFrame[index])
     index = index + 1

     # bus status
     __CanBusStatus = struct.unpack('<H', dataFrame[index])
     
     printdebug("+++ inputFrame=[" + dataFrame  + "], internStatus=" + self.__ArduinoInternStatus + ", externStatus=" + self.__ArduinoExternalStatus + ", busCanStatus=" + __CanBusStatus)

     return True

   # @brief returns externalArduinoStatus
   def getExternalArduinoStatus(self) :
      return self.__ArduinoExternStatus

   # @brief returns internalArduinoStatus
   def getInternalArduinoStatus(self):
      return self.__ArduinoInternalStatus

   # @brief return CanBus Status
   def getCanBusStatus(self):
      return self.__CanBusStatus



