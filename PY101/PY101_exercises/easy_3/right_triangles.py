def triangles(num):  #takes pos int n
    for idx in range(1,num+1):
        print(" "*(num-idx)+('*'*idx))
    

triangles(5)