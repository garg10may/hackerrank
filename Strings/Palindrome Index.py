
#https://www.hackerrank.com/challenges/palindrome-index


#rows = int(raw_input())

'''           
def reverse(x):
    return ''.join(reversed(x))

for _ in range(rows):
    s = raw_input()
    if s == reverse(s) or s[1:] == reverse(s[1:]) :
        print -1
    else:
        for i in range(1,len(s)+1):
            new = s[:i-1] + s[i:]
            if new == reverse(new):
                print i-1
                break
'''




rows = int(raw_input())

'''           
def reverse(x):
    return ''.join(reversed(x))

for _ in range(rows):
    s = raw_input()
    if s == reverse(s) or s[1:] == reverse(s[1:]) :
        print -1
    else:
        for i in range(1,len(s)+1):
            new = s[:i-1] + s[i:]
            if new == reverse(new):
                print i-1
                break
'''



for _ in range(rows):
    s = raw_input()
    last = len(s)-1
    for i in range(len(s)/2):
        if s[i] == s[last] :
            status = 1
        else:
            if s[i] == s[last-1] and (s[i+1]==s[last-2]): # what if last is removed, like wise removing the last occuring, and condition is for confirming, bcoz sometimes when I remove last the second last could match but further on it won't match. 
                print last
                status = 0
                break  
            if s[i+1] == s[last]: # what is first is removed, like wise remvoing the first occuring
                print i
                status = 0
                break
        last -= 1
    if status ==1 :
        print -1
        
        