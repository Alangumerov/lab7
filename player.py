#2 Create music player with keyboard controller. You have to be able to press keyboard: play, stop, next and previous as some keys. Player has to react to the given command appropriately.
import pygame
import os
pygame.init()
#дисплей создание
WIDTH, HEIGHT = 800, 600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.mixer.init()
MUSIC_FOLDER="music"
tracks=[f for f in os.listdir(MUSIC_FOLDER) if f.endswith(('.mp3', '.wav'))]
#условие если ничего не играет
if not tracks:
    raise FileNotFoundError("Ошибка")
current_track=0
paused=False
playing=False
#создание функций
def play(index):
    global paused
    paused=False
    playing=True
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[index]))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
    playing=False
def next():
    global current_track
    current_track=current_track+1
    play(current_track)

def previous():
    global current_track
    current_track=current_track-1
    play(current_track)
def pause():
    global paused, playing
    if pygame.mixer.music.get_busy():
        if paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        paused=not paused
    elif not playing:
        play(current_track)

play(current_track)
running=True
while running:
    #управление
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
          running=False
      elif event.type==pygame.KEYDOWN:
          if event.key==pygame.K_SPACE:
              pause()
          elif event.key==pygame.K_s:
              stop()
          elif event.key==pygame.K_n:
              next()
          elif event.key==pygame.K_p:
              previous()
pygame.quit()
