words=[]
f=open("english-words.txt")
for word in f:
    word=word.replace("\n","")
    words.append(word)
f.close()
valid_words=[]

def check(buffer,letters):
    for letter in letters:
        word=buffer+letter
        if (word.lower() in words):
            valid_words.append(word)
            
def fill_buffer(buffer,letters):
    for letter in letters:
        new_buffer=buffer+letter
        new_letters=letters.replace(letter,'')
        check(new_buffer,new_letters)

fill_buffer('',input())
print(valid_words)
        
