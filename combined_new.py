import sys

def get_shortest_path():
    line=sys.stdin.readline()
    vals=line.split()

    #print matrix_size_list 

    r=int(vals[0])
    c=int(vals[1])
    value_matrix=[] #empty list
    for i in range(0,r):
	    value_matrix.append([])
	    line_matrix=sys.stdin.readline()
	    col_vals=line_matrix.split()
	    for j in range(0,c):
		    value_matrix[i].append(int(col_vals[j]))

    #print value_matrix

    bs_line=sys.stdin.readline()
    val_bs=bs_line.split()
    r1=int(val_bs[0])
    c1=int(val_bs[1])
    r2=int(val_bs[2])
    c2=int(val_bs[3])
    
    #print r1,c1,r2,c2
    '''first get a matrix of valid locations based on BS visibility 
    criteria'''
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
                for x in range(lx+1,ux+1):
                    y=((float(r1-1-row)/(c1-1-col))*(x-(col+0.5)))+row+0.5
                    if y==int(y):
                        if float(r1-1-row)/(c1-1-col)<0:
                            y=int(y)-1
                        else:
                            y=int(y)
                    else:
                        y=int(y)
			    #the y value obtained should be +ve, otherwise int doesnt work
			    #as expected
                    z=(float(x-col)/(c1-1-col))*(value_matrix[r1-1][c1-1]-value_matrix[row][col])+value_matrix[row][col]+0.5
    #               print x,y
                    if value_matrix[y][x]>z:
                        IsBase1vis = False
#                        print 'obstruction1 at (%d,%d)' % (row,col)
                        break #this break should break us out of the nearest for loop..

                if (IsBase1vis == True):
                    if (row>(r1-1)):
                        ly=r1-1
                        uy=row
                    else:
                        ly=row
                        uy=r1-1
                    for y in range(ly+1,uy+1):
                        x=((float(c1-1-col)/(r1-1-row))*(y-(row+0.5)))+col+0.5
                        if x==int(x):
                            if float(c1-1-col)/(r1-1-row)<0:
                                x=int(x)-1
                            else:
                                x=int(x)
                        else:
                            x=int(x)
			    #the y value obtained should be +ve, otherwise int doesnt work
			    #as expected
                        z=(float(y-row)/(r1-1-row))*(value_matrix[r1-1][c1-1]-value_matrix[row][col])+value_matrix[row][col]+0.5
    #               print x,y
                        if value_matrix[y][x]>z:
                            IsBase1vis = False
 #                           print 'obstruction1 at (%d,%d)' % (row,col)
                            break #this break should break us out of the nearest for loop..


  

		#checking for BS2
                if (IsBase1vis == False):
                    if (col>(c2-1)):
                        lx=c2-1
                        ux=col
                    else:
                        lx=col
                        ux=c2-1
                    for x in range(lx+1,ux+1):
                        y=((float(r2-1-row)/(c2-1-col))*(x-(col+0.5)))+row+0.5
                        if y==int(y):
                            if float(r2-1-row)/(c2-1-col)<0:
                                y=int(y)-1
                            else:
                                y=int(y)
                        else:
                            y=int(y)
			    #the y value obtained should be +ve, otherwise int doesnt work
			    #as expected
                        z=(float(x-col)/(c2-1-col))*(value_matrix[r2-1][c2-1]-value_matrix[row][col])+value_matrix[row][col]+0.5
    #               print x,y
                        if value_matrix[y][x]>z:
                            IsBase2vis = False
  #                          print 'obstruction2 at (%d,%d)' % (row,col)
                            break #this break should break us out of the nearest for loop..

                    if (IsBase2vis == True):
                        if (row>(r2-1)):
                            ly=r2-1
                            uy=row
                        else:
                            ly=row
                            uy=r2-1
                        for y in range(ly+1,uy+1):
                            x=((float(c2-1-col)/(r2-1-row))*(y-(row+0.5)))+col+0.5
                            if x==int(x):
                                if float(c2-1-col)/(r2-1-row)<0:
                                    x=int(x)-1
                                else:
                                    x=int(x)
                            else:
                                x=int(x)
			    #the y value obtained should be +ve, otherwise int doesnt work
			    #as expected
                            z=(float(y-row)/(r2-1-row))*(value_matrix[r2-1][c2-1]-value_matrix[row][col])+value_matrix[row][col]+0.5
    #               print x,y
                            if value_matrix[y][x]>z:
                                IsBase2vis = False
   #                             print 'obstruction2 at (%d,%d)' % (row,col)
                                break #this break should break us out of the nearest for loop..	
           
                        if(IsBase1vis or IsBase2vis):
                            vis_matrix[row][col]=1
                else:
					vis_matrix[row][col]=1
#    print vis_matrix
			

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
#need to implement BFS. The steps taken first should be considered first
    while(len(to_scan_list)!=0):
        #print to_scan_list
        #print cost_matrix
        to_scan_list.reverse()
        (cur_row,cur_col)=to_scan_list.pop()
        to_scan_list.reverse()
        #reverse pop reverse to implement bfs using pop
        t=[]
        for (m,n) in [(-1,0),(1,0),(0,-1),(0,1)]:
            if (0<=(cur_row+m)<r and 0<=(cur_col+n)<c):
                if(-3<=value_matrix[cur_row][cur_col]-value_matrix[cur_row+m][cur_col+n]<=1):  
                    t.append(cost_matrix[cur_row+m][cur_col+n])
        if ((min(t)+1)<cost_matrix[cur_row][cur_col]):
            cost_matrix[cur_row][cur_col]=min(t)+1
        #print cost_matrix 
        is_scanned[cur_row][cur_col]=1
        for (inc_row,inc_col) in [(-1,0),(1,0),(0,-1),(0,1)]:
            if (0<=(cur_row+inc_row)<r and 0<=(cur_col+inc_col)<c and vis_matrix[cur_row+inc_row][cur_col+inc_col]==1 and is_scanned[cur_row+inc_row][cur_col+inc_col]==0):
                if(-3<=value_matrix[cur_row+inc_row][cur_col+inc_col]-value_matrix[cur_row][cur_col]<=1):
                    if (cur_row+inc_row,cur_col+inc_col) not in to_scan_list:
                        to_scan_list.append((cur_row+inc_row,cur_col+inc_col))
    
    #print cost_matrix[r2-1][c2-1]

    return cost_matrix[r2-1][c2-1]

   
def main():
    no_test_case=int(raw_input())
    for i in range(1,no_test_case+1):
        n=get_shortest_path()
        if n<500:
            print 'The shortest path is %d steps long.' % n 
        else:
            print 'Mission impossible!'

if __name__ == "__main__":
	main()



  

	

