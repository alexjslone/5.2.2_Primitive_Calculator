filledList = []
operations= [1, 2, 3]
def compute_operations(n):
    for i in range(0, n+1): 
        filledList.append(float('inf'))
    #this creates a list with the min operations for each number
    for v in range(0,n+1):
        for o in operations:
            if v == 0: 
                filledList[v]=0
            elif v==2: 
                filledList[v]=1
            elif v==3:
                filledList[v]=1
            elif v%o== 0 and filledList[int(v/2)]+1<= filledList[v]: 
                filledList[v]=filledList[int(v/2)]+1 
            elif v%o==0 and filledList[int(v/3)]+1<= filledList[v]:
                filledList[v]= filledList[int(v/3)]+1
            else: 
                filledList[v] = filledList[v-1]+1
    return[filledList[n]]
    
n= 96234
print(compute_operations(n))
   
 

"""
if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
"""