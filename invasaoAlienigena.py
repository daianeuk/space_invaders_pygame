import sys
sys.path.append('C:\\Users\\CtrlPlay\\Desktop\\JogoFinal')

import pygame
import funcoesDoJogo as funcoes
from configuracoes import Settings
from nave import Ship
from pygame.sprite import Group
from botao import Button
from imagemTela import imageScreen

def run_game():

    pygame.init()
    configuracoesDoJogo = Settings()

    screen = pygame.display.set_mode(
        (configuracoesDoJogo.screen_width, configuracoesDoJogo.screen_height))
    pygame.display.set_caption("Invasao alienígena")

    # Cria botão Play
    botaoPlay = Button(configuracoesDoJogo, screen, "Play")

    # Cria a nave
    ship = Ship(screen)
    # Cria grupo de projeteis
    bullets = Group()
    # Cria grupo de alienigenas
    aliens = Group()

    # Cria frota de alienigenas
    funcoes.createFleet(configuracoesDoJogo, screen, aliens)

    game_active = False
    funcoes.tocaMusica("C:\\Users\\CtrlPlay\\Desktop\\JogoFinal\\musicas\\musica.mp3")
    while True:
        funcoes.checa_eventos(configuracoesDoJogo, ship, screen, bullets, game_active, botaoPlay)
        if game_active and len(aliens)>0:
            funcoes.atualiza_tela(configuracoesDoJogo, screen, ship, aliens, bullets, game_active,botaoPlay)
            qtdAliens = len(aliens)
            pygame.sprite.groupcollide(bullets, aliens, True, True)
            if qtdAliens > len(aliens):
                funcoes.efeitoSonoro("C:\\Users\\CtrlPlay\\Desktop\\JogoFinal\\musicas\\boom.wav")
            bullets.update()
            funcoes.atualizaAliens(configuracoesDoJogo, aliens)
            game_active = funcoes.jogoAtivo(screen, aliens)
        elif game_active and len(aliens)==0:
            funcoes.createFleet(configuracoesDoJogo, screen, aliens)
        elif not game_active:
            pygame.time.wait(2000)
            aliens.empty()
            bullets.empty()
            funcoes.createFleet(configuracoesDoJogo, screen, aliens)
            imagemTela = imageScreen(screen, "C:\\Users\\CtrlPlay\\Desktop\\JogoFinal\\imagens\\telaInicial.png")
            funcoes.telaPlay(configuracoesDoJogo, screen, botaoPlay, imagemTela)
            game_active = funcoes.check_play_button(botaoPlay)
run_game()
