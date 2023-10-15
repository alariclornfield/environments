# implemtation of a traffic light management system

import lights

"""
    Imports related to Image Processing and Numerical Operations.
"""
import cv2 as cv2
import numpy as np

"""
    Imports related to simulation
"""
import pygame as game


# Function for vehicle detection using YOLO
def vehicle_detection_yolo(img_path):
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")  # Provide the correct paths
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Load image
    img = cv2.imread(img_path)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Information to return
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    return class_ids, confidences, boxes


def vehicle_classification(class_ids, confidences):
    vehicle_types = []

    # Define your classification criteria here
    for i, class_id in enumerate(class_ids):
        confidence = confidences[i]

        # Example: If class_id is 0 (car) and confidence is high, classify as 'car'
        if class_id == 0 and confidence > 0.7:
            vehicle_types.append('car')
        # Add more conditions for other types of vehicles

    return vehicle_types
    
def simulation():
    # Initialize pygame
    game.init()

    # Set up the simulation window
    window_size = (800, 600)
    screen = game.display.set_mode(window_size)
    game.display.set_caption('Traffic Light Simulation')

    # Define colors
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)

    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False

        # Draw traffic lights
        # Red light
        game.draw.circle(screen, RED, (200, 150), 30)
        # Yellow light
        game.draw.circle(screen, YELLOW, (200, 250), 30)
        # Green light
        game.draw.circle(screen, GREEN, (200, 350), 30)

        # Update the display
        game.display.flip()

    game.quit()
    
# def adjust_signal_duration(vehicle_counts, vehicle_types):
#     # Define weights for different types of vehicles
#     weights = {'emergency': 5, 'truck': 2, 'slow': 1, 'average': 1}

#     # Calculate the weighted count of vehicles in each lane
#     weighted_counts = [sum(weights[type] for type in types) for types in vehicle_types]

#     # Calculate the total weighted count
#     total_weighted_count = sum(weighted_counts)

#     # Calculate the proportion of vehicles in each lane
#     proportions = [count / total_weighted_count for count in weighted_counts]

#     # Define a base duration for your traffic signals (in seconds)
#     base_duration = 60

#     # Adjust the signal duration for each lane based on the proportion of vehicles
#     signal_durations = [base_duration * proportion for proportion in proportions]

#     return signal_durations

def adjust_signal_duration(vehicle_counts, vehicle_types, vehicle_speeds):
    # Define weights for different types of vehicles
    weights = {'emergency': 5, 'truck': 2, 'slow': 1, 'average': 1}

    # Calculate the weighted count of vehicles in each lane
    weighted_counts = [sum(weights[type] for type in types) for types in vehicle_types]

    # Adjust the counts based on average vehicle speed
    adjusted_counts = [count * (60 / speed) for count, speed in zip(weighted_counts, vehicle_speeds)]

    # Calculate the total adjusted count
    total_adjusted_count = sum(adjusted_counts)

    # Calculate the proportion of vehicles in each lane
    proportions = [count / total_adjusted_count for count in adjusted_counts]

    # Define a base duration for your traffic signals (in seconds)
    base_duration = 60

    # Adjust the signal duration for each lane based on the proportion of vehicles
    signal_durations = [base_duration * proportion for proportion in proportions]

    # Decrease signal duration for any lane with an emergency vehicle
    for i, types in enumerate(vehicle_types):
        if 'emergency' in types:
            signal_durations[i] -= 30

    return signal_durations


adjust_signal_duration(vehicle_counts=vehicle_detection(img=""), vehicle_types=vehicle_classification(), vehicle_speeds="")
