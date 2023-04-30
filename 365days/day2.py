#write a program to count character occurences in string
def char_occur(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
word = input("Enter your first string")
char_occur(word)