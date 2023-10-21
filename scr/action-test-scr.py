import sys
import os

args = sys.argv[1:]

lenargs = len(args)
aaa = args[0]

print(aaa)

f = open("action-wrfile.txt", "a")
f.write(aaa)
f.close()

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)