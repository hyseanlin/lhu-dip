import cv2
import numpy as np
import matplotlib.pyplot as plt

def visualize_gradients(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate gradients in x and y directions
    gradient_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    
    # Calculate gradient magnitude and direction
    magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    direction = np.arctan2(gradient_y, gradient_x) * (180 / np.pi)  # Convert radians to degrees
    
    # Visualization
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(magnitude, cmap='gray')
    plt.title('Gradient Magnitude')
    plt.colorbar()
    
    plt.subplot(1, 2, 2)
    plt.imshow(direction, cmap='hsv')
    plt.title('Gradient Direction')
    plt.colorbar()
    
    plt.show()

# Load an example image
image_path = '../dataset/bw02.bmp'  # Provide the path to your image
image = cv2.imread(image_path)
cv2.imshow('Original Image', image)

# Visualize gradients
visualize_gradients(image)

cv2.waitKey(0)
cv2.destroyAllWindows()