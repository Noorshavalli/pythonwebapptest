import os,sys
import re
from contextlib import contextmanager

'''
Created on May 1, 2020

@author: NOORSHAVALI
'''


def filefiltercustome(srcfilename):
    count = 0
    prev = ""
    with open("C:/Python27/cucumber/dstfile","w") as dstfileins:
        for line in srcfilename:
            #prev = line
            if prev.lower().find('error:') != -1:
                    count = count+1
                    print("creating {} \n new file {}".format(prev,count))
                    dstfileins = open("C:/Python27/cucumber/dstfile" + str(count), "w")
                    
            if line.startswith('>>>'):
                yield (line,dstfileins)
                
            else:
                pass
        
                
with open("C:/Python27/cucumber/rePatternSearch.txt") as file_handler:
    for block,fp in filefiltercustome(file_handler):
        print(block)
        fp.write(block)
    

'''
@contextmanager
def Timed(dstdir):
    cur = os.getcwd()
    print("Directory name before switching{}".format(cur))
    os.chdir(dstdir)
    
    yield 
    os.chdir(cur)
    

with Timed('C:\Python27\cucumber'): 
    print ("swithed directory",os.getcwd()) 
    print(os.listdir('.'))
    

    
    
if __name__ == '__main__':
    pass

'''