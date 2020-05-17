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

def parity_gen(data,type,size="2x2"):
	t="";
	data=str(data)
	if len(data)<9 or not isBitString(data):
		print("Not a bit string or k<9")
		return
	
	
	if type ==0 or type == 1:
		count = countOnes(data)
		t="Even" if type==0 else "Odd"
		if count%2==0 and type==0 or count%2==1 and type ==1:
			out=data+"0"
		else:
			out=data+"1"
		print("Input: "+data+"\nCount of 1 = "+str(count)+"\nType: "+ t +"\nOutput: "+out)
	
	elif type ==2 or type ==3:
		s=size.split('x')
		row=int(s[0])
		col=int(s[1])
		if len(data)!=row*col:
			print("Invalid input")
			return
		
		t="2D-Even" if type==2 else "2D-Odd"
		mat = np.array(list(data)).reshape((row,col))
		rows = np.zeros(row)
		cols = np.zeros(col+1)
		
		for x in range(row):
			countrow =0
			for y in range(col):
				if mat[x][y]=="1":
					countrow+=1
				
			if countrow%2==0 and type==2 or countrow%2==1 and type ==3:
				rows[x]="0"
			else:
				rows[x]="1"
		
		last =0
		for y in range(col):
			countcol =0
			for x in range(row):
				if mat[x][y]=="1":
					countcol+=1
			if countcol%2==0 and type==2 or countcol%2==1 and type ==3:
				cols[y]="0"
			else:
				cols[y]="1"
				last+=1
		if last%2==0 and type==2 or last%2==1 and type ==3:
			cols[col]="0"
		else:
			cols[col]="1"
		mat =np.insert(mat,col,rows,axis=1)
		mat =np.insert(mat,row,cols,axis=0)
		print("Input: "+data+"\nType: "+ t +"\nOutput:")
		print(mat)
		for i in mat:
			for j in i:
				print(j,end='')
			print(" ",end='')
	else:
		print("Invalid input")
		return
		

if __name__=="__main__":
	if len(sys.argv)==3:
		parity_gen(sys.argv[1],int(sys.argv[2]))
	elif len(sys.argv)==4:
		parity_gen(sys.argv[1],int(sys.argv[2]),sys.argv[3])
	

		

	