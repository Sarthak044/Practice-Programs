# from time import sleep


# try:
#   for i in range(0,6):
#       print(i)
#       sleep()
# except KeyboardInterrupt:
#   print("[+] ctrl+C Captured... Exiting")

# def func(arguments):
#         #code

# class first:
#   x = 9
#   a = 13
#   b = 10
#   def __init__(self, c,d):
#       self.c = c
#       self.d = d

# o1 = first("hello", "world")

# print(o1.c)
# print(o1.d)





class Error(Exception):
  
  def __init__(self,a):
      self.a = a
  def __str__(self):
      return repr(self.a)

try:
    raise(Error(2*7))
except Error:
    print('A New Exception occured')