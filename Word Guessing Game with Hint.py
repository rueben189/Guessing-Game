from tkinter import *
import tkinter.font as font
import math
import random
from Secret_Word_Dictionary import dictionary_name
from functions import underscoref, runf, spacedf

root = Tk()
root.title('Guessing Game')

frame= LabelFrame(root, padx = 5, pady = 5)

frame.pack(padx =100, pady = 100)

e = Entry(frame, width=35, borderwidth=3)

def playagainf():  #replay
    playagain.grid_forget()
    Label1.destroy()

    startf()
    e.delete(0,END)


def enterf(secret_word,closestguess,guesses, c, a, hintc, end_condition,underscores,clist,clistchange):
    #e.insert(0, closestguess) # this works, but doesnt show up in the entry box
    guess = e.get()

    condition, closestguess, underscores,c, a, hintc, clist, clistchange = runf(secret_word,closestguess, guess, guesses, c, a, hintc, end_condition,underscores,clist,clistchange)
    #print(condition)
    #print(closestguess)
    #print(c)
    #print(hintc)

    global displayclosestguess
    global svar
    global enterbutton
    global playagain
    global Label1
    global displayfont

    displayfont = font.Font(size=30)

    svar = spacedf(secret_word, closestguess)
    if condition == 'first':
        c -= 1
        e.grid_forget()
        displayclosestguess.destroy()
        enterbutton.destroy()
        Label1.destroy()
        Label1 = Label(frame, text='Congratulations! You have guessed the secret word correctly as ' + secret_word + ' in ' + str(c) + ' tries.' )
        Label1.grid(row=3,column=0)
        playagain = Button(frame, text = 'Play Again', command= playagainf)
        playagain.grid(row=4, column=0)


    elif condition == 'second':
        e.delete(0,END)
        displayclosestguess.grid_forget()
        displayclosestguess = Label(frame, text=svar, font=displayfont)
        displayclosestguess.grid(row=0, column=0)
        Label1.destroy()
        Label1 = Label(frame, text='You are on the right track')  # this guess becomes closest guess
        Label1.grid(row=3, column=0)
        enterbutton.grid_forget()
        enterbutton = Button(frame, text='Enter', padx=40, pady=20,
                             command=lambda: enterf(secret_word, closestguess, guesses, c, a, hintc,
                                                    end_condition, underscores, clist, clistchange))
        enterbutton.grid(row=2, column=0)
    elif condition == 'third':
        e.delete(0, END)
        displayclosestguess.grid_forget()
        displayclosestguess = Label(frame, text=svar, font=displayfont)
        displayclosestguess.grid(row=0, column=0)
        Label1.destroy()
        Label1 = Label(frame, text='You get another hint') #they get another hint because current guess in not better that closest guess
        Label1.grid(row=3, column=0)
        enterbutton.grid_forget()
        enterbutton = Button(frame, text='Enter', padx=40, pady=20,
                             command=lambda: enterf(secret_word, closestguess, guesses, c, a, hintc,
                                                    end_condition, underscores, clist, clistchange))
        enterbutton.grid(row=2, column=0)
    elif condition == 'fourth':
        e.delete(0, END)
        displayclosestguess.grid_forget()
        displayclosestguess = Label(frame, text=svar,font=displayfont)
        displayclosestguess.grid(row=0, column=0)
        Label1.destroy()
        Label1 = Label(frame, text='Not Quite. Try Again')
        Label1.grid(row=3, column=0)
        enterbutton.grid_forget()
        enterbutton = Button(frame, text='Enter', padx=40, pady=20,
                             command=lambda: enterf(secret_word, closestguess, guesses, c, a, hintc,
                                                    end_condition, underscores, clist, clistchange))
        enterbutton.grid(row=2, column=0)
    elif condition == 'fifth':  # a guess wasn't entered in entry box
        e.delete(0, END)
        displayclosestguess.grid_forget()
        displayclosestguess = Label(frame, text=svar,font=displayfont)
        displayclosestguess.grid(row=0, column=0)
        Label1.destroy()
        Label1 = Label(frame, text='You did not enter a guess')
        Label1.grid(row=3, column=0)
        enterbutton.grid_forget()
        enterbutton = Button(frame, text='Enter', padx=40, pady=20,
                             command=lambda: enterf(secret_word, closestguess, guesses, c, a, hintc,
                                                    end_condition, underscores, clist, clistchange))
        enterbutton.grid(row=2, column=0)

    elif condition == 'sixth':  # end condition due to underscores is satisfied
        c -= 1
        e.grid_forget()
        displayclosestguess.destroy()
        enterbutton.destroy()
        Label1.destroy()
        Label1 = Label(frame, text='You have exceeded maximum number of guesses of ' + str(c) + ' for this word.  You lose. The word was ' + secret_word)
        Label1.grid(row=3, column=0)
        playagain = Button(frame, text='Play Again', command=playagainf)
        playagain.grid(row=4,column=0)



    return closestguess, guesses, c, a, hintc,underscores,clist,clistchange, enterbutton

def startf():
    secret_word = dictionary_name[str(random.randint(1, len(dictionary_name)))]
    closestguess = secret_word[0]  # first letter of secret word
    guess = ''
    guesses = [closestguess]
    clist = [closestguess]
    clistchange = ['yes']
    c = 0  # c is the iteation number/number of guesses
    hintc = 0  # hint counter, increments by 1 whenever 3 guesses don't improve closestguess, resets when closestguess is
    # updatedfrom functions import underscoref
    a = 0  # if hint completes the word, they lose

    underscores = underscoref(secret_word, closestguess)
    end_condition = math.ceil(len(secret_word) / 3)

    global displayclosestguess
    global svar
    global enterbutton
    global Label1


    displayfont=   font.Font(size= 30)

    svar = spacedf(secret_word, closestguess)
    Label1 = Label(frame, text='')

    startbutton.grid_forget()
    displayclosestguess = Label(frame, text=svar,font=displayfont)
    displayclosestguess.grid(row=0,column=0)
    e.grid(row=1, column=0, padx=10, pady=10)
    enterbutton = Button(frame, text='Enter', padx=40, pady=20,
                         command=lambda: enterf(secret_word, closestguess, guesses, c, a, hintc,
                                                end_condition, underscores, clist, clistchange))
    enterbutton.grid(row=2, column=0)
    return displayclosestguess, enterbutton, closestguess, svar

start = 'start'

if start == 'start':
    startbutton= Button(frame, text = 'Start Game', padx=40,pady=20, command=startf)
    startbutton.grid(row= 2, column=0)
    start = 'false'



root.mainloop()