
myfile='sample.txt'

try:
    f=open(myfile,'r')
    Read_all=f.readlines()
    f.close()
    i=0
    print("Reading file content:")
    for x in Read_all:
        i+=1
        print('line',i,":",x)

except FileNotFoundError:
    print('Error: The file',myfile,'was not found.')


