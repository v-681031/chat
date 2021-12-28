#read file
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#convert file
def convert(lines):
	new =[]
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ':' + line)
	return new	

#write file
def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')
# main file
def main():
	lines = read_file('input.txt')
	print(lines)
	new_lines = convert(lines)
	print(new_lines)
	write_file('output20211229.txt', new_lines)


main()