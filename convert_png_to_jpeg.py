from PIL import Image

dark = (33,33,33)
light = (225,255,255)

iml = Image.open(r'data/images/img-test.png')
bg = Image.new("RGB", iml.size, dark)
bg.paste(iml,iml)
bg.save("test.jpeg", quality=95)