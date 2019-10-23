"""
Convert screenshots to include a device frame, background image and some text. The existing files are overwritten.
"""

import sys
import os
from framed_image import FramedImage
import translations


# All available device_frames can be seen in the device_frames folder
device_to_frame = {
    "phone": "pixel2xl",
    "sevenInch": "nexus9",
    "tenInch": "nexus9",
}

translations = translations.create()


def frame_fastlane_screenshots(folder):
    """
    Frame all png images inside the given folder, including subfolders
    :param folder: base folder
    """
    for root, dirs, files in os.walk(folder):
        for file in files:
            if ".png" in file:
                device = os.path.basename(root).replace("Screenshots", "")
                FramedImage(background_name="frame_dog_paws.png", frame=device_to_frame[device],
                            screen_shot=os.path.join(root, file), output_name=os.path.join(root, file)) \
                    .add_text(translations.get_title(root, file), translations.get_message(root, file),
                              title_font='fonts/MYRIADPRO-BOLDCOND.otf',
                              text_font='fonts/HelveticaNeueLTPro-LtCn.otf') \
                    .save()


if __name__ == '__main__':
    frame_fastlane_screenshots(sys.argv[1])
