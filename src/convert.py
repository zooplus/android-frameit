from PIL import Image, ImageDraw
from PIL import ImageFont


class DeviceFrame(object):
    def __init__(self, name):
        self.image = Image.open(f"device_frames/{name}.png")

    def _is_white_pixel(self, rgb_im, x, y):
        return rgb_im.getpixel((x, y)) == (255, 255, 255)

    def _screen_boundaries(self):
        rgb_im = self.image.convert('RGB')
        l = r = int(self.image.size[0] / 2)
        u = d = int(self.image.size[1] / 2)
        while self._is_white_pixel(rgb_im, l-1, (u+d)//2):
            l -= 1
        while self._is_white_pixel(rgb_im, r+1, (u+d)//2):
            r += 1
        while self._is_white_pixel(rgb_im, (l+r)//2, u-1):
            u -= 1
        while self._is_white_pixel(rgb_im, (l+r)//2, d+1):
            d += 1
        return l, u, r+1, d+1

    def set_screenshot(self, screenshot):
        boundaries = self._screen_boundaries()
        size = (boundaries[2] - boundaries[0], boundaries[3] - boundaries[1])
        screenshot = screenshot.resize(size, Image.ANTIALIAS)
        self.image.paste(screenshot, boundaries[:2])


class FramedImage(object):
    def __init__(self, background_name="default.png", output_name="output",
                 frame="pixel2xl", screenshot=None):
        self.background = Image.open(f"backgrounds/{background_name}")
        self.output_name = output_name
        if screenshot:
            frame = DeviceFrame(frame)
            self.screenshot = Image.open(screenshot)
            frame.set_screenshot(self.screenshot)
            self.background = self.background.resize(self.screenshot.size)
            self.set_device_frame(frame.image)
        self.img_draw = ImageDraw.Draw(self.background)

    def set_device_frame(self, image):
        b_size = self.background.size
        f_size = image.size
        size = (b_size[0], int(f_size[1] * (b_size[0] / f_size[0])))
        image = image.resize(size, Image.ANTIALIAS)
        self.background.paste(image, (0, 300), image)

    def add_text(self, title, text):
        title_size = 80
        text_size = 50
        fnt = ImageFont.truetype('fonts/MYRIADPRO-BOLDCOND.otf', title_size)
        self.img_draw.text((64, 64), title, fill='white', font=fnt)
        fnt = ImageFont.truetype('fonts/HelveticaNeueLTPro-LtCn.otf', text_size)
        self.img_draw.text((64, 64 + title_size), text, fill='white', font=fnt, spacing=20)

    def save(self):
        self.background.save(f"{self.output_name}.png")


if __name__ == '__main__':
    device_frame = "pixel2xl"  # or nexus9, nexus6p, nexus5x, wear, etc..

    framed_image = FramedImage(background_name="frame_dog_paws.png", frame=device_frame, screenshot="screenshot.png")
    framed_image.add_text("Zooplus Android App",
                          "Von überall bequem und schnell durch\nmehr als 8.000 Produkte für Ihr Haustier stöbern")
    framed_image.save()
