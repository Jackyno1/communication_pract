#確認檔案
def check(filename):
	import os
	if os.path.isfile('input.txt'):
		print('yeah~找到檔案了')
	else:
		print('沒有檔案')

#打開檔案
def disclose(filename):
	string = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for word in f:
			word = word.strip()
			string.append(word)
	return string

#Convert
def convert(string):
	file = []
	for line in string:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		file.append(person + ': ' + line)
	string = file
	return string

#寫入
def write(products, string):
	with open(products, 'w', encoding = 'utf-8') as output:
		for item in string:
			output.write(item + '\n')
	return output

#執行
def main():
	check('input.txt')
	string = disclose('input.txt')
	string = convert(string)
	write('output.txt', string)

main()