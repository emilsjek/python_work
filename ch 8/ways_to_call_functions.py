# module
import lifting

onerepma = lifting.estimate_1rm(200, 2)
print(onerepma)


# specific function
from lifting import estimate_1rm

onerepmax = estimate_1rm(200, 3)
print(onerepmax)


# function as alias
from lifting import estimate_1rm as rm

onerep = rm(200, 44)
print(onerep)


# module as alias
import lifting as lft

one = lft.estimate_1rm(200, 5)
print(one)


# all functions in module
from lifting import *

rep = estimate_1rm(200, 6)
print(rep)