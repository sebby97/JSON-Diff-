import json
import sys

output1 = json.load(open(sys.argv[1]))
output2 = json.load(open(sys.argv[2]))


#Not recursiveCheck (yet) trying to figure out how to properly loop through...
def recursiveCheck(output1,output2):
    
    for key in output1.keys():
        if key not in output2:
            print("The attribute --"+line+"--doesn't exist in Output 2")

        if output1[key] != output2[key]:
            print('\nOutput mismatch @ --'+key+'--\nOutput 1: '+str(output1[key])+' Output 2: '+str(output2[key])+'\n')

recursiveCheck(output1,output2)
