import curses as c
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
from random import choice


c.initscr()
win = c.newwin(20, 60, 0, 0)
win.keypad(1)
c.noecho()
c.curs_set(0)
win.border(0)
win.nodelay(1)

#Initializing values
key = KEY_RIGHT
total_score = 0

#Initializing Snake and Food at the beggining of the game
snake = [[5,10], [5,9], [5,8]]
 
food = [10, 30]

win.addch(food[0], food[1], '@')

gameover = False

while not gameover:
    win.border(0)
    win.addstr(0, 2, ' Score : ' + str(total_score) + ' ')
    win.addstr(0, 27, ' SNAKE GAME ')
    win.timeout(150 - (len(snake)/5 + len(snake)/10)%130)
    
    prevKey = key
    event = win.getch()
    key = key if event == -1 else event 


    if key == ord(' '):
        key = -1
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
        key = prevKey

    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])


    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1

    if snake[0] in snake[1:]: gameover = True

    
    if snake[0] == food:
        food = []
        total_score += 1
        while food == []:
            food = [randint(1, 18), randint(1, 58)]
            if food in snake: food = []
        win.addch(food[0], food[1], '@')
    else:    
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#')
    
c.endwin()
print("\nScore - " + str(total_score))
print("http://bitemelater.in\n")
