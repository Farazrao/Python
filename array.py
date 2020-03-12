from array import*
faraz=array('i',[10,20,30,40,50])
rao=array(faraz.typecode,(a*a for a in faraz))
for e in rao:
    print(e)