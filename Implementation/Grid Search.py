import sys


t = int(raw_input().strip())
for _ in xrange(t):
    R,C = map(int,raw_input().strip().split(' '))
    G = []
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = map(int,raw_input().strip().split(' '))
    P = []
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
        
print G
print P