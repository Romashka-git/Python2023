d = dict()
d = {'q': 'qwerty'}
d['up'] = '↑'
print(d)
d['down'] = '↓'
print(d)

for i in d:
    print(i)
    print(f'{i} {d[i]}')

for k, v in d.items():
    print(k, v)

print(d.items())
print(type(d.items()))