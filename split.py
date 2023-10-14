import MeCab
import markovify
import inspect

import unidic_lite

print(inspect.getfile(unidic_lite))

debug = False

input = open('./tweets','r',encoding='utf-8')
output = open('./splitted.txt','w',encoding='utf-8')

mecab = MeCab.Tagger("-Owakati")

for line in input.read().split('\n'):
    splittedLine = ' '.join(mecab.parse(line).split())
    output.write(splittedLine)
    output.write('\n')

input.close()
output.close()

