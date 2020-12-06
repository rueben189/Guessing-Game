

def underscoref(secret_word, closestguess):
    underscores = ''
    for num in range(0,len(secret_word)-len(closestguess)):
        underscores = underscores + ('_')
    return underscores

def spacedf(secret_word, closestguess):
    svar= ''
    for num in range(0,len(closestguess)):
        svar= svar + closestguess[num] + ' '
    for num in range(0, len(secret_word) - len(closestguess)):
        svar = svar + '_ '
        #if num == len(closestguess):
            #break

    return svar
def runf(secret_word,closestguess,guess, guesses,c, a, hintc, end_condition,underscores, clist,clistchange):
    global condition

    #while closestguess != secret_word:
    guesses.append(guess)

    if guess in secret_word:
        if guess == secret_word:
            closestguess = guess
            c += 1
            condition = 'first'
            # enterbutton = Button(root, text='Enter', padx=40, pady=20, command=enterf)
            #break
        else:
            guessi = ''
            for num in range(1, len(secret_word)):
                guessi = guess[0:num]
                if guessi in secret_word:
                    pass
                else:
                    guessi = guessi[0:num - 1]
                    break

            if len(guess) > len(closestguess):

                hintc = 0  # everytime closestguess is improved reset counter for hints to 0
                # enterbutton = Button(root, text='Enter', padx=40, pady=20, command=enterf)
                closestguess = guessi
                clist.append(closestguess)
                underscores = underscoref(secret_word, closestguess)
                clistchange.append('yes')
                condition = 'second'
            else:
                hintc += 1  # the guess is in secret word, but is the same guess
                condition = 'fourth'
                clistchange.append('no')

            if hintc >= 2:
                condition = 'third'
                closestguess = secret_word[0:len(closestguess) + 1]
                underscores = underscoref(secret_word, closestguess)
                clist.append(closestguess)
                if len(underscores) <= end_condition:
                    clistchange.append('no')
                else:
                    clistchange.append('yes')
                hintc = 0
                a = 0
                # enterbutton = Button(root, text='Enter', padx=40, pady=20, command=enterf)
    elif guess not in secret_word:

        guessi = ''
        for num in range(1, len(secret_word)):
            guessi = guess[0:num]
            if guessi in secret_word:
                pass
            else:
                guessi = guess[0:num - 1]
                break

        if len(guessi) > len(closestguess):

            closestguess = guessi
            clist.append(closestguess)
            underscores = underscoref(secret_word, closestguess)
            clistchange.append('yes')
            hintc = 0
            condition = 'second'


        elif hintc >= 2:
            closestguess = secret_word[0:len(closestguess) + 1]
            underscores = underscoref(secret_word, closestguess)
            clist.append(closestguess)
            if len(underscores) <= end_condition:
                clistchange.append('no')
            else:
                clistchange.append('yes')

            hintc = 0
            a = 0
            condition = 'third'

        else:
            hintc += 1
            condition = 'fourth'
            clistchange.append('no')


    elif guess == '':
        hintc += 1
        condition = 'fifth'
        clistchange.append('no')

    clistend = False
    if clistchange[-1] == 'no':
        if len(clistchange) < 3:
            pass
        else:
            if clistchange[-1] == clistchange[-2] and clistchange[-2] == clistchange[-3]:
                clistend = True  # if 3 after 3 failed attempts at guess beyond end_condition, break
            else:
                clistend = False

    if len(underscores) <= end_condition and clistend:  # clist did not update in 3 iteration
        c += 1
        condition = 'sixth'
        #break

    c += 1
    return condition, closestguess, underscores, c, a, hintc, clist, clistchange

