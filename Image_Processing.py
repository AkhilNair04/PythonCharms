##Using PIL
from PIL import Image
img = Image.open("ss.webp")
img.show()
gray_img=img.convert('L')
gray_img.show(title="NEW")
gray_img.save('output.webp')

##CV2
import cv2
img = cv2.imread("ss.webp")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
edges=cv2.Canny(img,50,30) #as value decreases efficiency of tracing border increases
cv2.imshow("Image", edges)
blurred_image = cv2.GaussianBlur(img, (171, 153), 0)
cv2.imwrite("Blurred_output.webp", blurred_image)
cv2.imshow("Blurred Image", blurred_image)

def shrink_image(image, factor):
    height, width = image.shape[:2]
    new_width = width // factor
    new_height = height // factor

    shrunk_image = cv2.resize(image,(new_width, new_height))
    return shrunk_image
img = cv2.imread("ss.webp")
small_img = shrink_image(img, 2)
cv2.imshow("Shrunk Image", small_img)

flippi=cv2.flip(img,1)
cv2.imshow("Flipped Image", flippi)
cv2.waitKey(0)
cv2.destroyAllWindows()

##SKIMAGE
from skimage import io, color
import matplotlib.pyplot as plt
img = Image.open("ss.webp").convert("L")
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()
