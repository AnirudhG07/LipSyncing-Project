from LS_only_metaphone import linearize, display_metaword
import pyttsx3
import pygame
from pygame import mixer
import sys, os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

# Display setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image and Sound Viewer")

# Clock
clock = pygame.time.Clock()

# Placeholder function to display images
def display_images(sent):
    # Your image displaying logic goes here
    # For example:
    meta_sent=linearize(sent)
    display_metaword(meta_sent)

# Placeholder function to play sound
def play_sound(sent):
    # Your sound playing logic goes here
    # For example:
    from gtts import gTTS
    import timeit, playsound

    tts = gTTS(text=sent, lang='en')
    start=timeit.default_timer()
    tts.save("gtts_sentence.mp3")
    stop=timeit.default_timer()
    print(stop-start)
    # Play the audio using the playsound library
    playsound.playsound("gtts_sentence.mp3")
    
input_sent=input("PLs enter a sentence: ")

# Main application loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Call the display_images function
    display_images(input_sent)

    # Call the play_sound function
    play_sound(input_sent)
    os.remove("gtts_sentence.mp3")

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)
