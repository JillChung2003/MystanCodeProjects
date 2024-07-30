"""
File: blur.py
Name: Jill
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(old_img):
    """
    :param img: SimpleImage, the original image
    :return: the blurred image
    """
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width-1):
        for y in range(old_img.height-1):
            all_red = 0
            all_green = 0
            all_blue = 0
            if old_img.width-1 > x > 0 and old_img.height-1 > y > 0:
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        old_pixel = old_img.get_pixel(i, j)
                        all_red += old_pixel.red
                        all_blue += old_pixel.blue
                        all_green += old_pixel.green
                new_pixel = new_img.get_pixel(x, y)
                new_pixel.red = all_red // 9
                new_pixel.green = all_green // 9
                new_pixel.blue = all_blue // 9
    return new_img


def main():
    """
    The program shows the original image first,
    and then it shows the blurred image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
