#To generate random numbers
from random import random
from random import seed
seed(1)
x=random()
class small(Exception):
    def __init__(self,x):
        self.msg=x
class goodtogo(Exception):
    def __init__(self,x):
        self.msg=x

if x>0.1:
    raise goodtogo('Your number is good to go')
else:
    raise small('Your number is smaller than 0.1')

        