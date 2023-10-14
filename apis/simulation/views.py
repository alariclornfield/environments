import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Define the traffic light status
traffic_light_status = {1: RED, 2: YELLOW, 3: GREEN}

# Create a screen
screen = pygame.display.set_mode((800, 600))

class Vehicle:
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

# Create some vehicles
vehicles = [Vehicle(random.choice(['car', 'truck', 'emergency']), random.randint(20, 60)) for _ in range(10)]

# Calculate vehicle counts
vehicle_counts = len(vehicles)

# Calculate vehicle types
vehicle_types = [vehicle.type for vehicle in vehicles]

# Calculate vehicle speeds
vehicle_speeds = [vehicle.speed for vehicle in vehicles]


def adjust_signal_duration(vehicle_counts, vehicle_types, vehicle_speeds):
    # Your function code here
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

    # Create a game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Randomly generate traffic density and traffic light status
        traffic_density = random.choice(['high', 'low'])
        light_status = random.choice([1, 2, 3])

        # Set the color based on traffic density
        color = RED if traffic_density == 'high' else GREEN

        # Fill the screen with the color
        screen.fill(color)

        # Draw the traffic light with its status color
        pygame.draw.circle(screen, traffic_light_status[light_status], (400, 300), 50)

        # Randomly generate vehicle data
        vehicle_counts = [random.randint(1, 10) for _ in range(4)]
        vehicle_types = [['average'] * count for count in vehicle_counts]
        vehicle_speeds = [random.randint(20, 60) for _ in range(4)]

        # Adjust signal durations based on vehicle data
        signal_durations = adjust_signal_duration(vehicle_counts, vehicle_types, vehicle_speeds)

        # Use signal_durations to adjust your traffic lights here

        # Update the display
        pygame.display.flip()

    pygame.quit()

adjust_signal_duration(vehicle_counts, vehicle_types, vehicle_speeds);
