##Using PIL
from PIL import Image
img = Image.open("ss.webp")
img.show()
gray_img=img.convert('L')
gray_img.show(title="NEW")
gray_img.save('output.webp')

##Using CV2
import cv2
img = cv2.imread("ss.webp")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

##SKIMAGE
from skimage import io, color
import matplotlib.pyplot as plt
img = Image.open("ss.webp").convert("L")
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()
