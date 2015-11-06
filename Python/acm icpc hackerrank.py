#You are given a list of N people who are attending ACM-ICPC World Finals.
#Each of them are either well versed in a topic or they are not.
#Find out the maximum number of topics a 2-person team can know.
#And also find out how many teams can know that maximum number of topics.


n,m = [int(x) for x in raw_input().split()]
maxi = 0
cnt = 0
inp = [raw_input() for _ in range(n)]
for i in range(0,n):
    for j in range(i+1,n):
        set_bit = bin(int(inp[i],2) | (int(inp[j],2))).count("1")  #bit wise matching of two array and count
        #print set_bit
        if set_bit>maxi:
            maxi = set_bit
            cnt = 1
        elif set_bit == maxi:
            cnt+=1
print maxi
print cnt
