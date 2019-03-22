Generic letters profile image generator.

This script allows the user to generate images for user profiles, that can be used in any application as a default
placeholder when user hasn't uploaded a custom profile image. The idea is tu have a range of placeholder profile
images that depend on users initials, making the UX better and richer in comparison to just using a single generic 
placeholder image.

This script can be used to generate a customizable set of such images - sizes, fonts and colors can be changed to fit
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
