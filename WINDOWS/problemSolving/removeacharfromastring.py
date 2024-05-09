


def removethischar(thephrase,char):
    thecharremoved = ""

    for i in thephrase:
        if i == char:
            continue
        thecharremoved += i

    return thecharremoved

print(removethischar("hola how are you today","o"))
