#Least Recently Used
import time
def lru(l):
    start_time = time.time()
    print len(l)
    frame=[-1]*3
    co=[0]*3
    count=-1
    for i in range(len(l)):
        if l[i] not in frame:
            mi=min(co)
            for j in range(len(co)):
                if co[j]==mi:
                    pos=j
                    break
            frame[pos]=l[i]
            co[pos]=i+1
        else:
            for j in range(len(frame)):
                if frame[j]==l[i]:
                    pos=j
                    break
            co[pos]=i+1
    print frame
    print("--- %s seconds ---" % (time.time() - start_time))

#Just for testing
lru([2,3,2,1,5,2,4,5,3,2,5,2])
