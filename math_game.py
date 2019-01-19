from random import randint
def main():
    Right = 0
    Wrong = 0
    print('WELCOME TO MATH GAME VER 1.0, BY NG9526')
    print('CREDITS:NG9526 FOR EVERYTHING')
    print('CONTACTS:NG9526 @ ng.9526@yes.my')
    print('TUTORIALS:THIS GAME HAD 20 QUESTIONS, ANSWER ALL QUESTIONS')
    for i in range(1, 21):
        print('QUESTION ', i)
        NumA = randint(0, 10)
        NumB = randint(0, 10)
        Ans = NumA + NumB
        print('Problem', i, ':', NumA, '+', NumB)
        PlayerAns = int(input('Answer:'))
        if PlayerAns == Ans:
            print('You are very fantaaaaaaaaaaaaaaaaaaaaastic!')
            Right += 1
        else:
            print('I heard every door you open')
            Wrong += 1
    print('\n')
    print('THE GAME ENDED')
    print('You had', Right, 'question(s) done right,', Wrong, 'question(s) done wrong')
             


if __name__ == '__main__':
    main()

    
