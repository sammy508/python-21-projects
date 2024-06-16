

#WPm 
import curses
from curses import wrapper
def start_screen(stdscr):
    stdscr.clear()
    #  stdscr.addstr(1,0"Welcome to the speed typing test!") #here 1, 0 means coordination 1 line down and 0 denotes starting space
    stdscr.addstr("Welcome to the speed typing test!")
    stdscr.addstr("\n press any kry to begin! \n")
    stdscr.refresh()
    key = stdscr.getkey()


    stdscr.refresh()
    stdscr.getkey() # it waits to user to press some keys


def display_text(stdscr,current,target, wpm=0):
    stdscr.addstr(target)

    for i,char in enumerate(current):
            stdscr.addstr(char, curses.color_pair(2))


def wpm_tester(stdscr):
    target_text = "The quick brown fox jumps over the laxy dog."
    current_text =[]

    while True:
        stdscr.clear()
        display_text(stdscr,target_text,current_text)
        stdscr.refresh()
        key = stdscr.getkey()

        if ord(key)== 27:
            break
        if key in ("KEY_BACKSPACE", "\b","\x7f"):
            if len(current_text)>0:
                current_text.pop()
        else:
            current_text.append(key) 





def main(stdscr):
    curses.init_pair(  1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(  2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(  3, curses.COLOR_GREEN, curses.COLOR_WHITE)
   
    start_screen(stdscr)
 
    wpm_tester(stdscr)
  


wrapper(main) # Wrapper call outside of the main function


