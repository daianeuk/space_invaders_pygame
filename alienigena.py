import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, configuracoesDoJogo, screen):
        # inicializa o alienígena e o posiciona na tela
        super(Alien, self).__init__()
        self.screen = screen
        self.configuracoesDoJogo = configuracoesDoJogo
        
        # carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('C:\\Users\\CtrlPlay\\Desktop\\JogoFinal\\imagens\\alien.bmp')
        self.rect = self.image.get_rect()
        
        # Inicia o alienígena próximo à parte superior 
        # da tela em uma posicao aleatória dentro do intervalo que o jogador se movimenta
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # armazena a posição exata do alienígena
        self.x = float(self.rect.x)
        
    def blitme(self):
        # desenha o alienígena em sua posição atual
        self.screen.blit(self.image, self.rect)
        
    def checaBordas(self):
        # retorna True se um alienígena estiver na borda da tela
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
            
    def update(self):
        # move o alienígena para a direita ou para esquerda
        self.x += (self.configuracoesDoJogo.alien_speed_factor * 
                    self.configuracoesDoJogo.fleet_direction)
        self.rect.x = self.x