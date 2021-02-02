import pygame

class imageScreen():
    
    # inicializa a nave e coloca sua posição inicial
    def __init__(self, screen, endereco):
        
        # carregando a tela do jogo        
        self.screen = screen
        # carregando imagem para tela
        self.image = pygame.image.load(endereco)
        
        # coletando o retângulo da imagem e da tela
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # coincidindo a posição central da imagem com posição central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        # desenha a imagem na posicao atual
        self.screen.blit(self.image, self.rect)
            
            
            