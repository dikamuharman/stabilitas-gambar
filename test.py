
import cv2 as cv

src = cv.imread('citra.jpeg')
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
result = cv.equalizeHist(src)

cv.imwrite('before-equalization.jpg', src);
cv.imwrite('after-equalization.jpg', result);
