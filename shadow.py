from PIL import Image, ImageFilter, ImageOps

def dropShadow( image, shadow=(255,255,255,255), offset=(0,0), background = (0,0,0,255), iterations=3, radius=15):

  back = Image.open(sys.argv[1])

  for x in range(0, back.width):
      for y in range(0, back.height):
          if back.getpixel((x,y))[3] != 0:
             back.putpixel((x,y), shadow)
          else:
             back.putpixel((x,y), background)

  n = 0
  while n < iterations:
    back = back.filter(ImageFilter.BoxBlur(radius))
    n += 1

  back.paste(image, offset, image)
  return back

if __name__ == "__main__":
  import sys

  image = Image.open(sys.argv[1])

  dropShadow(image, shadow=(234,100,100,255)).save('k.png')

