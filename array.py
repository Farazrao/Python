from array import*
faraz=array('i',[1,2,3,4,5])
rao=array(faraz.typecode,(a*a for a in faraz))
for i in rao:
    print(i)