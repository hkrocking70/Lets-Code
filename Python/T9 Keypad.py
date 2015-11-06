
'''In the pre-smartphone era, most mobile phones with numeric keypads had a private dictionary of words to allow users to type messages quicker. On a typical phone of this type, each number key is assigned a subset of the alphabet {a,b,…,z}: 2 is assigned the subset {a,b,c}, 3 is assigned {d,e,f}, 4 is assigned {g,h,i}, 5 is assigned {j,k,l}, 6 is assigned {m,n,o}, 7 is assigned {p,q,r,s}, 8 is assigned {t,u,v} and 9 is assigned {w,x,y,z}.

When the user types a sequence of numbers, this sequence is mapped to all possible words that can be constructed from the key assignment. For instance, if the user types 66, this could correspond to any one of the letter sequences "mm", "mn", "mo", "nm", "nn", "no", "om", "on" or "oo". These letter sequences are looked up in the dictionary stored in the phone and all matches are reported. For instance, if the phone's dictionary contains only "on" and "no" from this set of sequences, the user will be offered a choice of "on" or "no" to insert in the message. Similarly, the input 4663 might be interpreted as either "good" or "home". An input sequence may have a unique interpretation---for example, the only word in the dictionary matching the input 28 may be "at". Other sequences may not match any word in the dictionary—for instance, 99999.

Your task is the following. Given the typical assignment from number keys to letters of the alphabet given above and given a dictionary of words, report the input sequence that matches the largest number of words in the dictionary. For example, if the dictionary consists of the words {at,on,good,no} then the answer is 66, because 66 matches both "on" and "no" while no other input matches more than one word in the dictionary. On the other hand, with the dictionary {at,on,good,no,home,gone}, the answer is 4663, because 4663 matches three words, "good", "home" and "gone" in the dictionary.'''

from collections import Counter
d_dict={2:{'a','b','c'},
	3: {'d','e','f'},
	4:{'g','h','i'},
	5:{'j','k','l'},
	6:{'m','n','o'},
	7:{'p','q','r','s'},
	8:{'t','u','v'},
	9:{'w','x','y','z'}}

t=input()
inp = [raw_input() for _ in range(t)]
temp=[]
res=[]
j=0
for i in range(0,len(inp)):
    r=0
    for j in range(0,len(inp[i])):
        for k in range(2,10):
            if inp[i][j] in d_dict[k]:
                res.append(k)
    res=''.join(map(str,res))
    temp.append(res)
    res=[]
    t=t-1
count = Counter(temp)
count=count.most_common()
print count[0][0]

