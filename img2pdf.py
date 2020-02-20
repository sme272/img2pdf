import os
import sys
from PIL import Image

filelist = [i for i in os.listdir('./') if (i.endswith(".jpg") or i.endswith(".png"))]
imagelist = []

for image in filelist:
	 img = Image.open(image)
	 img = img.convert('RGB')
	 imagelist.append(img)

imagelist[0].save(f'./{sys.argv[1]}.pdf', save_all=True, append_images=imagelist[1:])