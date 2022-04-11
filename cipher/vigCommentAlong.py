def encrypt(message,key):
    #empty string that will be filled with the encrypted       message
    encrypted=""
    #make all lowercase letters into uppercase
    message = message.upper()
    key = key.upper()
  #while loop to iterate thgouh my plaintext
    i = 0
    while (i<len(message)):
        #key needs a separate index, used to loop back to         beginning of the key
        iKey = i%len(key)

        #plain textconverting a char into integer,                shifted by 65 to ensure A is 0
        p = ord(message[i])-65 
        
      #key converting a char into integer,                     shifted by 65 to ensure A is 0
        d = ord(key[iKey])-65

        #p+d: doing shift
        #%26: loops back to front of alphabet
        #+65: undoing shift
        #chr: converts unicode into char
        c = chr(((p+d)%26)+65)

        #concatonate to our empty string that we are             building along
        encrypted+=c
        i+=1
    return encrypted

m = "ciphers are cool"
k = "vigenere"

print(m)
print(encrypt(m,k))