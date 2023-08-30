# a = [1, 2, 3, 4, 5]
# b = [2, 4, 6, 8]
# print(b.count(1))
# print(len(b))

import re
fh = open('elaleph_cuentos.txt')
libro = []
for line in fh:
    # nombres = re.findall('[A-Z][a-z]+', line)
    nombres = re.findall('[a-z] [A-Z][a-z]+', line)
    if nombres != []:
        i = 0
        for i in range(len(nombres)):
            x, n = nombres[i].split(' ')
            if libro.count(n) == 0:
                libro.append(n)
        # libro += nombres
print(f'Patrones encontrados: {len(libro)}\nPrimeros 20:\n')
for i in range(20):
    print(libro[i])
