# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:52:55 2024

@author: Morteza
"""

import cv2
import numpy as np
import ctypes

# Get the monitor resolution
user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Create a black image
image = np.zeros((height, width, 3), dtype=np.uint8)

# Define parameters for the dancing effect
num_columns = 50  # Number of columns
column_spacing = width // num_columns
amplitude = height // 2 - 50  # Maximum height variation
frequency = 0.1  # Frequency of height variation
duration = 60  # Duration of the animation in seconds

# Define the gradient colors for a rainbow effect
rainbow_colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]

# Create a video writer
out = cv2.VideoWriter('light_dancing_effect_fit_monitor.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

# Loop to create the animation frames
for t in np.arange(0, duration * 2 * np.pi, 0.1):
    # Clear the image
    image.fill(0)
    
    # Calculate the height of each column
    heights = [int(height / 2 + amplitude * np.sin(frequency * (t + i))) for i in range(num_columns)]
    
    # Draw the columns with rainbow colors
    for i in range(num_columns):
        x = i * column_spacing
        y1 = height
        y2 = heights[i]
        
        # Calculate the color for the current column based on the rainbow gradient
        color_index = int((i / num_columns) * len(rainbow_colors))
        color = rainbow_colors[color_index]
        
        cv2.rectangle(image, (x, y1), (x + column_spacing, y2), color, -1)
    
    # Write the frame to the video writer
    out.write(image)
    
    # Display the frame
    cv2.imshow('Light Dancing Effect', image)
    
    # Wait for a short duration (30ms)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the video writer and close the OpenCV window
out.release()
cv2.destroyAllWindows()
