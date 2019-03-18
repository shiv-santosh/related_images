import os
file=open("cars1_front",'r')
for line in file:
        l=line.split()
        os.system("wget -O {0}.jpg {1}".format(l[0],l[1]))
