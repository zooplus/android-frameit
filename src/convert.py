from framed_image import FramedImage


def main():
    device_frame = "pixel2xl"  # or nexus9, nexus6p, nexus5x, wear, etc..
    FramedImage(background_name="frame_dog_paws.png", frame=device_frame, screen_shot="screenshot.png") \
        .add_text("Zooplus Android App",
                  "Von überall bequem und schnell durch\nmehr als 8.000 Produkte für Ihr Haustier stöbern",
                  title_font='fonts/MYRIADPRO-BOLDCOND.otf', text_font='fonts/HelveticaNeueLTPro-LtCn.otf') \
        .save()


if __name__ == '__main__':
    main()
