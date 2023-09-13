colors = ['red ', 'yellow ', 'green ']

# data = open('file.txt', 'w')
# data.writelines(colors)
# data.close()

#--------------------------------------------

# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('colors \n')
#     data.write(f'{colors} \n')
#     data.writelines(f'{colors} \n')

#--------------------------------------------

path = 'file.txt'
data = open(path, 'r')
for i in data:
    print(i)
data.close()
