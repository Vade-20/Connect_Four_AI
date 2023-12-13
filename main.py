from tkinter import *
from time import sleep

root = Tk()
root.title('Connect Four')
board = [['' for i in range(7)] for j in range(6)]
FONT_COLOR = 'blue'
BACKGROUND_COLOR = 'white'
READONLY_COLOR_BG = 'black'
READONLY_COLOR_FG = 'red'
player_1 = 'violet'
player_2 = 'black'
turn = True
PAUSE = 1

def new_game(event=None):
    pass

def player_token_animation(event,move):
    global event_board
    for i in range(6):
        for j in range(7):
            if event_board[i][j] == event:
                row = i
                column = j
                break
        else:
            continue
        break
    
    while row != 6:
        event = event_board[row][column]
        event.insert(0,move)
        event.config(bg=player_1,fg=READONLY_COLOR_FG)
        sleep(PAUSE)
        row += 1
        if row != 6 :
            event.delete(0,END)
            event.config(bg=BACKGROUND_COLOR,fg=FONT_COLOR)
    event.config(state='disabled')
    
def adding_turn(event_key,box):
    global turn
    if box['state'] != 'normal':
        return None
    move = 'X' if turn else 'O'
    player_token_animation(box,move)
        
    turn = not turn
            
    













l1 = Label(root, text='TIC TAC TOE', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
l1.grid(row=0, column=0, columnspan=15,sticky=W+E)
l2 = Label(root, text='Game Mode---->', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '12'), bd=3, relief='solid',justify='center')
l2.grid(row=1, column=0,columnspan=2)
l3 = Label(root, text='  '*100, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='flat',justify='center')
l3.grid(row=2, column=0, columnspan=15,sticky=W+E)

mode = StringVar()
options_list = ["PvP", "Computer Easy", "Computer Hard"] 
mode.set('PVP')
o1 = OptionMenu(root,mode,*options_list,command=new_game)
o1.grid(row=1,column=1,columnspan=3) 
o1.config(fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='raised',justify='center',width=20)

event_board = []
for i in range(3,9):
    box__ = []
    for j in range(7):
        e1 = Entry(root, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '30'), bd=3, relief='groove',width=5,justify='center',
                   disabledbackground=READONLY_COLOR_BG,disabledforeground=READONLY_COLOR_FG)
        e1.grid(row=i, column=j)
        e1.bind('<Button-1>',lambda event,box=e1:adding_turn(event,box))
        box__.append(e1)
    event_board.append(box__)
mainloop()