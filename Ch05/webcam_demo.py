import cv2
import numpy as np
import scipy.special as special

def beta_correction(f, a=2.0, b=2.0):
    # Create the lookup table
    x = np.linspace(0, 1, 256)
    table = np.round(special.betainc(a, b, x) * 255).astype(np.uint8)
    
    # Apply the lookup table to the image
    g = table[f]
    
    return g

# Initialize the webcam
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
    
beta_enabled = False

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    if beta_enabled:    
        frame = beta_correction(frame)

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('b'):
        beta_enabled = not beta_enabled

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
