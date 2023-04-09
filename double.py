def encoding():
    phrase=input("Enter the Phrase to encode : ")
    encoded=[]
    
    for i in range (2*len(phrase)) :
        shift=(pow(i+1,i))%26
        if (phrase[i%len(phrase)].isalpha()):
            if(ord(phrase[i%len(phrase)])+shift >ord('z')):
                shift-=26
            encoded.append(chr(ord(phrase[i%len(phrase)])+shift)) 
        else :
            encoded.append(phrase[i%len(phrase)])
    print ("#"*50+"\n\t" + "".join(encoded) + "\n"+"#"*50)

def decoding():
    phrase=input("Enter the Phrase to decode : ")
    decoded=[]
    
    for i in range (len(phrase)//2) :
        shift=(pow(i+1,i))%26
        if (phrase[i].isalpha()):
            if(ord(phrase[i])-shift <ord('a')):
                shift-=26
            decoded.append(chr(ord(phrase[i])-shift))
        else :
            decoded.append(phrase[i])
    print ("#"*50+"\n\t" + ''.join(decoded) + "\n"+"#"*50)


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
