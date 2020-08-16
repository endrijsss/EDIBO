   1: def f(): pass
   2: f()
   3: type (f)
   4: def f(): print("Haļo")
   5: f()
   6:
def g():
    a = 22
    print(a+3)
   7: g(22)
   8:
def g(a):
    print(a+3)
   9: g(22)
  10: g(122)
  11:
def g(a):
    c = a+3
    print(c)
  12: g(123)
  13:
def h():
    a = 11
    b = 22
    c = a + b
    print(c)
  14: h()
  15:
def h(a,b):
    c = a + b
    print(c)
  16: h(11,44)
  17:
def h(a,b):
    c = a - b
    print(c)
  18: h(133,67)
  19:
def h(a,b):
    c = a ** b
    print(c)
  20: h(3,4)
  21:
def h(a,b):
    c = a * b
    print(c)
  22:
def h(a=5,b=8):
    c = a * b
    print(c)
  23:
def h2(a=5,b=8):
    c = a * b
    print(c)
  24: h2()
  25:
def f2(a,b):
    return(a+b)
  26: f2(3,4)
  27: print(f2(3,4))
  28: mkdir python_files
  29: cd python_files/
  30: $ echo Hello > a.dat
  31: cat a.dat
  32: $ echo Hello
  33: echo hello
  34: pwd
  35: f = (open)
  36: f.close90
  37: f = open("a.dat")
  38: f.close()
  39: f = open("a.dat")
  40: f.read()
  41: f.close()
  42: f = open("a.dat")
  43: f.read
  44: f.read()
  45: f.readlines()
  46: f.readlines()
  47: f = open("a.dat")
  48: f.readlines()
  49: f.readlines()
  50: f = open("a.dat")
  51: s = f.readlines()
  52: f.close()
  53: s
  54: s
  55: print(s)
  56: print(s+s)
  57: s[0]
  58: f = open("a.dat")
  59: f.tell
  60: f.tell()
  61: f.tell()
  62: f = open("a.dat")
  63: f.tell()
  64: f.seek()
  65: f = open("a.dat")
  66: f.seek(3)
  67: f.readlines()
  68: f.seek(1)
  69: f.readlines()
  70: %history
  71: %history -g -o -t diary20200813b.py
  72: f = open("a.dat","w")
  73: f.write("EDIBO")
  74: f.close
  75: f.close()
  76: f = open("a.dat","w")
  77: f.write("EDIBO\n")
  78: f.close()
  79: f.closed
  80: f = open("a.dat","w")
  81: f.closed
  82: f.write("\n\n\tEDIBO\n")
  83: f.close()
  84: f = open("a.dat","a")
  85: f.write("\n 2020 \n")
  86: f.close()
  87: %history -g -f history20200813ip.py
