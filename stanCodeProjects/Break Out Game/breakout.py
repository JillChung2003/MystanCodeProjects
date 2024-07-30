"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from breakoutgraphics import BRICK_ROWS, BRICK_COLS

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    for i in range(3):
        while True:
            graphics.bounce()
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            graphics.ball.move(vx, vy)
            if graphics.dead() or graphics.win():
                break
            pause(FRAME_RATE)
    if graphics.brick_num == BRICK_ROWS * BRICK_COLS:
        graphics.window.add(graphics.label2)
    else:
        graphics.window.add(graphics.label1)


if __name__ == '__main__':
    main()
