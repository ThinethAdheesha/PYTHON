class Python:
    __x = 10  # private variable

    def private(self):
        print("Hello Thineth")
        self.__method2()

    def __method2(self):  # private method
        print("Hi, I'm in a private method")


# Create an object of the class
myobj = Python()
myobj.private()
