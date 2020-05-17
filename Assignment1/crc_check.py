import sys

def isBitString(input): 
	for i in input:
		if i!="1" and i!="0":
			return False;
	return True;

def checkZeros(input):
	for i in input:
		if i!="0":
			return False
	return True

def crc_gen(data,div):
	if not isBitString(data):
		print("Not a bit string")
		return
	enc=list(data)
	n=len(div)
	for i in range(n-1):
		enc+='0'
	for i in range(len(data)):
		if enc[i]=='1':
			for j in range(len(div)):
				enc[i+j]='0' if div[j]==enc[i+j] else '1'
				
	crc = "".join(enc[len(enc)-n+1:])
	ans="True" if checkZeros(crc) else "False"
	print("Codeword: "+data+"\nDivider: "+div+"\nRemainder: "+crc+"\nValid: "+ans)
	

if __name__=="__main__":
	crc_gen(sys.argv[1],sys.argv[2])
	

		

	