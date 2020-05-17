import sys
import numpy as np

def isBitString(input): 
	for i in input:
		if i!="1" and i!="0":
			return False;
	return True;

def parity(data):
	count=0
	for i in data:
		if i=="1":
			count+=1
	if count%2==0:
		return "0"
	else:
		return "1"
	
def hamming_check(data):
	
	if not isBitString(data):
		print("Not a bit string")
		return
	
	size=len(data)
	cbit=0
	while 2**cbit-1<size:
		cbit+=1
	ham=list(data)
	list.reverse(ham)
	err=""
	for i in range(cbit):
		check=[]
		for j in range(2**i):
			check.extend(ham[2**i+j-1::2**(i+1)])
		check="".join(check)
		if parity(check)=="1":
			err="1"+err
		else:
			err="0"+err
	list.reverse(ham)
	print("Recieved data: "+"".join(ham))
	error=int(err,2)
	if error==0:
		print("No error bit")
	else:
		print("Error bit: "+str(error)+" (from the left)")
	list.reverse(ham)
	
if __name__=="__main__":
	hamming_check(sys.argv[1])
	
