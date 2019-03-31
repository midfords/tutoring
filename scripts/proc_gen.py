

file = open('practice.txt', 'r')
lines = file.readlines()
file = open('practice2.txt', 'w+')
for line in lines:
	if len(line) > 2:
		line = line.replace('\n', '')
		line = line.replace(':', '')
		line = line.strip()
		file.write('print(\'' + line + '\')\n')
		file.write('if ' + line + ':\n\tprint(\'\\n\\tTrue\\n\')\nelse:\n\tprint(\'\\n\\tFalse\\n\')\n')