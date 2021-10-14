import os
from PIL import Image

# image formatting
image_quality = 70  # image quality will become the given number - range: 1-100
image_width = 800
image_height = 500


fileDir = os.path.dirname(__file__) # current file directory
imagesFolder = os.path.join(fileDir, 'images') # path to images folder
optimizedFolder = os.path.join(fileDir, 'optimized')

# if the folder to save optimized images doesn't exist then create it
if os.path.isdir('optimized') == False:
  os.mkdir(optimizedFolder)

unopt_images = []
for file in os.listdir(imagesFolder):
  if file.endswith(('jpg', 'jpeg', 'png')):
    unopt_images.append(file)
    size = os.stat(imagesFolder + f"\{file}").st_size
    print(f"Original image size: {file} - {size}")

print('compressing images...')
for image in unopt_images:
  img = Image.open(os.path.join(fileDir, 'images', image))
  # resizing images to given dimension (800x500)
  img = img.resize((image_width, image_height), resample=1)
  img.save(
    os.path.join(optimizedFolder, image),
    optimize = True,
    quality = image_quality
  )
  size = os.stat(optimizedFolder + f"\{image}").st_size
  print(f"New compressed image size: {image} - size{size}")