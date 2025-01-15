import cv2
import numpy as np


#define color boundaries is HSV space
color_boundaries = {
    'red':([0,120,70],[10,255,255]),
    'green':([40,40,40],[90,255,255]),
    'blue':([100,150,0],[10,255,255]),
    'yellow':([20,100,100],[30,255,255]),
    'black':([0,0,0],[180,255,30]),  #Low saturation and brightness
    'white':([0,0,200],[180,20,255]), #High brightness, low saturation
    'gray':([0,0,40],[100,20,200]) #Moderate brighness, low saturation
}

def detect_color(frame):
    """Detect the dominant color in the frame"""
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Loop through each color boundary and check for matches
    for color, (lower, upper) in color_boundaries.items():
        lower_bound = np.array(lower)
        upper_bound = np.array(upper)
        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

        #if there in a signifiant match, return the color
        if cv2.countNonZero(mask) > 500: #Adjust this threshold as needed
            return color
    return 'None'

#Load the input image
image_path ="C:/Users/Priyanka B/Desktop/color/peal.jpg.jpg"  #Replace with your image file path
frame = cv2.imread(image_path)

if frame is None:
    print("Error: Could not read the image.")
else:
    #Detect the dominant color in the image
    detected_color = detect_color(frame)
    print(f"Detected Color: {detected_color}")

    #Display the detected color on the image
    cv2.putText(frame, f"[detected _color]",(10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 50, 0)),

    #Show the image with the detected color
    cv2.imshow("Color Detection", frame)

    #Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyA11Windows()

                
