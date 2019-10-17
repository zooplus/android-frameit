from PIL import Image, ImageDraw
from PIL import ImageFont

SHRINK = 114


class DeviceFrame(object):
    def __init__(self, name):
        self.image = Image.open(f"device_frames/{name}.png")

    def _is_white_pixel(self, rgb_im, x, y):
        return rgb_im.getpixel((x, y)) == (255, 255, 255)

    def _screen_boundaries(self):
        rgb_im = self.image.convert('RGB')
        l = r = int(self.image.size[0] / 2)
        u = d = int(self.image.size[1] / 2)
        while self._is_white_pixel(rgb_im, l-1, u):
            l -= 1
        while self._is_white_pixel(rgb_im, r+1, u):
            r += 1
        while self._is_white_pixel(rgb_im, r, u-1):
            u -= 1
        while self._is_white_pixel(rgb_im, r, d+1):
            d += 1
        return l, u, r+1, d+1

    def set_screenshot(self, screenshot):
        boundaries = self._screen_boundaries()
        size = (boundaries[2] - boundaries[0], boundaries[3] - boundaries[1])
        screenshot = screenshot.resize(size)
        self.image.paste(screenshot, boundaries[:2])


class FramedImage(object):
    def __init__(self, background_name="default", output_name="output"):
        self.background = Image.open(f"backgrounds/{background_name}.jpg")
        self.output_name = output_name
        self.img_draw = ImageDraw.Draw(self.background)

    def set_device_frame(self, image):
        b_size = self.background.size
        f_size = image.size
        size = (b_size[0], int(f_size[1] * (b_size[0] / f_size[0])))
        image = image.resize(size)
        self.background.paste(image, (0, 500), image)

    def add_text(self, text):
        fnt = ImageFont.truetype('src/Fulbo-Argenta.otf', 60)
        self.img_draw.text((64, 64), text, fill='white', font=fnt)

    def save(self):
        self.background.save(f"{self.output_name}.png")


if __name__ == '__main__':
    # frame = DeviceFrame("pixel2")
    # frame = DeviceFrame("nexus5x")
    frame = DeviceFrame("nexus6p")
    frame.set_screenshot(Image.open("screenshot.png"))

    framed_image = FramedImage()
    framed_image.set_device_frame(frame.image)
    framed_image.add_text("Zooplus Android App")
    framed_image.save()
