import cv2
import mediapipe as mp
import numpy as np
import pygame
import random
import time

# Initialize pygame for sound
pygame.mixer.init()

# Function to generate beep sound
def generate_beep(frequency=1000, duration=300):
    sample_rate = pygame.mixer.get_init()[0]
    t = np.linspace(0, duration / 1000, int(sample_rate * duration / 1000), endpoint=False)
    
    # Create a sine wave
    sound_wave = np.sin(2 * np.pi * frequency * t)
    
    # Convert to 16-bit PCM format (values between -32767 and 32767)
    sound_wave = np.int16(sound_wave * 32767)
    
    # Make the array 2D (for stereo), by repeating the sound wave for both channels
    stereo_wave = np.column_stack((sound_wave, sound_wave))

    # Create the sound object
    beep = pygame.mixer.Sound(stereo_wave)
    return beep

# Initialize mediapipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

# Set up the webcam
cap = cv2.VideoCapture(0)

# Ball properties
ball_radius = 30
ball_x = random.randint(ball_radius, 640 - ball_radius)
ball_y = -ball_radius
ball_speed = 5

# Game variables
score = 0
game_over = False

# Define the game window size
screen_width = 640
screen_height = 480

# Generate beep sound
catch_beep = generate_beep()

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to capture frame.")
        break

    # Flip the frame horizontally and convert to RGB for mediapipe
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    result = hands.process(rgb_frame)

    # Draw the falling ball
    if not game_over:
        cv2.circle(frame, (ball_x, ball_y), ball_radius, (0, 0, 255), -1)

        # Move the ball down
        ball_y += ball_speed

        # Reset the ball position if it goes off-screen
        if ball_y > screen_height:
            ball_x = random.randint(ball_radius, screen_width - ball_radius)
            ball_y = -ball_radius

        # Check for hand landmarks
        if result.multi_hand_landmarks:
            for landmarks in result.multi_hand_landmarks:
                # Get the position of the wrist (landmark 0)
                wrist_x = int(landmarks.landmark[mp_hands.HandLandmark.WRIST].x * screen_width)
                wrist_y = int(landmarks.landmark[mp_hands.HandLandmark.WRIST].y * screen_height)

                # Draw the hand landmarks and wrist
                for landmark in landmarks.landmark:
                    x = int(landmark.x * screen_width)
                    y = int(landmark.y * screen_height)
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

                # Check if the ball collides with the hand
                distance = np.sqrt((ball_x - wrist_x) ** 2 + (ball_y - wrist_y) ** 2)
                if distance < ball_radius:
                    score += 1
                    ball_x = random.randint(ball_radius, screen_width - ball_radius)
                    ball_y = -ball_radius
                    catch_beep.play()  # Play the beep sound when ball is caught
                    print(f"Score: {score}")

        # Display the score on the screen
        cv2.putText(frame, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Check for exit condition (press 'q' to quit)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Show the game window
        cv2.imshow("Hand Tracking Game", frame)

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
