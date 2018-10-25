class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def push(self,val):
         self.stack.append(val)
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    def size(self):
        return self.stack.__len__()
    def is_empty(self):
        return self.size() == 0

class BrowserHistory:
    def __init__(self):
        self.backH = Stack()
        self.fwdH = Stack()
        self.__current = ""

    def open(self, url):
        if self.__current != "":
            self.backH.push(self.__current)
            self.fwdH = Stack()
        self.__current = url

    def back(self):
        if self.backH.is_empty():
            print ("No History")
        else:
            self.fwdH.push(self.__current)
            self.__current = self.backH.pop()
    def __get_current__(self):
        return self.__current

def main():
    bh = BrowserHistory()
    bh.open("Vcho")
    bh.open("Youtube")
    bh.open("Facebook")
    print (bh.__get_current__())

main()