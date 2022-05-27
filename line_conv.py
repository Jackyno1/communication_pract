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
    with open(filename, 'r', encoding = 'utf-8-sig') as f: #for utf-8 BOM
        for word in f:
            word = word.strip().split(' ')
            string.append(word)
    return string

#Convert
def convert(string):
    allen_word_count = 0 #計字
    allen_emog_count = 0 #計貼圖
    allen_pict_count = 0 #計圖片
    viki_word_count = 0
    viki_emog_count = 0
    viki_pict_count = 0
    for line in string:
        for m in line:
            if m == 'Allen':
                if line[2] == '貼圖':
                    allen_emog_count += 1
                elif line[2] == '圖片':
                    allen_pict_count += 1
                else:
                    for m in line[2:]:
                        allen_word_count += len(m)
            elif m == 'Viki':
                if line[2] == '貼圖':
                    viki_emog_count += 1
                elif line[2] == '圖片':
                    viki_pict_count += 1
                else:
                    for m in line[2:]:
                        viki_word_count += len(m)
    print('Allen說了', allen_word_count, '個字')
    print('Viki說了', viki_word_count, '個字')
    print('Allen有', allen_emog_count, '個貼圖')
    print('Viki有', viki_emog_count, '個貼圖')
    print('Allen有', allen_pict_count, '個圖片')
    print('Viki有', viki_pict_count, '個圖片')

#寫入
def write(products, result):
    with open(products, 'w', encoding = 'utf-8') as output:
        for item in result:
            output.write(item + '\n')
    return output

#執行
def main():
    check('LINE-Viki.txt')
    string = disclose('LINE-Viki.txt')
    result = convert(string)
#    write('LINE_final.txt', result)

main()