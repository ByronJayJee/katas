def triangle(n):
    if(n<1):
        return []

    p_arr=[]
    p_arrl=0
    for x in range(1,n+1):
        p_arrl += x
        for y in range(0,x):
            out=0
            if(y==0 or y==(x-1)):
                out=1
            else:
                coor=p_arrl - (2*x) + y + 1
                out = p_arr[coor-1] + p_arr[coor]
            p_arr.append(out)
    return(p_arr)

print( triangle(5) )