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
	
def hamming_gen(data):
	
	if not isBitString(data):
		print("Not a bit string")
		return
	
	size=len(data)
	cbit=0
	while 2**cbit-cbit-1<size:
		cbit+=1
	ham=list(data)
	list.reverse(ham)
	for i in range(cbit):
		ham.insert(2**i-1,'0')
	for i in range(cbit):
		check=[]
		for j in range(2**i):
			check.extend(ham[2**i+j-1::2**(i+1)])
		check="".join(check)
		ham[2**i-1]=parity(check)
	list.reverse(ham)
	print("Hamming code: "+"".join(ham))
if __name__=="__main__":
	hamming_gen(sys.argv[1])
	

		

	