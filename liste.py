prenume = ['Mihai', 'George', 'Ana', 'Dan', 'Ion', 'Geta', 'Vio'] 
varsta = [14, 23, 15, 14, 12, 41, 39]
print(prenume)
print(varsta)
for i in range(0, len(prenume)):
    print(prenume[i], 'are varsta de', varsta[i], 'ani')
    i+=1
prenume.extend(['Andreea', 'Ioan'])
print(prenume)
varsta.extend(['34', '23'])
print(varsta)
del prenume [2:3]
print(prenume)
del varsta [2:3]
print(varsta)
prenume.insert(2, 'Ana')
l1 = prenume[0:3]
print(l1)