myfile='output.txt'
myinput=input("Enter text to write in the file:")
try:
    f=open(myfile,'w')
    outputWrite=f.write(myinput)
    f.close()
    if outputWrite>0:
        print("Data successfully written to",myfile,"\n")


    secondInput=input("Enter additional text to append:")
    f=open(myfile,'a')
    secondOutputWrite=f.write('\n'+secondInput)
    f.close()
    if secondOutputWrite>0:
        print("Data successfully appended."+"\n")


    f=open(myfile,'r')
    reading_Text=f.read()
    f.close()
    print("Final content of",myfile)
    print(reading_Text)

except (IOError, OSError) as e:
    print("An error occurred while handling the file:", e)
