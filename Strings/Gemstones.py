'''
John has discovered various rocks. Each rock is composed of various elements, and each element is represented by a lower-case Latin letter from 'a' to 'z'. An element can be present multiple times in a rock. An element is called a gem-element if it occurs at least once in each of the rocks.

Given the list of NN rocks with their compositions, display the number of gem-elements that exist in those rocks.

Input Format

The first line consists of an integer, NN, the number of rocks. 
Each of the next NN lines contains a rock's composition. Each composition consists of lower-case letters of English alphabet.

Constraints 
1≤N≤1001≤N≤100 
Each composition consists of only lower-case Latin letters ('a'-'z'). 
1≤1≤ length of each composition ≤100≤100
Output Format

Print the number of gem-elements that are common in these rocks. If there are none, print 0.

Sample Input

3
abcdde
baccd
eeabg
Sample Output

2
'''

rows = int(raw_input())

result = set('abcdefghijklmnopqrstuvwxyz')
for _ in range(rows):
    line = set(raw_input())
    result = result & set(line)

print len(result) 