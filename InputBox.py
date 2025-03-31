from pygame import pygame


class InputBox:
    def __init__(self, x, y, width, height, font, color, background_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.text = ""
        self.color = color
        self.background_color = background_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_color, self.rect)
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))