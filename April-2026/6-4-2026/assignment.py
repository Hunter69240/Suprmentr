'''
Assignment (06/04/2026)

Assignment Name : Image as Numbers
Description : Load an image, print shape, pixel values, channels, and explain them.
'''

from pathlib import Path

import numpy as np
from PIL import Image


def get_image_path() -> Path:
	"""Use sample_image.png in this folder; create one if missing."""
	image_path = Path(__file__).parent / "sample_image.png"

	if not image_path.exists():
		sample = np.array(
			[
				[[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0]],
				[[255, 255, 255], [0, 0, 0], [255, 0, 255], [0, 255, 255]],
				[[120, 80, 200], [90, 30, 10], [200, 200, 200], [50, 150, 20]],
				[[10, 10, 10], [240, 240, 240], [30, 60, 90], [220, 100, 40]],
			],
			dtype=np.uint8,
		)
		Image.fromarray(sample).save(image_path)

	return image_path


image_file = get_image_path()
image = Image.open(image_file).convert("RGB")
image_array = np.array(image)

height, width, channels = image_array.shape

print(f"Loaded image: {image_file.name}")
print("\n1) Shape:")
print(f"Image shape = {image_array.shape}")
print(
	"This means: Height =",
	height,
	", Width =",
	width,
	", Channels =",
	channels,
)

print("\n2) Pixel values:")
print("Top-left pixel [0, 0] (R, G, B):", image_array[0, 0])
print("Center pixel [height//2, width//2] (R, G, B):", image_array[height // 2, width // 2])
print("Each pixel has 3 numbers from 0 to 255 -> [Red, Green, Blue].")

red_channel = image_array[:, :, 0]
green_channel = image_array[:, :, 1]
blue_channel = image_array[:, :, 2]

print("\n3) Channels:")
print("Red channel shape:", red_channel.shape)
print("Green channel shape:", green_channel.shape)
print("Blue channel shape:", blue_channel.shape)
print("A channel is one color layer across all pixels.")

print("\n4) Quick channel summary:")
print(f"Red min/max: {red_channel.min()} / {red_channel.max()}")
print(f"Green min/max: {green_channel.min()} / {green_channel.max()}")
print(f"Blue min/max: {blue_channel.min()} / {blue_channel.max()}")