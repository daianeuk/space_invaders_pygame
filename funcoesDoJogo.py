import sys
sys.path.append('C:\\Users\\CtrlPlay\\Desktop\\JogoFinal')
import pygame
from projetil import Bullet
from alienigena import Alien

def checa_eventos(configuracoesDoJogo, ship, screen, bullets, game_active, botaoPlay):
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                efeitoSonoro("C:\\Users\\CtrlPlay\\Desktop\\JogoFinal\\musicas\\laser.wav")
                novoProjetil = Bullet(configuracoesDoJogo, screen, ship)
                bullets.add(novoProjetil)
                
            if event.key == pygame.K_RIGHT:
                # Move a nave para direita
                if ship.rect.right < 1100:
                    ship.rect.centerx += 100
                    
            if event.key == pygame.K_LEFT:
                # Move a nave para esquerda
                if ship.rect.left > 100:
                    ship.rect.centerx -= 100

def check_play_button(botaoPlay):
    for event in pygame.event.get():
        # inicia um novo jogo quando o jogador clicar em Play
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if botaoPlay.rect.collidepoint(mouse_x, mouse_y):
                return True

def telaPlay(configuracoesDoJogo, screen, botaoPlay, telaInicial):
    # Cria com imagem de fundo e com um botão
        screen.fill(configuracoesDoJogo.bg_color_play)
        telaInicial.blitme()
        botaoPlay.draw_button()
        pygame.display.flip()
        
def atualiza_tela(configuracoesDoJogo, screen, ship, aliens, bullets, game_active, botaoPlay):
        # Atualiza as imagens na tela e alterna para uma nova tela
        screen.fill(configuracoesDoJogo.bg_color)
        for b in bullets.sprites():
            b.desenhaProjetil()
        # desenha a nave
        ship.blitme()
        
        # desenha a frota de alienígenas
        aliens.draw(screen)
                
        # deixa a tela mais recente visível
        pygame.display.flip()
        
def createFleet(configuracoesDoJogo, screen, aliens):
        configuracoesDoJogo.alien_speed_factor = configuracoesDoJogo.alien_speed_factor+0.1
        alien = Alien(configuracoesDoJogo, screen)
        # largura do alienígena
        alien_width = alien.rect.width
        # altura do alienígena
        alien_height = alien.rect.height
        # espaco disponível é igual a largura da tela menos um alienígena de cada lado
        espacoDisponivel = configuracoesDoJogo.screen_width - 2 * alien_width
        # espaco disponível Y é igual a altura da tela menos 3 alienígenas e a nave do jogador
        espacoDisponivelY = (configuracoesDoJogo.screen_height - (3 * alien_height))
        # número de linhas
        number_rows = int(espacoDisponivelY/(2 * alien_height))
        # número de naves da frota
        numeroDeAlienigenas = int(espacoDisponivel/(2*alien_width))
        
        for row_number in range(number_rows-1):
            for numero in range(numeroDeAlienigenas):
                alien = Alien(configuracoesDoJogo, screen)
                # posiciona os alienigenas um ao lado do outro
                alien.x = alien_width + 2 * alien_width * numero
                alien.rect.x = alien.rect.x + alien.x
                alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
                aliens.add(alien)

def checaFrotaNaBorda(configuracoesDoJogo, aliens):
    # responde no momento que um alienígena alcançou uma borda
    for alien in aliens.sprites():
        if alien.checaBordas():
            mudaDirecaoDaFrota(configuracoesDoJogo, aliens)
            break

def mudaDirecaoDaFrota(configuracoesDoJogo, aliens):
    #faz toda a frota descer e mudar a direção
    for alien in aliens.sprites():
        alien.rect.y += configuracoesDoJogo.fleet_drop_speed
    configuracoesDoJogo.fleet_direction *= -1
    
def atualizaAliens(configuracoesDoJogo, aliens):
    # verifica se a frota está em uma das bordas
    # e então atualiza a posição de todos os alienígenas da tropa
    checaFrotaNaBorda(configuracoesDoJogo, aliens)
    aliens.update()

def jogoAtivo(screen, aliens):
    # verifica se algum alienígena alcançou a parte inferior da tela
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom :
            return False
    return True

def tocaMusica(endereco):
    pygame.mixer.music.load(endereco)
    pygame.mixer.music.play(-1)
    
def efeitoSonoro(endereco):
    som = pygame.mixer.Sound(endereco)
    som.set_volume(1)
    som.play()