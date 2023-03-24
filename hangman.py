import random     #for recieving a sentence
import time       #for the timer bonus

listoflists = [
['Always','be', 'yourself'],
['Always' ,'deliver', 'quality'],
['Ask','powerful', 'questions'],
['Audit' ,'your', 'metrics'],
['Audit', 'your', 'mistakes'],
['Based', 'on' ,'results'],
['Be', 'constantly', 'curious'],
['Be' ,'here', 'now'],
['Be' ,'the' ,'change'],
['Be' ,'the' ,'communication'],
['Believe', 'you' ,'can']
]

#play = True
def play():

        print('you are playing Word Guess! good luck:)\n\n\n')
        sentence = random.choice(listoflists) #call the random sentence
        blank_list = blank_sentence(sentence) #create the blank_list
        blank_list = ' '.join(blank_list)   #make the blank list str
        joins = ' '.join(sentence)        #make the sentence str
        joins = joins.lower()            #make sentence lower case
        get_guess(blank_list, joins)     #send the new status of sentence and blank list to the user guess func



def blank_sentence(sentence):   # recives sentence and return blank_list
    # print(sentence)
    blank_list = []
    for i in sentence:    #loop for all the indexes in the sentence
        output = '_' * len(i)
        blank_list.append(output) #append '_' to each letter (index)
    return blank_list


def sentence_new_status(guess, joins, blank_list, score):  #recives  str sentence , user guess , blank_list and first score
                                                           # and return the new status of  blank_list and score
    if guess in joins: #check if user guess is in the str sentence and if True add 5 points to score
        score += 5
        for letter in range(len(joins)):
            if guess == joins[letter]:
                blank_list = blank_list[:letter] + guess + blank_list[letter+1:] #place the correct guess in the right place

    else:
        print('wrong, try again')
        score -= 1

    print(f'current points:{score}\ndo it fast if you want bonus!!\n\n')         #print the  current score points and current status of the sentence
    print(blank_list)

    return blank_list, score

def get_guess(blank_list, joins):

        guess = ''
        score = -5
        start = time.time()
        edited_sentence, score = sentence_new_status(guess, joins, blank_list, score)
        while edited_sentence != joins:
            guess = input('enter letter:')
            guess = guess.lower()

            edited_sentence, score = sentence_new_status(guess, joins, edited_sentence, score)

        end = time.time()
        if end - start < 30:
            score += 100
            print('\n\n\nnice! you have got the BONUS!!!\n\n\n')
        print(f'success!! your score is:{score}')


again = True   # run the game in while loop in order to play again when finished
while again:
    play()
    input1 = input('play again? type y/n')
    if input1 == 'n':
        again =  False



