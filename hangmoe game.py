import random
print= input("welcome to the game, Hangman")
word=(word.txt)
gusseword=''
print("gusseword ", gusseword) 
availbleletters = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z] 
word = random.choice(letters)
print('Guess the letter')
gusses=''
turns=12
while turns>0:
    failed=0
    for letter in availbleletters:
        if letter in gusses:
            print('letter')
            
            else:
                print('_')
                failed+=1
    if failed==0:
        print('younwin')
        print('the word is:',word)
        break;





