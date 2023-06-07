import os
from PIL import Image

ANIM_FOLDER = "animation-frames/"
OUTPUT_FILE = "ouptput.gif"

def convert(input_folder, output_path):
    files = os.listdir(input_folder)
    files.sort()

    frames = [Image.open(os.path.join(input_folder,file)) for file in files]
    frames = [frame.convert("P") for frame in frames]

    frames[0].save(output_path,
                format="GIF",
                append_images=frames[1:],
                save_all=True,
                duration=40,
                transparency=0,
                disposal=2,
                optimize=True)

if __name__ == '__main__':
    convert(ANIM_FOLDER, OUTPUT_FILE)