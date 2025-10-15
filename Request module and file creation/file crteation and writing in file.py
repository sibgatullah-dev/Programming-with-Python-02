# this part should be done in terminal 
# Created a file using open() function. inside open i gave the name of the file and a w .
fp = open("tst.txt",'w')# W here means write method which means we can write in this file 
fp.write("This file was created using Python!")
fp.close()

# fp is is an Object of TextIOWrapper class of _io module
print(type(fp))

with open("tst.txt",'w') as f: # when we open the file second time with w method it will erase previous writings 
    f.write("Hello Python. This is the second time writing \n")
    
with open("tst.txt",'a') as f:# when we open the file with a ( append ) method it appends the next line in the file not erasing anything
    f.write("This is second line written in a(append) method so it didn't over write the previous writing\n ")