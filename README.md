# android-frameit
A tool for rendering a device frame around screenshots with text and a background image. 
Google [recommends not using framed screenshots in Play Store](https://developer.android.com/distribute/marketing-tools/device-art-generator). 
Nevertheless, a lot of companies do that for conversion optimization.

## Related projects
The most famous framing solution is integrated into [fastlane](https://docs.fastlane.tools/actions/frameit/).
It works well for iOS but unfortunately not for Android. Even though there is enough demand for an
[Android](https://github.com/fastlane/fastlane/issues/14968) [implementation](https://github.com/fastlane/fastlane/issues/14796),
at the time of creating this project it did not exist yet.

## Installation
You should have Python with [Pillow](https://pillow.readthedocs.io/en/stable/) installed, 
preferably via [pipenv](https://github.com/pypa/pipenv).

```python
pipenv install
```


## Usage
Edit the src/frameit.py configuration to match your needs and run it:

```shell script
pipenv run python src/frameit.py <path to screenshots> --background default.jpg
```

Here is an example to convert a single screenshot

```python
FramedImage(background_name="frame_dog_paws.png", frame="pixel2xl",
            screen_shot="screenshot_phone.png", output_name="output_phone") \
            .add_text("Zooplus Android App",
                      "Von überall bequem und schnell durch\nmehr als 8.000 Produkte für Ihr Haustier stöbern",
                      title_font='fonts/MYRIADPRO-BOLDCOND.otf', text_font='fonts/HelveticaNeueLTPro-LtCn.otf') \
            .save()
```

It will transform a typical screenshot like

![Screenshot](example_screenshot.png)

into a framed image with text:

![Framed](example_framed.png)

For more details on the available parameters type

```shell script
pipenv run python src/frameit.py -h
```

## Credits
Developed for [Zooplus](https://www.zooplus.de/) by [Ulrich Scheller](https://www.ulrich-scheller.de/)
