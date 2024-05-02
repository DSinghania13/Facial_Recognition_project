import face_recognition as fr # Importing the face_recognition library
import cv2 # Importing OpenCV library
import numpy as np # Importing numpy library for numerical operations
import os # Importing the os module for file operations


# Path to the directory containing training images
path = "./train/"

known_names = [] # List to store names of known individuals
known_name_encodings = [] # List to store face encodings of known individuals

# Get list of image files in the specified directory
images = os.listdir(path)

# Loop through each image file in the directory
for _ in images:
    image = fr.load_image_file(path + _) # Load the image using face_recognition library
    image_path = path + _
    encoding = fr.face_encodings(image)[0] # Extract face encoding (features) from the image

     # Append the face encoding to the list of known encodings
    known_name_encodings.append(encoding)
     # Extract the base name of the image (without extension) and capitalize for display
    known_names.append(os.path.splitext(os.path.basename(image_path))[0].capitalize())

print(known_names) # Display the list of known names after processing

test_image = "./test/test.jpg" # Path to the test image
image = cv2.imread(test_image) # Read the test image using OpenCV
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Locate faces in the test image
face_locations = fr.face_locations(image)
# Encode faces found in the test image
face_encodings = fr.face_encodings(image, face_locations)

# Loop through each face found in the test image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = fr.compare_faces(known_name_encodings, face_encoding)  # Compare face with known encodings
    name = ""

    # Calculate distances from the test face to all known faces
    face_distances = fr.face_distance(known_name_encodings, face_encoding)
    # Identify the index with the smallest distance (best match)
    best_match = np.argmin(face_distances)

    # If a match is found based on face distance
    if matches[best_match]:
        name = known_names[best_match] # Assign the name of the best matching known face

     # Draw a rectangle around the detected face
    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
     # Draw a filled rectangle for displaying the name label
    cv2.rectangle(image, (left, bottom - 15), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX # Font for displaying the name
    # Put text (name) on the image
    cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

# Display the resulting image with face recognition annotations
cv2.imshow("Output", image)
# Save the annotated image with recognized faces
cv2.imwrite("./result.jpg", image)
cv2.waitKey(0) # Wait for any key press to close the image display
cv2.destroyAllWindows() # Close all OpenCV windows
