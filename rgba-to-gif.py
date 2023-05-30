import os
from PIL import Image

ANIM_FOLDER = "animation-frames/"
OUTPUT_FILE = "ouptput.gif"

files = os.listdir(ANIM_FOLDER)
files.sort()

frames = [Image.open(os.path.join(ANIM_FOLDER,file)) for file in files]
frames = [frame.convert("P") for frame in frames]

frames[0].save(OUTPUT_FILE,
               format="GIF",
               append_images=frames[1:],
               save_all=True,
               duration=40,
               transparency=0,
               disposal=2,
               optimize=True)
