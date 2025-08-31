import cv2
source = "WhatsApp Image 2025-08-31 at 03.12.47_b2569f59.jpg"
destination = "resized_image.jpg"
image = cv2.imread(source)
scale_percent = 70
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)
resized_image = cv2.resize(image, (new_width, new_height))
cv2.imwrite("resized_image.jpg", resized_image)
cv2.waitKey(0)