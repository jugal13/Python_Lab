def Initials(name):
	s=name.split()
	f=[]
	for i in s:
		f.append(i[0])
	return "".join(f)
name=input("Enter full name: ")
print("Initials are: "+Initials(name))