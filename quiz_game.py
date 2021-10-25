#Welcoming section
print('Welcome to the Quiz Game!')
print('In a moment I will ask you 3 questions that u have to answear yes / no.')
answear = input ('Are you ready? ').lower()
if answear != 'yes':
    quit()

    

#Questions 


def Questions():   
    score = 0
    correct_ans = ['yes', 'no', 'yes', 'no']


    firstQuestion = input ('Is Rome a capitol of Italy?' '\n').lower()
    if firstQuestion == correct_ans[0]:
        score = score+1
        print('Correct!')
    else:
        print('Incorrect!')
    scdQuestion = input('Is William Shakespeare a author of The Sorrows of Young Werther?' '\n').lower()
    if scdQuestion == correct_ans[1]:
        score = score+1
        print('Correct!')
    else:
        print('Incorrect!')
    thirdQuestion = input ('Winter is a season that comes after fall? ' '\n').lower()
    if thirdQuestion == correct_ans[2]:
        score = score+1
        print('Correct!')
    else:
        print('Incorrect!')
    fourQuestion = input ('Cracov is a capitol of Poland?' '\n').lower()
    if fourQuestion == correct_ans[3]:
        score = score+1
        print('Correct!')
    else:
        print('Incorrect!')
    

    if score == 0:
        print('You didnt guess the answears, try again! Your score is: %s ' % score)
    elif score == 1:
        print('You only guess one, try again! Your score is: %s ' % score)
    elif score == 2:
        print('You guess half aswears, try again! Your score is: %s ' % score)
    elif score == 3:
        print('Almost! You miss one point! Try again! Your score is: %s ' % score)
    else:
        print('Congratulation! You guess everything! Your score is: %s ' % score)






Questions()
