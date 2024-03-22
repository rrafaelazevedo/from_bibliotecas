import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ubuntu_tutu.mp3')
pygame.mixer.music.play()
pygame.event.wait()