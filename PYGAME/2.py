import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Music_player')
icon = pygame.image.load('Icon/icons.png')
pygame.display.set_icon(icon)
player = pygame.image.load('Icon/carous1.png')

music_sound = [
    pygame.mixer.Sound('Icon/rain.mp3'),
    pygame.mixer.Sound('Icon/adai.mp3'),
    pygame.mixer.Sound('Icon/ik.mp3')
]

selected_sound_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                music_sound[selected_sound_index].play()
            elif event.key == pygame.K_DOWN:
                music_sound[selected_sound_index].stop()
            elif event.key == pygame.K_LEFT:
                selected_sound_index = (selected_sound_index - 1) % len(music_sound)
            elif event.key == pygame.K_RIGHT:
                selected_sound_index = (selected_sound_index + 1) % len(music_sound)

    screen.blit(player, (0, 0))
    pygame.display.update()