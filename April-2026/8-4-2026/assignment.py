'''
Assignment (08/04/2026)

Assignment Name : Image Filter Lab
Description : Use OpenCV to grayscale, blur, detect edges and show before/after.
'''

from pathlib import Path

import cv2
import numpy as np


def get_image_path() -> Path:
	"""Use sample_input.png in this folder; create one if missing."""
	image_path = Path(__file__).parent / "sample_input.png"

	if not image_path.exists():
		sample = np.zeros((300, 400, 3), dtype=np.uint8)
		cv2.rectangle(sample, (20, 20), (180, 150), (0, 255, 0), -1)
		cv2.circle(sample, (280, 90), 60, (255, 0, 0), -1)
		cv2.line(sample, (30, 250), (370, 220), (0, 0, 255), 6)
		cv2.putText(sample, "OpenCV", (110, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
		cv2.imwrite(str(image_path), sample)

	return image_path


image_file = get_image_path()
image = cv2.imread(str(image_file))

if image is None:
	raise ValueError("Could not load image file.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (9, 9), 0)
edges = cv2.Canny(image, 100, 200)

gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

top_row = np.hstack((image, gray_bgr))
bottom_row = np.hstack((blurred, edges_bgr))
comparison = np.vstack((top_row, bottom_row))

output_file = Path(__file__).parent / "before_after.png"
cv2.imwrite(str(output_file), comparison)

print(f"Loaded image: {image_file.name}")
print("\nApplied filters:")
print("1) Grayscale: converts color image to black and white shades.")
print("2) Blur: smooths image and reduces noise.")
print("3) Edge Detection: highlights object boundaries.")
print(f"\nBefore/After saved as: {output_file.name}")

window_title = "Image Filter Lab - Before/After"
try:
	cv2.imshow(window_title, comparison)
	print("\nA window is opened. Press any key in that window to close.")
	cv2.waitKey(0)
	cv2.destroyAllWindows()
except cv2.error:
	print("GUI preview not available in this environment.")
	print("Open before_after.png to see before/after result.")