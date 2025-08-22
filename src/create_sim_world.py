# create_sim_world.py
import cv2
import numpy as np

# Create a blank white world canvas: 500x500 pixels, 3 color channels (BGR)
world = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Define the goal (apple) position
goal_center = (400, 400)
goal_radius = 20

# Draw the goal (a red circle) on the world
# cv2.circle(image, center_coordinates, radius, color(B,G,R), thickness)
cv2.circle(world, goal_center, goal_radius, (0, 0, 255), -1)  # -1 fills the circle

# Draw the robot's start position (a blue circle)
start_center = (50, 250)
start_radius = 10
cv2.circle(world, start_center, start_radius, (255, 0, 0), -1)

# Save the generated image to the 'data' folder
cv2.imwrite('../data/simulated_world.png', world)

# (Optional) Display the image
cv2.imshow('Simulated World', world)
cv2.waitKey(0)
cv2.destroyAllWindows()