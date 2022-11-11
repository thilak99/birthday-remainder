import sys,os
import splunk.Intersplunk
def matching():
    f = open("birthday.txt","r")
    a=f.readlines()
    f.close()
    return a

a = matching()
splunk.Intersplunk.outputResults([{"result":a}])     
