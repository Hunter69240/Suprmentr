import cv2

image_path = "ANGEL AND DEVIL.png"
img = cv2.imread(image_path)
if img is None:
	print("Error: Could not load image. Check image file name/path.")
else:
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	edges = cv2.Canny(blur, 100, 200)
	cv2.imshow("Original", img)
	cv2.imshow("Grayscale", gray)
	cv2.imshow("Blur", blur)
	cv2.imshow("Edges", edges)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

