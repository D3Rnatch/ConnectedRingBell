

import SystemLoader

if __name__ == "__main__" :
 sl = SystemLoader.SystemLoader()
 li = sl.loadPwd()

 if len(li) != 0 : 
   print ("ok")

