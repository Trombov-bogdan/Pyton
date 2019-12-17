print("Ener name of file or adress!")
file_name = input()
sourceFile = open(file_name, 'r')
print("Our numbers :")
lis = [line.rstrip('\n') for line in sourceFile]
print(lis)
a = [int(number) for number in lis]
print(a)
sourceFile.close()
b = 1
for x in a:
    b *= x
print(b)