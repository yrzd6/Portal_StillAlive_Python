import time
import sys
import threading
import os
import shutil
import signal

import assets.dispose_arg as args
import assets.lyrics as lyric

from unicodedata import east_asian_width


from assets.credits import *
from assets.ascii_art import ascii_art



# Initialize settings
cursor_x = 0  # Cursor X position
cursor_y = 0  # Cursor Y position
print_lock = threading.Lock()  # Print lock for thread safety


# Load config
DISABLE_SOUND = args.config['nosound']
ENABLE_STAY = args.config['stay']
LANG = args.config['language']
lyrics = lyric.lyrics[LANG]

print(f'Disable sound: {DISABLE_SOUND}, Enable stay: {ENABLE_STAY}, Language: {LANG}')



# Sleep for 1 seconds to wait for the terminal to initialize
time.sleep(4)


# Get terminal dimensions
term_columns, term_lines = shutil.get_terminal_size()
if term_columns < 80 or term_lines < 24:
    print("Error: Terminal size must be at least 80x24")
    sys.exit(1)

is_draw_end = False  # Flag to indicate if drawing is complete


# Handle Ctrl+C interrupt signal
def sigint_handler(sig, frame):
    try:
        end_draw()
    except:
        print('\033[0m', end='')  # Reset all attributes
    finally:
        print('User interrupted')
        sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)


# Begin drawing with yellow text on black background
def begin_draw():
    print_lock.acquire()
    print('\033[40m\033[38;5;3m', end='')  # Black bg, yellow text
    print_lock.release()


# End drawing and reset terminal settings
def end_draw():
    global is_draw_end
    print_lock.acquire()
    is_draw_end = True
    print('\033[0m', end='')  # Reset all attributes
    clear(False)
    move(1, 1, False, False)
    print_lock.release()


# Move cursor to specified position
def move(x, y, update_cursor=True, mutex=True):
    global cursor_x, cursor_y
    if mutex:
        print_lock.acquire()
    print("\033[%d;%dH" % (y, x), end='')
    sys.stdout.flush()
    if update_cursor:
        cursor_x = x
        cursor_y = y
    if mutex:
        print_lock.release()


# Clear screen
def clear(mutex=True):
    global cursor_x, cursor_y
    cursor_x = 1
    cursor_y = 1
    if mutex:
        print_lock.acquire()
    print('\033[2J', end='')
    if mutex:
        print_lock.release()


# Get character width
def get_char_width(ch):
    if east_asian_width(ch) in  ('F', 'W', 'A'):
        return 2
    else:
        return 1

# Thread-safe print function
def _print(str, newline=True):
    global cursor_x, cursor_y
    print_lock.acquire()
    if newline:
        print(str)
        cursor_x = 1
        cursor_y += 1
    else:
        print(str, end='')
        cursor_x += get_char_width(str)
    print_lock.release()


