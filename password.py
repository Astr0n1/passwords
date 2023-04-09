def encoding():
    phrase=input("Enter the Phrase to encode : ")
    encoded=list("Astr0n1_")
    
    for i in range (len(phrase)) :
        shift=(pow(i+1,i))%26
        if (phrase[i].isalpha()):
            if(ord(phrase[i])+shift >ord('z')):
                shift-=26
            encoded.append(chr(ord(phrase[i])+shift)) 
        else :
            encoded.append(phrase[i])
    print ("#"*50+"\n\t" + "".join(encoded) + "\n"+"#"*50)

def decoding():
    phrase=input("Enter the Phrase to decode : ")
    phrase=phrase[8:]
    print(phrase)
    decoded=[]
    
    for i in range (len(phrase)) :
        shift=(pow(i+1,i))%26
        if (phrase[i].isalpha()):
            if(ord(phrase[i])-shift <ord('a')):
                shift-=26
            decoded.append(chr(ord(phrase[i])-shift))
        else :
            decoded.append(phrase[i])
    print ("#"*50+"\n\t Astr0n1_ + " + ''.join(decoded) + "\n"+"#"*50)


while(True):
    process=input("Select ( encode / decode / exit) : ")
    
    if(process=="encode" or  process=='e'):
        encoding()
    elif (process=="decode" or process=='d'):
        decoding()
    elif (process=='exit' or process=='x'):
        break
    else : 
        print("#"*70+"\nSelect only from ( encode / decode /exit) the selection is case sensitive\n"+"#"*70+"\n")
