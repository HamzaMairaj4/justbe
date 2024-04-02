import cv2

# Step 1: Collect images and annotations (positive and negative samples)

# Step 2: Prepare data for training
# Create a text file containing paths to positive samples and corresponding annotations
# Create a text file containing paths to negative samples

# Step 3: Train the Haar cascade classifier
# Use the opencv_traincascade utility provided by OpenCV to train the classifier
# Example command:
# opencv_traincascade -data classifier -vec positive_samples.vec -bg negative_samples.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000 -numNeg 600 -w 20 -h 20 -featureType LBP

# Step 4: Test the trained classifier
# Load the trained classifier
classifier = cv2.CascadeClassifier('classifier/cascade.xml')

# Load an image
image = cv2.imread('test_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect turn arrows in the image
turn_arrows = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw bounding boxes around detected turn arrows
for (x, y, w, h) in turn_arrows:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the result

