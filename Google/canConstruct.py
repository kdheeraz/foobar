def canConstruct(s,words):
    print("s is",s)
    if(s==""):
        return True
    if(s==words[0]):
        return True
    subS=s
    for word in words:
        lenL = len(word)
        if(s[0:lenL]==word):
            print("-prefix",s[lenL:])
            if(canConstruct(s[lenL:],words)):
                return True
            
        # if(word == s[-lenL:]):  
        #     print("-suffix",s[-lenL:])
        #     if(canConstruct(s[:-lenL],words)):
        #         return True
    return False


print(canConstruct("kefabc",["ab","c","kef","d"]))
