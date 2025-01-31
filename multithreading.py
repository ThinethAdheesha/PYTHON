import  threading
from time  import sleep
def  func1():
    for i  in range(100):
         print("good")
         sleep(1)



def func2():
    for  i  in range(100):
         print("bye")
         sleep(1)    
         
t1 =threading.Thread(target=func1)
t2=threading.Thread(target=func2)
t1.start()
sleep(1)
t2.start()








