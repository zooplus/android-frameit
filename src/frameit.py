"""
Convert screenshots to include a device frame, background image and some text. The existing files are overwritten.
"""

import os
import argparse
from translations import Translations
from framed_image import FramedImage


device_to_frame = {
    # All available device_frames can be seen in the device_frames folder
    "phone": "pixel2xl",
    "sevenInch": "tablet1200x2048",
    "tenInch": "tablet1600x2560",
}


def frame_fastlane_screenshots(folder, background, translations):
    """
    Frame all png images inside the given folder, including subfolders
    :param background: background image to use
    :param folder: base folder
    """
    for root, dirs, files in os.walk(folder):
        for file in files:
            if ".png" in file:
                device = os.path.basename(root).replace("Screenshots", "")
                FramedImage(background_name=background, frame=device_to_frame[device],
                            screen_shot=os.path.join(root, file), output_name=os.path.join(root, file)) \
                    .add_text(translations.get_title(root, file), translations.get_message(root, file),
                              title_font='fonts/MYRIADPRO-BOLDCOND.otf',
                              text_font='fonts/HelveticaNeueLTPro-LtCn.otf') \
                    .save()


def main():
    parser = argparse.ArgumentParser(description='Frame screenshots with a device frame, background, etc...')
    parser.add_argument('folder', nargs="?",
                        help='specify the base folder where all the screenshots can be found')
    parser.add_argument('--background', dest="background", default="default.jpg",
                        help='background image to use')
    parser.add_argument('--translations', dest="translations", default="default.json",
                        help='translations file to use')

    args = parser.parse_args()
    translations = Translations(args.translations)
    if args.folder:
        frame_fastlane_screenshots(args.folder, background=args.background, translations=translations)
    else:
        parser.parse_args(["-h"])


if __name__ == '__main__':
    main()
