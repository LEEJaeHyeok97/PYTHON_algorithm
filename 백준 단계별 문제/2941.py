croatiaAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str = input()

for i in croatiaAlphabet:
    str = str.replace(i, '*')

print(len(str))