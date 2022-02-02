flag=True
while(flag==True):
    
 word=input('Enter Word:').lower()
 if len(word)<8:
     print("Word Too Small Try Again ")
 else:
     flag=False

ch=[]
c=word.count(word[0])
for i in word:
    if word.count(i)>c:
        c=word.count(i)
        ch.append(i)
for i in word:
        if word.count(i)==c and i not in ch:
           ch.append(i)
print("Most Occurred Characters:",ch)
choice=input("Enter Your Choice: ").lower()
if choice== word[0] or choice== word[1] or choice== word[4] or choice== word[6] or choice== word[8]:
    print('Congratulations You Won!!!')
else:
    print("Better Luck Next Time!!")
