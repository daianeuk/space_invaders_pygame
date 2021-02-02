import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, configuracoesDoJogo, screen, ship):
        # Cria um objeto projétil na posição atual da nave
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Cria um retângulo para o projétil em (0, 0) e 
        # depois define a posição correta
        self.rect = pygame.Rect(0, 0, configuracoesDoJogo.bullet_width, 
                                configuracoesDoJogo.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)
        
        # cor do projétil
        self.color = configuracoesDoJogo.bullet_color
        # velocidade da bala
        self.speed_factor = configuracoesDoJogo.bullet_speed_factor
        
    def update(self):
        # Move o projétil para cima
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def desenhaProjetil(self):
        # desenha o projétil na tela
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    
    