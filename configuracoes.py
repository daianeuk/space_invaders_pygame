class Settings():

    def __init__(self):
        # largura
        self.screen_width = 1200
        # altura
        self.screen_height = 600
        # cor de fundo
        self.bg_color = (230, 230, 230)
        # cor de fundo tela inicial
        self.bg_color_play = (255, 255, 255)
        
        # configurando projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250, 0, 0
        
        # configurações dos alienígenas
        # velocidade
        self.alien_speed_factor = 1
        # velocidade que a tropa desce
        self.fleet_drop_speed = 20
        # fleet_direction igual a 1 representa direita;
        # -1 representa a esquerda
        self.fleet_direction = 1
        