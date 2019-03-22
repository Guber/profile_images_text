from PIL import Image, ImageDraw, ImageFont
import string

""" Generic letters profile image generator.

This script allows the user to generate images for user profiles, that can be used in any application as a default
placeholder when user hasn't uploaded a custom profile image. The idea is tu have a range of placeholder profile
images that depend on users initials, making the UX better and richer in comparison to just using a single generic 
placeholder image.

This script can be used to generate a customizable set of such images - sizes, example and colors can be changed to fit
the application in which generated images can be used.

The core functionality uses PIL library.

This file can also be imported as a module and contains the following
functions:

    * profile_image_generator - generates a generic user profile image

Todo:
    * add ability to be called from terminal with a hel function
    * add more customization options (no circle, circle :) )
    * more anti-aliasing options
    * better example


"""


def generate_profile_image(filename, text, font, text_color, image_dimensions, background_color, circle_padding,
                           circle_color, imgtype='JPEG', quality=90):
    """ Generates a generic user profile image.

    Args:
        filename: generated filename
        type: generated filetype (check possible image file types defined by PIL module)
        quality: set a value between 0-100, lower values mean lower quality but lesser file size
        text: text to be displayed on the image, usually initials
        font: PIL ImageFont object that defines the displayed text's style
        text_color: displayed text's color (possible color names defined by PIL modules)
        image_dimensions: generated image dimensions
        background_color: generated image background color (possible color names defined by PIL modules)
        circle_padding: circle in which text is displayed's padding dimensions
        circle_color: circle in which text is displayed's color


    Returns:
        The return value. True for success, False otherwise.

    """

    img = Image.new('RGB', (image_dimensions[0], image_dimensions[1]), color=background_color)
    d = ImageDraw.Draw(img)
    d.ellipse(
        (circle_padding, circle_padding, image_dimensions[0] - circle_padding, image_dimensions[1] - circle_padding),
        fill=circle_color)

    text_pos = ((image_dimensions[0] - font.getsize(text)[0]) / 2,
                (image_dimensions[0] - font.getsize(text)[1]) / 2 - circle_padding)

    d.text(text_pos, text, font=font, fill=text_color)

    img = img.resize((700, 700), Image.ANTIALIAS)
    img.save(filename, imgtype, quality=quality, optimize=True, progressive=True)


def main():
    image_dimensions = (1440, 1440)
    circle_padding = 40
    circle_color = '#29C4AF'
    background_color = 'white'
    fnt = ImageFont.truetype('./example/fonts/Raleway.ttf', 500)
    text_color = 'white'
    alphabet = list(string.ascii_uppercase) + ['Č', 'Ć', 'Š', 'Ž']
    for c_1 in alphabet:
        for c_2 in alphabet:
            text = (c_1 + " " + c_2).upper()
            filename = './profile_images/' + text.replace(' ', '_') + '.jpeg'
            generate_profile_image(filename, text, fnt, text_color, image_dimensions, background_color, circle_padding,
                                   circle_color)


if __name__ == '__main__':
    main()
