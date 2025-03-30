#1 Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds.
import pygame
import time


pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
BG_COLOR = (255, 255, 255)


clock_face = pygame.image.load('images/photo_5373113437619612369_x.jpg')  # Загружаем изображение циферблата
hand_for_minutes = pygame.image.load('images/photo_5373113437619612371_x-removebg-preview.png')  # Загружаем минутную стрелку
hand_for_seconds = pygame.image.load('images/photo_5373113437619612372_x-removebg-preview.png')  # Загружаем секундную стрелку


clock_face = pygame.transform.scale(clock_face, (800, 600))


screen = pygame.display.set_mode((800, 600))


def rotate_image(image, angle, position):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=position)
    return rotated_image, new_rect

def main():
    running = True
    while running:
        screen.fill(BG_COLOR)
        screen.blit(clock_face, (0, 0))

        t = time.localtime()
        minutes = t.tm_min
        seconds = t.tm_sec


        min_angle = -(minutes * 6) - 90
        sec_angle = -(seconds * 6) - 90


        min_hand, min_rect = rotate_image(hand_for_minutes, min_angle, CENTER)
        sec_hand, sec_rect = rotate_image(hand_for_seconds, sec_angle, CENTER)


        screen.blit(min_hand, min_rect)
        screen.blit(sec_hand, sec_rect)

        pygame.display.flip()



if __name__ == "__main__":
    main()
