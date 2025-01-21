import cv2
import dlib

# Initialize dlib's face detector (HOG-based)
face_detector = dlib.get_frontal_face_detector()

# Initialize OpenCV's pre-trained eye detector (Haar Cascade)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize video capture (0 is the default camera)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert frame to grayscale (necessary for the detector)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_detector(gray)

    # Initialize a counter for eyes
    total_eyes = 0

    # Iterate over each detected face
    for face in faces:
        # Get the coordinates of the face rectangle
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Detect eyes within the face region using the eye cascade
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Count the number of eyes detected
        eye_count = len(eyes)
        total_eyes += eye_count

        # Draw rectangles around detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

    # Display the count of eyes on the frame
    cv2.putText(frame, f'Total Eyes Detected: {total_eyes}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Eye Detection and Counting', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()