'''
https://www.hackerrank.com/challenges/funny-string
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
rows = int(raw_input())


for _ in range(rows):
    line = raw_input()
    line2 = line[::-1]
    l = len(line)
    for i in range(len(line)-1):        
        if abs( ord(line[i+1]) - ord(line[i]) ) == abs( ord(line2[i+1]) - ord(line2[i]) ):
            status =1 
        else:
            status = 0
            break
    if status ==1:
        print 'Funny'
    else:
        print 'Not Funny'


