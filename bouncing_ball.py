"""
File: bouncing_ball.py
Name: Jill
-------------------------
The file shows a bouncing ball in animation for three times after the user clicks.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')

ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True

click = False
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    window.add(ball)
    onmouseclicked(drop)


def drop(event):
    global click, count
    if not click:
        count += 1
        click = True
        vy = 0
        if count <= 3:
            while True:
                ball.move(VX, vy)
                vy += GRAVITY
                pause(DELAY)
                if ball.y + ball.height < window.height:
                    vy += GRAVITY
                else:
                    vy = -vy * REDUCE
                if ball.x + ball.width >= window.width:
                    click = False
                    ball.x = START_X
                    ball.y = START_Y
                    break


if __name__ == "__main__":
    main()
