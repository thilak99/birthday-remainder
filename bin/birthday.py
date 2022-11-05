import sys,os
import splunk.Intersplunk


def matching():
    s1=sys.argv[1]
    s2=sys.argv[2]
    s3=sys.argv[3]
    s4=sys.argv[4]
    
    f=open("C:\\Program Files\\Splunk\\etc\\apps\\Birthday-Remainder\\birthday.txt","a")
    f.write(str(s1)+":"+str(s2)+":"+str(s3)+":"+str(s4))
    f.write("\n")
    f.close()
    return (str(s1)+":"+str(s2)+":"+str(s3)+":"+str(s4))

    

a = matching()
splunk.Intersplunk.outputResults([{"result":a}]) 
