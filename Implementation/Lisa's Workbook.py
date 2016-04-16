#n, k = map(int, raw_input().strip().split(' '))
#problems = map(int, raw_input().strip().split(' '))

n, k = 10,5
problems = (3, 8, 15 ,11 ,14 ,1,9 ,2, 24, 31)

problems_page_wise = []
for i in problems:
	if k<i:
		if (i%k) == 0:
			temp = [k] * (i/k)
			problems_page_wise.extend(temp)
		else:
			temp = [k] * (i/k)
			problems_page_wise.extend(temp)
			problems_page_wise.extend([i%k])
	else:
		problems_page_wise.extend([i])

print problems_page_wise

count = 0
problem_no = 0
for page_no, problems in enumerate(problems_page_wise):
	problem_no += problemsage_no <= problems:
		count +=1

print count 


