import cv2
from skimage import metrics
import numpy as np

image1 = cv2.imread('Flower.jpg')
image2 = cv2.imread('full-moon.jpg')

gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
height, width = gray_image2.shape[:2]  
gray_image1_resized = cv2.resize(gray_image1, (width, height))
# Mean Squared Error (MSE)
mse = np.mean((gray_image1_resized - gray_image2) ** 2)

#  Structural Similarity Index (SSIM)
ssim_index = metrics.structural_similarity(gray_image1_resized, gray_image2)

# Normalized Cross-Correlation (NCC)
ncc = cv2.matchTemplate(gray_image1_resized, gray_image2, cv2.TM_CCORR_NORMED)[0][0]

print("Mean Squared Error (MSE):", mse)
print("Structural Similarity Index (SSIM):", ssim_index)
print("Normalized Cross-Correlation (NCC):", ncc)