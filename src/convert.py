from PIL import Image, ImageDraw
from PIL import ImageFont

SHRINK = 114


if __name__ == '__main__':
    screenshot = Image.open("screenshot.png")
    blank_image = Image.open("background.png")
    img_draw = ImageDraw.Draw(blank_image)
    old_size = screenshot.size

    size = (screenshot.size[0] - (2 * SHRINK), screenshot.size[1] - (2 * SHRINK))
    screenshot.thumbnail(size)
    blank_image.paste(screenshot, (SHRINK, 290 + old_size[1] - screenshot.size[1]))

    fnt = ImageFont.truetype('src/Fulbo-Argenta.otf', 60)
    img_draw.text((64, 64), 'Zooplus Android App', fill='white', font=fnt)
    img_draw.text((64, 124), 'blablablabla', fill='white', font=fnt)

    blank_image.save('output.png')
