 #!/usr/bin/env python3
from lib.Logger import Logger

class Module:
  def printFib(n):    # write Fibonacci series up to n
    Logger.printStart()
    a, b = 0, 1
    while b < n:
            print(b),
            a, b = b, a+b
    Logger.printOk()
    