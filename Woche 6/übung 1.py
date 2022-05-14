def dec_to_bin_rec(n):
    if n==0:
        return(str(0))
    else:
        return((dec_to_bin_rec(n//2)+str(n%2)))

print(dec_to_bin_rec(10))
print(dec_to_bin_rec(1))

def dec_to_bin_rec2(n):
    if n==0:
        return(str(0))
    elif int(n)==0:
        return("")
    else:
        return((dec_to_bin_rec2(str(int(n)//2))+str(int(n)%2)))

print(dec_to_bin_rec2(10))
print(dec_to_bin_rec2(1))