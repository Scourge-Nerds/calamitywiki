# Asset navigation.
this is a this is a test test

block: block models 64x64

item: item textures ripped directly from the datapack, then resized by 2

gui: more textures ripped from the datapack

effect: more textures ripped from the datapack

gif: animated textures

models: other models

painting: paintings

# Code tools

rescale.py: requires PIL (python image library). Rescales all images by 2, tries to make it use a palette, and will not resize them if it is already resized using the magic of metadata

rescale_mobs.py: requires PIL (python image library). Same as rescale, but it targets ./models/mobs & forces images to be 300xY or Xx300, 300 being the smaller size.
