def Z(x):
    z=0
    for i in range(1,13):
        z += x/(5**i)
    return(z)

count=int(raw_input())
for i in range(1,count+1):
	inp =int(raw_input())
	print Z(inp)
