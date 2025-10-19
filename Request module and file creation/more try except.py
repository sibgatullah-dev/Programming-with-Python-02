import io

file = "tst.txt"
mode= 'r'

try:
    with open(file,mode) as fp:
        print(fp.read())
except FileNotFoundError:
    print(file,"not found. Please check if the file exists")
except io.UnsupportedOperation:
    print('Are you sure',file,'is readable?')