k = 'laptop'

# Введите ваше решение ниже

k = k.upper()
eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JX',
      	10:'QZ'}
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}

ru_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЪЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщыъьэюя'
k_2 = list(k)
if k_2[0] in ru_alphabet:
	N = 0
else:
	N = 1


if N == 1:
	print(sum([k for i in k for k, v in eng.items() if i in v]))
elif N == 0:
	print(sum([k for i in k for k, v in rus.items() if i in v]))
else:
    print('Вы мухлюете и играете не по правилам!')