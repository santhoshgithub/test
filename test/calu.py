import sys
for i in range(100):
 a=int(raw_input("Enter first number:"))
 b=int(raw_input("Enter second number:"))
 c = int(raw_input("Enter 1 for add, 2 for sub:"))
 try:
    int(a)
    int(b)
   # print "Addition of",a+b
   #print "Division of two numbers",a/b
   # print "Substraction of two numbers",a-b
 except ValueError:
    try:
        float(a)
        float(b)
    except ValueError:
        print "Enter Integers only"
 if c==1:
   print a+b
 elif c==2:
   print a-b
 elif c==0:
   sys.exit()
 else :
   print "You entered wrong number"
   #print input()
  #i=int(raw_input("Enter 100 to exit :"))
 #if i==100:
  #  return false
   #else:
    #return true
