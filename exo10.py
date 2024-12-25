word = input("enter a word : ")

def is_pala(word):
    i=0
    while i <round(len(word)/2):
        if word[i]!=word[-(i+1)]:
            return False
        i+=1
    return True
if is_pala(word) :
    print("Yes, it's a palindrome.")
else :
    print("No, it's not a palindrome.")