lines=[]
allen_W_C = 0
viki_W_C = 0
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())
for line in lines:
	s = line.split(' ')
	if 'Allen' in s[0]:
		name = 'Allen'
		for allen in s[1:]:
			allen_W_C += len(allen)
	elif 'Viki' in s[0]:
		name = 'Viki'
		for viki in s[1:]:
			viki_W_C += len(viki)
print('Allen wording :', allen_W_C)
print('Viki wording :', viki_W_C)



