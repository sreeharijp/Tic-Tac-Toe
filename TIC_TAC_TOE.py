import TIC as a
import turtle as b
a.tic()
while 1:
    c=b.textinput('TIC TAC TOE','Do you want to play again?(YES/NO)')
    if c in ['yes','YES','Yes','Y','y']:
        b.clear()
        a.tic()
        break
    elif c in ['No','NO','no','N','n']:
        b.bye()
        break


