words=[]
running = True
while running:
    word = input("enter a word :")
    if word in words :
        print(f"you entered {len(words)-1} unique")
        running=False
    else:
        words.append(word)

    