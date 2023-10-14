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


def vehicle_detection(img):
    pass

def vehicle_classification():
    pass

def simulation():
    pass

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
