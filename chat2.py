
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker = 0
	viki_sticker = 0
	allen_image = 0
	viki_image = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker += 1
			elif s[2] == '圖片':
				allen_image += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker += 1
			elif s[2] == '圖片':
				viki_image += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print('allen說了', allen_word_count)
	print('allen傳了', allen_sticker, '個貼圖')
	print('allen傳了', allen_image, '個圖片')

	print('viki說了', viki_word_count)
	print('viki傳了', viki_sticker, '個貼圖')
	print('viki傳了', viki_image, '個圖片')
		# print(s)


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines) #有覆蓋的感覺
	# write_file('output.txt', lines)


main()