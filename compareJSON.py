import json
import sys

def recursiveCheck(output1,output2):
    for line in output1:

        if line not in output1:
            print("The attribute --"+line+"--doesn't exist in Output 1")
        if line not in output2:
            print("The attribute --"+line+"--doesn't exist in Output 2")

        if output1[line] != output2[line]:
            output1[line]
            output2[line]
            difference = 'Output mismatch @ --'+line+'--\nOutput 1: '+str(output1[line])+' Output 2: '+str(output2[line])+'\n'
            print(difference)

output1 = json.load(open(sys.argv[1]))
output2 = json.load(open(sys.argv[2]))

recursiveCheck(output1,output2)
