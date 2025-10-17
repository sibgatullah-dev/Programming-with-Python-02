with open("tst.txt","r") as tst: # using the "r" reading mode to read the content of the file 
    print(tst.read())
    
# using with as to open and close a file is called context manager