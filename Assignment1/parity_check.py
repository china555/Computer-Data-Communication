import sys
import numpy as np

def isBitString(input): 
	for i in input:
		if i!="1" and i!="0":
			return False;
	return True;

def countOnes(data):
	count=0
	for i in data:
		if i=="1":
			count+=1
	return count

def checkLinear(data,type):
	count = countOnes(data)
	if count%2==0 and type==0 or count%2==1 and type ==1 or count%2==0 and type==2 or count%2==1 and type ==3 :
		return True
	else:
		return False
def parity_check(data,type,size="2x2"):
	t="";
	data=str(data)
	if not isBitString(data):
		print("Not a bit string")
		return
	
	if type ==0 or type == 1:
		send=data[0:len(data)-1]
		bit=data[len(data)-1]
		t="Even" if type==0 else "Odd"
		ans = checkLinear(data,type)
		print("Type: "+ t+"\nValid: "+str(ans))
	
	elif type ==2 or type ==3:
		s=size.split('x')
		row=int(s[0])+1
		col=int(s[1])+1
		if len(data)!=row*col:
			print("Invalid input")
			return
		
		t="2D-Even" if type==2 else "2D-Odd"
		ans="True"
		for x in range(row):
			if not checkLinear(data[x*col:x*col+col],type):
				ans="False"
				break
		for x in range(col):
			if not checkLinear(data[x::col],type):
				ans="False"
				break
		print("Type: "+t+"\nValid: "+ans)
	else:
		print("Invalid input")
		return
		

if __name__=="__main__":
	if len(sys.argv)==3:
		parity_check(sys.argv[1],int(sys.argv[2]))
	elif len(sys.argv)==4:
		parity_check(sys.argv[1],int(sys.argv[2]),sys.argv[3])
	

		

	