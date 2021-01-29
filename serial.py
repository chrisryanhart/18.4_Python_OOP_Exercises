"""Python serial number generator."""
import copy

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    # need to add constructors at the top 
    # update the self.var = 
    # if you set copy in function, it will reset everytime it's run
    # 


    def __init__(self, start=100):
        self.start = start 
        self.copy = copy.copy(start)
    def __repr__(self):
        return f"Serial Gen = {self.start}, copy = {self.copy}"
    def generate(self):
        # copy = copy.copy(self.start)
        self.start += 1
        # can return copy here
        return self.start
    def reset(self):
        self.start = self.copy

# def generate(start=100):
#     # make copy of start?
    # func must know what the start is of the instance
    # must know what value serial is 
    # counter = copy.copy(start)


    
    # if counter == start
    
    # counter = 0


    # need to reset function


