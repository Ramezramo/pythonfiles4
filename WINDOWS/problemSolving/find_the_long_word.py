
def longWordFinder(thephrase):
    wordsSeparated = thephrase.split(" ")
    longistword = ""
    for i in wordsSeparated :
        if len(longistword) <= len(i):
            longistword = i


    print(f"longist word is ({longistword})")

        



    # print(wordsSeparated)



longWordFinder("sdjkfshd sjdfhskjdfhsdkj kjsdhfskdcv cvx    cxccldfjh dvzxfsdfs zxczxczfx czxczxcz xczxcdfsd")




