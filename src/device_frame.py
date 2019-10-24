from PIL import Image
from functools import lru_cache


@lru_cache(10)
def image_open(file_name):
    return Image.open(file_name)


class DeviceFrame(object):
    """
    device frame image, optionally with a screenshot shown
    """
    def __init__(self, name):
        self.image = image_open(f"device_frames/{name}.png")

    @staticmethod
    def _is_white_pixel(rgb_im, x, y):
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

    def set_screen_shot(self, screen_shot):
        boundaries = self._screen_boundaries()
        size = (boundaries[2] - boundaries[0], boundaries[3] - boundaries[1])
        screen_shot = screen_shot.resize(size, Image.ANTIALIAS)
        self.image.paste(screen_shot, boundaries[:2])
