"""
Working solution for Problem 1114 but performs terribly, will improve
"""
class Foo(object):
    
    def __init__(self):
        self.firstDone = False
        self.secondDone = False

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstDone = True


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while(self.firstDone is False):
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.secondDone = True
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while(self.firstDone is False or self.secondDone is False):
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

if __name__ == '__main__':
    pr_one = lambda: print("first")
    pr_two = lambda: print("second")
    pr_three = lambda: print("third")
    x = Foo()
    x.first(pr_one)
    x.second(pr_two)
    x.third(pr_three)