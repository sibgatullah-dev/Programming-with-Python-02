lines = ["this is the first line","this is the second line","this is the third line","this is the forth line","this is the fifth line"]
# creating the file and writing in it
with open("file.txt","w") as f:
    for line in lines:
        f.write(line+'\n')
        
# reading the content of the file 
with open("file.txt","r") as f:
    print(f.read())