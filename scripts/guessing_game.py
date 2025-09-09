import random
while True:
    a=input('Level: ')
    if a.isnumeric()==False:
        pass
    else:
        if int(a)>0:
            ran_num=random.randint(1,int(a))
            while True:
                guess=int(input('Guess: '))
                if guess<0:
                    pass
                elif ran_num==guess
                print('Just right!')
                    break
                elif ran_num>guess:
                    print('Too small!')
                    break
                else:
                 print('Too large!')
                 break
            break
        else:
            pass




