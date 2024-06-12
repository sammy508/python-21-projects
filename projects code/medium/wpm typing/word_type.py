

#WPm 
import curses
from curses import wrapper
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test!")
    stdscr.addstr("\n press any kry to begin! \n")
    stdscr.refresh()
    key = stdscr.getkey()


    stdscr.refresh()
    stdscr.getkey()

def wpm_tester(stdscr):
    target_text = "The quick brown fox jumps over the laxy dog."
    current_text =[]

    while True:
        stdscr.clear()
        stdscr.addstr(target_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(2))

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
