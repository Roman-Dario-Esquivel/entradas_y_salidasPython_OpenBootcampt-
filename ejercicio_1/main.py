f = open('archivo.txt','w')

f.write('linea 1\n')
f.write('linea 2\n')
f.write('linea 3\n')
f.write('linea 4\n')
f.write('linea 5\n')
f.write('linea 6\n')
f.close
f = open('archivo.txt','r')

print(f.read())
f.close
f = open('archivo.txt','a')
f.write('linea 7\n')
f.write('linea 8\n')
f.write('linea 9\n')
f.write('linea 10\n')
f.write('linea 11\n')
f.write('linea 12\n')
f.close
f = open('archivo.txt','r')

print(f.read())
f.close