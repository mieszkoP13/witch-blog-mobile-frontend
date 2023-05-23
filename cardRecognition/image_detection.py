import cv2
import os


def delete_files_in_directory(directory):
    file_list = os.listdir(directory)
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


delete_files_in_directory('detectedCards')

cards_to_detect = int(input("Enter the number of cards to scan: "))


# Load the input image
image = cv2.imread("images/1.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection to detect the contours of the tarot cards
edges = cv2.Canny(gray, 50, 150)

# Find contours in the edge image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort the contours based on their areas in descending order
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Extract the three contours with the largest areas
top_contours = contours[:cards_to_detect]

# Extract the tarot card images from the original image using the contours
extracted_images = []
for i, contour in enumerate(top_contours):
    x, y, w, h = cv2.boundingRect(contour)
    tarot_card_image = image[y:y+h, x:x+w]

    # Check dimensions and rotate if necessary
    if h < w:
        rotated_image = cv2.rotate(tarot_card_image, cv2.ROTATE_90_CLOCKWISE)
        extracted_images.append(rotated_image)
        # Save the rotated tarot card image
        cv2.imwrite(f"detectedCards/tarot_card_{i}.jpg", rotated_image)
    else:
        extracted_images.append(tarot_card_image)
        # Save the tarot card image as is
        cv2.imwrite(f"detectedCards/tarot_card_{i}.jpg", tarot_card_image)