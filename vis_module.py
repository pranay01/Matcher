''' Given a height matrix, and the location of the two base stations
    find for each cell in the matrix whether it is visible or not, so 
    that we can exclude it form our path if not visible'''

#value_matrix=[[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[9,9,9,9,9,9,9,2],[2,2,2,2,2,2,2,2]]
value_matrix=[[5,5,5,5,1,5,5,5,5,5,5,5],[5,5,5,5,1,5,5,5,5,5,5,5],[5,5,5,5,9,5,5,5,5,5,5,5],[5,9,1,5,5,5,5,5,5,5,5,5],[5,5,9,5,5,5,5,5,5,5,5,5],[5,5,9,5,5,5,5,5,5,5,5,5]]
r=6
c=12

r1=6
c1=1
r2=3
c2=12
#print value_matrix    

	
vis_matrix = [[0 for i in range(c)] for j in range(r)]
for row in range(0,r):
    for col in range(0,c):
        if ((row==r1-1 and col==c1-1) or (row==r2-1 and col==c2-1)):
            vis_matrix[row][col]=1
        else:
            IsBase1vis = True
            IsBase2vis = True
            if (col>(c1-1)):
                lx=c1-1
                ux=col
            else:
                lx=col
                ux=c1-1
   #         print lx,ux
            for x in range(lx+1,ux+1):
                y=((float(r1-1-row)/(c1-1-col))*(x-(col+0.5)))+row+0.5
			    #the y value obtained should be +ve, otherwise int doesnt work
			    #as expected
                z=(float(x-col)/(c1-1-col))*(value_matrix[r1-1][c1-1]-value_matrix[row][col])+value_matrix[row][col]+0.5
                print x,y,z
                if value_matrix[int(y)][x-1]>z:
                    IsBase1vis = False
                    print 'obstruction1'
                    break #this break should break us out of the nearest for loop..

		#checking for BS2	
            if col>c2-1:
                lx=c2-1
                ux=col
            else:
                lx=col
                ux=c2-1
            for x in range(lx+1,ux+1):
                y=((float(r2-1-row)/(c2-1-col))*(x-(col+0.5)))+row+0.5
                z=(float(x-col)/(c2-1-col))*(value_matrix[r2-1][c2-1]-value_matrix[row][col])+value_matrix[row][col]+0.5
                if value_matrix[int(y)][x-1]>z:
                    IsBase2vis = False
                    print 'obstruction2'
                    break
            if(IsBase1vis or IsBase2vis):
                vis_matrix[row][col]=1

print vis_matrix
			

''' Now use some DP based mathod, with some cells blocked'''
#initialise the matrix with 500
# 500 as max number of rows and cols 200,200

cost_matrix = [[500 for i in range(c)] for j in range(r)]
is_scanned= [[0 for i in range(c)] for j in range(r)] #store  the tuple from which it is possible to come here
cur_row = r1-1
cur_col = c1-1

cost_matrix[cur_row][cur_col]=0;
to_scan_list=[]
to_scan_list.append((cur_row,cur_col))
#how to efficiently scan the matrix?BFS/DFS
while(len(to_scan_list)!=0):
    (cur_row,cur_col)=to_scan_list.pop()
    is_scanned[cur_row][cur_col]=1
    for (inc_row,inc_col) in [(-1,0),(1,0),(0,-1),(0,1)]:
        if (0<=(cur_row+inc_row)<r and 0<=(cur_col+inc_col)<c and vis_matrix[cur_row+inc_row][cur_col+inc_col]==1 and is_scanned[cur_row+inc_row][cur_col+inc_col]==0):
            if(-3<=value_matrix[cur_row+inc_row][cur_col+inc_col]-value_matrix[cur_row][cur_col]<=1):
                t=[]
                for (m,n) in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if (0<=(cur_row+inc_row+m)<r and 0<=(cur_col+inc_col+n)<c):
                        t.append(cost_matrix[cur_row+inc_row+m][cur_col+inc_col+n])

                cost_matrix[cur_row+inc_row][cur_col+inc_col]=min(t)+1
                to_scan_list.append((cur_row+inc_row,cur_col+inc_col))
#                print to_scan_list

#print cost_matrix
print cost_matrix[r2-1][c2-1]


