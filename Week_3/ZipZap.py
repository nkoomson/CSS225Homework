#ZipZap
#Nelson Koomson
#2/10/21

#This function prints "if", "elif", and "else" statements
def ZipZap(n):
    if n%5 == 0 and n%7 == 0:
        print("ZipZap")
    elif n%5 == 0:
        print("Zip")
    elif n%7 == 0:
        print("Zap")
    else:
        print(n)

ZipZap(5)
ZipZap(14)
ZipZap(35)
ZipZap(2)
ZipZap(105)
