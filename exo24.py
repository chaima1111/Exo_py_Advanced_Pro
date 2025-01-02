def anagrams(str1,str2):
    str1=sorted(str1)
    str2=sorted(str2)
    if str1 == str2:
        return True
    else:
        return False

print(anagrams("tame", "mate"))
print(anagrams("tame", "team"))
print(anagrams("tabby", "batty"))
print(anagrams("python", "java"))