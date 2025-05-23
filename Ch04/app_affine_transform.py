import streamlit as st
import cv2
import numpy as np
from PIL import Image

def draw_polylines_with_text(image, points, color, thinkness=3, label='p'):
    points = points.astype(np.int32)
    # draw polines
    cv2.polylines( image, [points], True, color, thinkness)
    # draw text
    for i in range(points.shape[0]):
        cv2.putText(image, f'{label}{i}', points[i], cv2.FONT_HERSHEY_PLAIN, 5.0, color, thinkness)


# Streamlit app title
st.title("Affine Transformation App")

# Image upload in the sidebar
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is not None:
    # Convert the file to an OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Get the dimensions of the image
    (h, w) = image.shape[:2]

    st.sidebar.write("Enter the source points (control points on the original image):")
    src_points = []
    src_points.append([
        st.sidebar.slider('Source point 1 - x:', min_value=0, max_value=w, value=w // 4),
        st.sidebar.slider('Source point 1 - y:', min_value=0, max_value=h, value=h // 4)
    ])
    src_points.append([
        st.sidebar.slider('Source point 2 - x:', min_value=0, max_value=w, value=w * 3 // 4),
        st.sidebar.slider('Source point 2 - y:', min_value=0, max_value=h, value=h // 4)
    ])
    src_points.append([
        st.sidebar.slider('Source point 3 - x:', min_value=0, max_value=w, value=w // 2),
        st.sidebar.slider('Source point 3 - y:', min_value=0, max_value=h, value=h * 3 // 4)
    ])

    st.sidebar.write("Enter the destination points:")
    dst_points = []
    dst_points.append([
        st.sidebar.slider('Destination point 1 - x:', min_value=0, max_value=w, value=w // 4),
        st.sidebar.slider('Destination point 1 - y:', min_value=0, max_value=h, value=h // 4)
    ])
    dst_points.append([
        st.sidebar.slider('Destination point 2 - x:', min_value=0, max_value=w, value=w * 3 // 4),
        st.sidebar.slider('Destination point 2 - y:', min_value=0, max_value=h, value=h // 4)
    ])
    dst_points.append([
        st.sidebar.slider('Destination point 3 - x:', min_value=0, max_value=w, value=w // 2),
        st.sidebar.slider('Destination point 3 - y:', min_value=0, max_value=h, value=h * 3 // 4)
    ])

    # Convert to np.float32
    src_points = np.float32(src_points)
    dst_points = np.float32(dst_points)

    # Compute the affine transformation matrix
    M = cv2.getAffineTransform(src_points, dst_points)

    # Apply the affine transformation
    transformed_image = cv2.warpAffine(image, M, (w, h))

    draw_polylines_with_text(image, src_points, (255, 0, 0), 4, 's') # source points
    draw_polylines_with_text(image, dst_points, (0, 0, 255), 3, 'd') # target points

    # Display the uploaded image
    st.image(image, channels="BGR", caption="Uploaded Image")


    # Convert the transformed image to RGB (for PIL compatibility) and display it
    transformed_image_rgb = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)
    st.image(transformed_image_rgb, caption="Transformed Image")

    # Download button for the transformed image
    st.download_button(
        label="Download Transformed Image",
        data=cv2.imencode('.jpg', transformed_image)[1].tobytes(),
        file_name='transformed_image.jpg',
        mime='image/jpeg'
    )
