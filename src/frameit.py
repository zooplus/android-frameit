"""
Script for framing the 3 example images.
"""

from framed_image import FramedImage

# All available device_frames can be seen in the device_frames folder
device_to_frame = {
    "phone": "pixel2xl",
    "7inch": "nexus9",
    "10inch": "nexus9",
}


def main():
    for device in ("phone", "7inch", "10inch"):
        FramedImage(background_name="frame_dog_paws.png", frame=device_to_frame[device],
                    screen_shot=f"screenshot_{device}.png", output_name=f"output_{device}") \
            .add_text("Zooplus Android App",
                      "Von überall bequem und schnell durch\nmehr als 8.000 Produkte für Ihr Haustier stöbern",
                      title_font='fonts/MYRIADPRO-BOLDCOND.otf', text_font='fonts/HelveticaNeueLTPro-LtCn.otf') \
            .save()


if __name__ == '__main__':
    main()
