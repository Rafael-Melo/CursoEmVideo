import pygame
pygame.init()
pygame.mixer.music.load('Olivia Rodrigo Good 4 U.mp3')
pygame.mixer.music.play()
# Wait for the music to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Limit the loop to 10 frames per second
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
