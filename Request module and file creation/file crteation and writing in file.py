# this part should be done in terminal 
# Created a file using open() function. inside open i gave the name of the file and a w .
fp = open("tst.txt",'w')# W here means write method which means we can write in this file 
fp.write("This file was created using Python!")
fp.close()

# fp is is an Object of TextIOWrapper class of _io module
print(type(fp))