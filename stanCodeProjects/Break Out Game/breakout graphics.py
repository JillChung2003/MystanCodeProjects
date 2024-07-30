"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 5    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        """
        Initializes the Breakout game graphics including the window, paddle, ball, and bricks.
        Sets up the initial game state and mouse event listeners.
        """
        self.click = False
        self.brick_num = 0
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width-paddle_width)/2,
                            y=self.window.height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window.width-ball_radius)/2,
                          y=(self.window.height-ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0
        # Initialize our mouse listeners
        onmousemoved(self.move)
        onmouseclicked(self.start)
        # Draw bricks
        x = 0
        y = brick_offset
        color = ['black', 'dimgray', 'gray', 'silver', 'gainsboro']
        for i in range(brick_rows):
            y += brick_height + brick_spacing
            for j in range(brick_cols):
                x = j * (brick_width + brick_spacing)
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color[i // 2]
                self.brick.color = color[i // 2]
                self.window.add(self.brick, x, y)
        self.label1 = GLabel('Game Over', x=(self.window.width - BALL_RADIUS) / 2 - 40,
                             y=(self.window.height - BALL_RADIUS) / 2 + 50)
        self.label1.font = '-20'
        self.label2 = GLabel('You Win:)', x=(self.window.width - BALL_RADIUS) / 2 - 40,
                             y=(self.window.height - BALL_RADIUS) / 2 + 50)
        self.label2.font = '-20'

    def move(self, mouse):
        """
        Updates the position of the paddle based on the mouse's x position.
        Ensures the paddle stays within the window boundaries.

        :param mouse: The mouse event containing the current x position of the mouse.
        """
        if mouse.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x - self.paddle.width/2 < 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width/2
            self.paddle.y = self.window.height-PADDLE_OFFSET-self.paddle.height

    def start(self, mouse):
        """
        Starts the ball movement when the mouse is clicked for the first time.
        Sets the initial velocity of the ball in a random horizontal direction.

        :param mouse: The mouse event that triggers the ball to start moving.
        """
        if not self.click:
            self.click = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        """
        :return: The horizontal velocity of the ball.
        """
        return self.__dx

    def get_dy(self):
        """
        :return: The vertical velocity of the ball.
        """
        return self.__dy

    def bounce(self):
        """
        Checks for collisions with the walls and paddle, and updates the ball's direction accordingly.
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y >= 0.5 * self.window.height:
            if self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2) or \
                    self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2) is not None:
                self.__dy = -self.__dy
        if self.ball.y <= 0.5 * self.window.height:
            self.collision()

    def dead(self):
        """
        Checks if the ball has fallen below the paddle (the player loses a life).
        Resets the ball's position and velocity if it is below the window height.

        :return:True if the ball is dead (below the window height), False otherwise.
        """
        if self.ball.y >= self.window.height:
            self.click = False
            self.__dy = 0
            self.__dx = 0
            self.ball.x = (self.window.width - BALL_RADIUS) / 2
            self.ball.y = (self.window.height - BALL_RADIUS) / 2
            return True

    def win(self):
        """
        Checks if all bricks have been removed (the player wins the game).

        :return: True if all bricks are removed, False otherwise.
        """
        if self.brick_num == 100:
            return True

    def collision(self):
        """
        Handles the ball's collision with bricks.
        Removes the brick and updates the ball's direction and the number of bricks removed.
        """
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
            self.brick_num += 1
            self.__dy = -self.__dy
        elif self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y) is not None:
            self.window.remove(self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y))
            self.brick_num += 1
            self.__dy = -self.__dy
        elif self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2) is not None:
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2))
            self.brick_num += 1
            self.__dy = -self.__dy
        elif self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2) is not None:
            self.window.remove(self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2))
            self.brick_num += 1
            self.__dy = -self.__dy

