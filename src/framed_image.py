from PIL import Image, ImageDraw
from PIL import ImageFont
from device_frame import DeviceFrame


class FramedImage(object):
    """
    Framed image with background, device frame and text
    """
    def __init__(self, background_name="default.png", output_name="output",
                 frame="pixel2xl", screen_shot=None):
        self.background = Image.open(f"backgrounds/{background_name}")
        self.output_name = output_name
        self.frame = frame
        if screen_shot:
            frame = DeviceFrame(frame)
            self.screen_shot = Image.open(screen_shot)
            frame.set_screen_shot(self.screen_shot)
            self.background = self.background.resize(self.screen_shot.size)
            self.set_device_frame(frame.image)
        self.img_draw = ImageDraw.Draw(self.background)

    def _oversize(self):
        if self.frame == "nexus9":
            return 200
        return 0

    def set_device_frame(self, image):
        b_size = self.background.size
        f_size = image.size
        size = (b_size[0] + self._oversize(), int(f_size[1] * (b_size[0] / f_size[0])) + self._oversize())
        image = image.resize(size, Image.ANTIALIAS)
        self.background.paste(image, (0 - (self._oversize()//2), 450 - (self._oversize()//2)), image)

    def add_text(self, title, text, title_font, text_font, title_size=80, text_size=50):
        fnt = ImageFont.truetype(title_font, title_size)
        self.img_draw.text((64, 128), title, fill='white', font=fnt)
        fnt = ImageFont.truetype(text_font, text_size)
        self.img_draw.text((64, 128 + 32 + title_size), text, fill='white', font=fnt, spacing=20)
        return self

    def save(self):
        self.background.save(f"{self.output_name}.png")