# UI layout parameters
ascii_art_width = 40  # ASCII art width
ascii_art_height = 20  # ASCII art height
credits_width = min((term_columns - 4) // 2, 56)  # Credits section width
credits_height = term_lines - ascii_art_height - 2  # Credits section height
lyric_width = min(term_columns - 4 - credits_width, 56)  # Lyrics section width
lyric_height = term_lines - 3  # Lyrics section height

# Section positions
credits_pos_x = lyric_width + 4  # Credits X position
ascii_art_x = lyric_width + 4 + (credits_width - ascii_art_width) // 2  # ASCII art X
ascii_art_y = credits_height + 3  # ASCII art Y position


# Draw ASCII art
def drawAA(x, y, ch):
    for dy in range(ascii_art_height):
        move(x, y + dy)
        print(ascii_art[ch][dy], end='')
        sys.stdout.flush()
        time.sleep(0.01)


# Draw UI frame
def drawFrame():
    move(1, 1)
    print(' ' + '-' * lyric_width + '  ' + '-' * credits_width + ' ')
    for _ in range(credits_height):
        print('|' + ' ' * lyric_width + '||' + ' ' * credits_width + '|')

    print('|' + ' ' * lyric_width + '| ' + '-' * credits_width + ' ')
    for _ in range(lyric_height - 1 - credits_height):
        print('|' + ' ' * lyric_width + '|')
    print(' ' + '-' * lyric_width + ' ')
    move(2, 2)
    sys.stdout.flush()
    time.sleep(1)


# Clear lyrics section
def clearLyrics():
    move(1, 2)
    for _ in range(lyric_height):
        _print('|' + ' ' * lyric_width)
    move(2, 2)


# Draw lyrics with character animation
def drawLyrics(str, x, y, interval, newline):
    move(x + 2, y + 2)
    for ch in str:
        _print(ch, False)
        sys.stdout.flush()
        time.sleep(interval)
        x += get_char_width(ch)
    if newline:
        x = 0
        y += 1
        move(x + 2, y + 2)
    return x


# Credits scrolling thread
class ThreadCredits(threading.Thread):
    def run(self):
        credit_x = 0
        i = 0
        length = len(credits)
        last_credits = [""]
        startTime = time.time()

        for ch in credits:
            currentTime = startTime + 174.0 / length * i
            i += 1

            if ch == '\n':
                credit_x = 0
                last_credits.append("")
                if len(last_credits) > credits_height:
                    last_credits = last_credits[-credits_height:]

                print_lock.acquire()
                if is_draw_end:
                    print_lock.release()
                    break

                # Update credits display
                for y in range(2, 2 + credits_height - len(last_credits)):
                    move(credits_pos_x, y, False, False)
                    print(' ' * credits_width, end='')

                for k in range(len(last_credits)):
                    y = 2 + credits_height - len(last_credits) + k
                    move(credits_pos_x, y, False, False)
                    print(last_credits[k], end='')
                    print(' ' * (credits_width - len(last_credits[k])), end='')

                move(cursor_x, cursor_y, False, False)
                print_lock.release()
            else:
                last_credits[-1] += ch
                print_lock.acquire()
                if is_draw_end:
                    print_lock.release()
                    break

                move(credits_pos_x + credit_x, credits_height + 1, False, False)
                print(ch, end='')
                move(cursor_x, cursor_y, False, False)
                print_lock.release()
                credit_x += 1

            while time.time() < currentTime:
                time.sleep(0.01)


# Main program
begin_draw()
clear()
drawFrame()
move(2, 2)
time.sleep(1)

startTime = time.time() * 100
currentTime = 0
currentLyric = 0
x = 0
y = 0

# Main lyrics display loop
while lyrics[currentLyric].mode != 9:
    currentTime = time.time() * 100 - startTime

    if currentTime > lyrics[currentLyric].time:
        if lyrics[currentLyric].mode <= 1 or lyrics[currentLyric].mode >= 5:
            wordCount = len(lyrics[currentLyric].words)
        if wordCount == 0:
            wordCount = 1

        # Calculate interval between characters
        if lyrics[currentLyric].interval < 0:
            interval = (lyrics[currentLyric + 1].time - lyrics[currentLyric].time) / 100.0 / wordCount
        else:
            interval = lyrics[currentLyric].interval / wordCount

        # Process lyrics based on mode
        if lyrics[currentLyric].mode == 0:  # Normal mode with newline
            x = drawLyrics(lyrics[currentLyric].words, x, y, interval, True)
            y += 1
        elif lyrics[currentLyric].mode == 1:  # No newline mode
            x = drawLyrics(lyrics[currentLyric].words, x, y, interval, False)
        elif lyrics[currentLyric].mode == 2:  # Show ASCII art
            drawAA(ascii_art_x, ascii_art_y, lyrics[currentLyric].words)
            move(x + 2, y + 2)
        elif lyrics[currentLyric].mode == 3:  # Clear lyrics section
            clearLyrics()
            x = 0
            y = 0
        elif lyrics[currentLyric].mode == 4 and not DISABLE_SOUND:
            try:
                from playsound import playsound

                music_file = "./assets/sa1.mp3"
                if os.path.exists(music_file):
                    threading.Thread(
                        target=lambda: playsound(music_file, block=True),
                        daemon=True
                    ).start()
            except:
                pass
        elif lyrics[currentLyric].mode == 5:  # Start credits scroll
            th_credit = ThreadCredits()
            th_credit.daemon = True
            th_credit.start()

        currentLyric += 1

    time.sleep(0.01)

end_draw()

# Keep program running if ENABLE_STAY is True
while ENABLE_STAY:
    time.sleep(60)