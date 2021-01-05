import pygame
import random
import sys

# Definir as cores
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 200, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
# Cores das  Plataformas: MARRON, DARK GREEN, CHOCOLATE, SIENNA, BROWN, SADDLEWBROWN, GREEN and DARK GRAY
PLAT_COLORS = [(128, 0, 0), (20, 115, 20), (210, 105, 30), (160, 82, 45), (165, 42, 42), (139, 69, 190), (0, 255, 0), (27, 24, 25)]

# Inicializa o Pygame
pygame.init()

# Ajusta a altura e largura da screen(tela).
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption('Ribanceira')


uiFont = pygame.font.Font("Fonts/retro.ttf", 25)

# Clock para gerenciar os updates
clock = pygame.time.Clock()

pause = False


def QuitGame():
    """ Desliga o jogo"""
    print("Fim da Apresentação. Obrigado!")
    pygame.quit()
    sys.exit()
    

def text_objects(text, font, COLOR):
    textSurface = font.render(text, True, COLOR)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("Fonts/CHILLER.TTF", 18)
    textSurf, textRect = text_objects(msg, smallText, BLACK)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    
def show_InicialScreenSenac():
    """
    Mostra Tela Inicial
    """
    pygame.mixer.music.load('Sounds/splash.ogg')
    pygame.mixer.music.play()

    # Fade na imagem devagar.
    splash = pygame.image.load("assets/Senac.png").convert()
    for i in range(24):
        splash.set_alpha(i)
        screen.blit(splash, (200, 200))
        pygame.display.update()
        pygame.time.wait(100)
        

    pygame.mixer.fadeout(2000)
    splash.set_alpha(0)
    screen.blit(splash, (200, 200))
    pygame.display.update()
    pygame.time.wait(1200)


def show_InicialScreenPesadao():
    """
    Mostra Tela Inicial
    """
    screen.fill(WHITE)
    pygame.display.update()

    # Fade na imagem devagar.
    pesado = pygame.image.load("assets/pesadao.jpg").convert()
    pygame.mixer.music.load('Sounds/pesadao.wav')
    pygame.mixer.music.play()
    for i in range(27):
        pesado.set_alpha(i)
        screen.blit(pesado, (220, 200))
        pygame.display.update()
        pygame.time.wait(100)

    pygame.mixer.fadeout(2200)
    screen.blit(pesado, (220, 200))
    pygame.display.update()
    pygame.time.wait(1300)

def show_CreditsScreen():
    """
    Mostra Tela de Créditos
    """
    global start_level
    start_level = 1
    
    pygame.mixer.music.load('Sounds/Japanese.ogg')
    pygame.mixer.music.play()

    # Fade na imagem devagar.
    splash = pygame.image.load("assets/Creditos_finalizado.png").convert()
    for i in range(30):
        splash.set_alpha(i)
        screen.blit(splash, (0, 0))
        pygame.display.update()
        pygame.time.wait(100)

    pygame.mixer.fadeout(2000)
    screen.blit(splash, (0, 0))
    pygame.display.update()
    pygame.time.wait(2500)
    return TitleIntro()


def TitleIntro():
    pygame.mixer.stop()

    global done
    done = True
    pause = False
    gameOver = False
    global start_level
    start_level = 1

    #musica
    titleLevel = Level(start_level)
    titleLevel.themeMusic.stop()
    titleLevel.level_music.stop()

    titleLevel.themeMusic.play()

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
        # Define Imagem de Fundo
        background_image = pygame.image.load("Assets/forest.png")
        screen.blit(background_image, [0, 0])

        # Escreve o Texto Citado na Janela Criada
        largeText = pygame.font.Font('Fonts/COLONNA.ttf', 120)
        TextSurf, TextRect = text_objects("Ribanceira", largeText, BLACK)
        TextRect.center = ((screen_width / 2), (screen_height / 8))
        screen.blit(TextSurf, TextRect)

        # Se o mouse estiver acima do botão ele muda a cor senão mantém a cor original
        # Define o Botão Verde
        button("Jogar", 350, 350, 120, 60, GREEN, PLAT_COLORS[2], Main)

        # Define o Botão Vermelho
        button("Sair", 695, 550, 75, 40, RED, PLAT_COLORS[3], QuitGame)

        pygame.display.update()
        clock.tick(45)
        pygame.display.flip()

def Paused():

    largeText = pygame.font.Font('Fonts/retro.ttf', 125)
    TextSurf, TextRect = text_objects("Paused", largeText, BLACK)
    TextRect.center = ((screen_width/2), (screen_height/2))


    while pause == True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                QuitGame()

        screen.fill(WHITE)
        screen.blit(TextSurf, TextRect)

        button("Continue", 150, 450, 100, 50, GREEN, PLAT_COLORS[2], UnPaused)
        
        button("Menu", 550, 450, 100, 50, RED, PLAT_COLORS[3], TitleIntro)

        pygame.display.update()
        clock.tick(25)
        
def StartLevelScreen():

    largeText = pygame.font.Font('Fonts/comicz.ttf', 125)
    TextSurf, TextRect = text_objects("Level "+ str(int(start_level)), largeText, BLACK)
    TextRect.center = ((screen_width/2), (screen_height/2))

    while pause == True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                QuitGame()

        screen.fill(WHITE)
        screen.blit(TextSurf, TextRect)

        button("Continuar", 150, 450, 100, 50, GREEN, PLAT_COLORS[2], Main)
        
        button("Menu", 550, 450, 100, 50, RED, PLAT_COLORS[3], TitleIntro)

        pygame.display.update()
        clock.tick(25)

def GameOver():
    pygame.mixer.stop()

    # Define Imagem de Fundo e Musica
    background_image2 = pygame.image.load("Assets/gameOver.png")
    screen.blit(background_image2, [0, 0])
    gameOver = True
    gameOverMusic = pygame.mixer.Sound("Sounds/Nevermore.ogg")
    gameOverMusic.play()

    global start_level
    start_level = 1


    while gameOver == True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                QuitGame()

        #screen.fill(BLACK)
        #screen.blit(TextSurf, TextRect)

        button("Recomeçar", 150, 450, 100, 50, GREEN, PLAT_COLORS[2], Main)
        
        button("Menu", 550, 450, 100, 50, RED, PLAT_COLORS[3], TitleIntro)

        pygame.display.update()
        clock.tick(25)


def UnPaused():
    global pause
    pause = False


class Lists(pygame.sprite.Group):
    def __init__(self):
        super().__init__(self, )
        # Aqui é a lista dos 'sprites.' Cada item no programa está
        # adicionado nesta lista. A lista é gerenciada pela class  'Group.'

        self.block_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()
        self.ammo_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.bigPlatform_list = pygame.sprite.Group()
        # Lista de todos sprites.
        self.all_sprites_list = pygame.sprite.Group()

        # Lista das bullets (balas)
        self.bullet_list = pygame.sprite.Group()

class Abs(pygame.sprite.Sprite):
    """
    Define a classe principal abstrata da hierarquia, serve de base para as outras classes de
    "Sprite" no Pygame
    """
    def __init__(self, color, width, height):
        """ Construtor. Passa cores e posições em x e y. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Cria a imagem od objeto, com uma cor.
        self.image = pygame.Surface([width, height])
        self.image = pygame.transform.scale(self.image, ([width, height]))

        # Update da posição desse objecto feita por valores
        # de rect.x and rect.y
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ Reseta a posição to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = 275
        self.rect.x = random.randrange(35, 65)

    def update(self):
        """ Chama cada frame. """
        self.change_x = 0
        self.change_y = 3.8


        # Move  para cima
        self.rect.y -= self.change_y

        # Se o block estiver muito alto, reseta ele.
        if self.rect.y < -2:
            self.reset_pos()


class Level:
    """
    Classe Genérica para definir os levels/níveis
    """

    def __init__(self, start_level):
        self.themeMusic = pygame.mixer.Sound("Sounds/Music0.ogg")
        self.level = start_level
        self.level_music_1 = pygame.mixer.Sound("Sounds/Music1.ogg")
        self.block_level = 12
        self.platform_level = 10
        self.bigPlatform_level = 1
        self.level_music = self.level_music_1
        self.init_x = 275
        self.init_y = 70

        if self.level == 3:
            self.block_level = 18
            self.platform_level = 10
            self.bigPlatform_level = 1
            self.level_music = pygame.mixer.Sound("Sounds/Music3.ogg")
            self.init_x = 275
            self.init_y = 70

        if self.level == 2:
            self.block_level = 16
            self.platform_level = 12
            self.bigPlatform_level = 1
            self.level_music = pygame.mixer.Sound("Sounds/Music2.ogg")
            self.init_x = 275
            self.init_y = 7


class Block(Abs):
    """
    Define os inimigos 
    """

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__(color, width, height)

        # Imagem, cor e sprites para serem carregados.
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("Assets/Fireguy.png").convert()
        self.image = pygame.transform.scale(self.image, ([width, height]))
        self.image.set_colorkey(BLACK)

        self.dead_sound = pygame.mixer.Sound("Sounds/hit.wav")
        self.dead_sound.set_volume(0.75)

        # Update da posição desse objecto feita por valores
        # de rect.x and rect.y
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ Reseta a posição to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(610, 10, -600)
        self.rect.x = random.randrange(0, screen_width - 100)


class Platform(Abs):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__(color, width, height)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.dead_sound = pygame.mixer.Sound("Sounds/crush.ogg")
        self.dead_sound.set_volume(0.40)

    def reset_pos(self):
        self.rect.y = random.randrange(610, 10, -600)
        self.rect.x = random.randrange(0, screen_width - 50)

    def update(self):
        """ Called each frame. """
        self.change_x = 0
        self.change_y = 2.8

        # Move a plataforma para cima
        self.rect.y -= self.change_y

        # Se a plataforma estiver muito alto, reseta ela.
        if self.rect.y < -10:
            self.reset_pos()


class Ammo(Abs):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__(color, width, height)
        self.image = pygame.image.load("Assets/Ammo2.png").convert()
        self.image = pygame.transform.scale(self.image, ([width, height]))
        self.image.set_colorkey(BLACK)
        self.change_x = 0
        self.change_y = 0

        self.get_sound = pygame.mixer.Sound("Sounds/reload.wav")
        self.get_sound.set_volume(0.71)

    def reset_pos(self):
        self.rect.y = random.randrange(610, 10, -600)
        self.rect.x = random.randrange(0, screen_width - 50)

    def update(self):
        """ Chama cada frame. """
        self.change_x = 0
        self.change_y = 4.8

        # Move a plataforma para cima
        self.rect.y -= self.change_y

        # Se a plataforma estiver muito alto, reseta ela.
        if self.rect.y < -10:
            self.reset_pos()


class Player(Abs):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.image0 = pygame.image.load("Assets/carrito0.png").convert()
        self.imagem = pygame.image.load("Assets/carrito.png").convert()
        self.image = self.imagem
        self.image1 = pygame.image.load("Assets/carrito1.png").convert()
        self.image = pygame.transform.scale(self.image, ([width, height]))
        self.change_x = 0
        self.change_y = 0
        self.acc = 1
        self.image.set_colorkey(BLACK)
        self.imagem.set_colorkey(BLACK)
        self.image0.set_colorkey(BLACK)
        self.image1.set_colorkey(BLACK)

        self.life = 20
        self.nitro = 5
        self.shot_jet = False

        self.dash_sound = pygame.mixer.Sound("Sounds/dash.ogg")
        self.dash_sound.set_volume(0.55)
        self.danger_sound = pygame.mixer.Sound("Sounds/fausto.wav")
        self.danger_sound.set_volume(0.85)
        self.dangerIsActive = False
        self.imagemDanger = pygame.image.load("Assets/fausto.jpg").convert()
        self.imagemDanger.set_colorkey(BLACK)
        self.imagemDanger = pygame.transform.scale(self.imagemDanger,([width, height]))

    def update(self):
        self.change_y = self.acc
        if self.shot_jet == True:
            self.acc = -20
        else:
            self.acc = 1

        self.rect.x += self.change_x
        self.rect.y += self.change_y - 1


    # Player-controlled movement:

    def go_left(self, width, height):
        self.change_x = -6

        self.image = self.imagem
        self.image = pygame.transform.scale(self.image, ([width, height]))

    def go_right(self, width, height):
        self.change_x = 6
        self.image = self.image0
        self.image = pygame.transform.scale(self.image, ([width, height]))

    def go_down(self, width, height):
        self.image = self.image1
        self.rect.y = self.rect.y + 80
        self.image = pygame.transform.scale(self.image, ([width, height]))

    def stop_downDash(self, width, height):
        self.image = self.imagem
        self.rect.y = self.rect.y + self.acc
        self.image = pygame.transform.scale(self.image, ([width, height]))

    def stop(self):
        self.change_x = 0


class Bullet(Abs):
    """ Essa classe representa a bullet/bala. """

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__(color,width, height)
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load("Assets/Bullet.png")
        self.image = pygame.transform.scale(self.image, ([width, height]))
        self.image.set_colorkey(color)

        self.shot_sound = pygame.mixer.Sound("Sounds/laser5.ogg")
        self.shot_sound.set_volume(0.71)
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y += 20
        self.change_y = 0
        # Set speed vector of player
        self.change_x = 0
        self.change_y = - 20

def Main():

    global start_level
    pygame.mixer.stop()
    current_lvl = Level(start_level)

    background = pygame.image.load("Assets/background.png").convert()
    background_position = [(1 - start_level)*(470), -start_level]

    global pause

    for counter in range(20):
        pygame.time.wait(20)

    current_lvl.level_music.play()

    # --- Sprite - Listas  ---

    listas = Lists()


    for i in range(current_lvl.block_level):
        # Aqui se representa o block/inimigo
        block = Block(RED, 24, 32)

        # As posições randomicas dos blocks
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(screen_height)

        # Adicionar o block na lista de objetos
        listas.block_list.add(block)
        listas.all_sprites_list.add(block)

    # Criar um Player
    playerWidth = 72
    playerHeight = 68
    player = Player(BLUE, playerWidth, playerHeight)
    listas.player_list.add(player)
    listas.all_sprites_list.add(player)
    player.nitro = player.nitro + start_level -1

    # Criar um Plataformas
    for p in range(current_lvl.platform_level):
        # This represents a platforma padrão
        platform = Platform(PLAT_COLORS[random.randint(0, 4)], random.randint(30, 75), random.randint(6, 20))
        # Coloca as plataformas em localizações randomicas
        platform.rect.x = random.randrange(screen_width)
        platform.rect.y = random.randrange(screen_height)

        # Adiciona o block/inimigo na lista dos objetos
        listas.platform_list.add(platform)
        listas.all_sprites_list.add(platform)

    for bp in range(current_lvl.bigPlatform_level):
        # This represents a platforma grande
        bigPlatform = Platform(PLAT_COLORS[random.randint(5, 6)], random.randint(470, 515), random.randint(8, 22))
        # Coloca as plataformas em localizações randomicas
        bigPlatform.rect.x = random.randrange(screen_width)
        bigPlatform.rect.y = random.randrange(screen_height)

        # Adiciona o block/inimigo na lista dos objetos
        listas.bigPlatform_list.add(bigPlatform)
        listas.all_sprites_list.add(bigPlatform)

    # Criar Municao
    for m in range(3 + current_lvl.level):
        # This represents a platform
        ammo = Ammo(YELLOW, 62, 40)
        # as ammo em localizações randomicas
        ammo.rect.x = random.randrange(screen_width)
        ammo.rect.y = random.randrange(screen_height)

        # Adiciona o block/inimigo na lista dos objetos
        listas.ammo_list.add(ammo)
        listas.all_sprites_list.add(ammo)

    # Loop até o Game Over ou o User clickar no close.
    global done
    done = False
    

    score = 0
    pente = 10
    bullet = Bullet(BLACK, 10, 20)
    player_lifeColor = CYAN

    player.shot_jet = False

    player.rect.y = current_lvl.init_x
    player.rect.x = current_lvl.init_y

    # -------- Main Program Loop -----------

    while not done:
        player.shot_jet = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()

            if player.life <= 0:
                done = True
                GameOver()

            if event.type == pygame.KEYDOWN and pente > 0:
                if event.key == pygame.K_COMMA or event.key == pygame.K_z:
                    # Fire a bullet if the user clicks the mouse button
                    
                    player.shot_jet = True
                    bullet.shot_sound.play()
                    pente -= 1
                    # Set the bullet so it is where the player is
                    bullet.rect.x = player.rect.x + 35
                    bullet.rect.y = player.rect.y + 35
                    # Add the bullet to the lists
                    listas.all_sprites_list.add(bullet)
                    listas.bullet_list.add(bullet)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left(playerWidth, playerHeight)
                if event.key == pygame.K_RIGHT:
                    player.go_right(playerWidth, playerHeight)
                if event.key == pygame.K_DOWN and player.nitro > 0:
                    player.go_down(playerWidth, playerHeight)
                    player.dash_sound.play()
                    player.nitro -= 1
                elif event.key == pygame.K_ESCAPE:
                    pause = True
                    #current_lvl.level_music.stop()
                    Paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_UP:
                    player.stop_downDash(playerWidth, playerHeight)

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > screen_width:
            player.rect.left = 0

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left+2 < 0:
            player.rect.right = screen_width
            
        #Sinal que o player tá morrendo
        if player.life < 5 and player.dangerIsActive == False:
            player.danger_sound.play()
            player_lifeColor = RED
            player.image = player.imagemDanger
            if player_lifeColor == RED:
                player_lifeColor = CYAN
                if player_lifeColor == CYAN:
                    player_lifeColor = RED
            player.dangerIsActive = True
        elif player.life >= 5:
            player_lifeColor = CYAN
            player.dangerIsActive = False

            #   ----- Game logic -----

        # 'Limpa' a screen
        screen.fill(BLACK)

        # Chama o metodo update()em cada sprite na lista
        listas.all_sprites_list.update()

        # Checa se o player colidiu com quaisquer platformas.
        # Plataforma padrão

        platforms_hit_list = pygame.sprite.spritecollide(player, listas.platform_list, False)

        for platform in platforms_hit_list:
            if player.change_y > 0:
                platform.change_y = 0
                player.rect.bottom = platform.rect.top
            elif player.change_y < 0:
                player.rect.top = platform.rect.bottom

        # Se Player toca o topo ou embaixo da Screen
        if player.rect.y < - 4 or player.rect.y > 603:
            player.life -= 5
            player.nitro += 1
            player.reset_pos()

        # plataforma grande
        bigPlatforms_hit_list = pygame.sprite.spritecollide(player, listas.bigPlatform_list, False)

        for bigPlatform in bigPlatforms_hit_list:
            if player.change_y > 0:
                bigPlatform.change_y = 0
                player.rect.bottom = bigPlatform.rect.top
            elif player.change_y < 0:
                player.rect.top = bigPlatform.rect.bottom

        # Calcula o funcionamento de cada bullet
        for bullet in listas.bullet_list:

            # Ve se  acerta o block/inimigo
            block_hit_list = pygame.sprite.spritecollide(bullet, listas.block_list, True)

            # Para cada block acertado, remove a bullet e adiciona valor no score
            for block in block_hit_list:
                listas.bullet_list.remove(bullet)
                listas.all_sprites_list.remove(bullet)
                listas.block_list.remove(block)
                listas.all_sprites_list.remove(block)
                block.dead_sound.play()
                score += 100
                print("Score:: %3d\n" % (score))

            # Ve se acerta o a plataforma padrão
            platform_hit_list = pygame.sprite.spritecollide(bullet, listas.platform_list, True)

            # Para cada plataforma acertada, remove a bullet e adiciona valor no score
            for platform in platform_hit_list:
                listas.bullet_list.remove(bullet)
                listas.all_sprites_list.remove(bullet)
                platform.dead_sound.play()
                listas.platform_list.remove(platform)
                listas.all_sprites_list.remove(platform)
                score += 50
                print("Score:: %3d\n" % (score))

            # Remove a bullet se ela sai fora da tela
            if bullet.rect.y < -10 or bullet.rect.y > screen_height + 5:
                shot_jet = 0
                listas.bullet_list.remove(bullet)
                listas.all_sprites_list.remove(bullet)

            # Checa se o player colidiu com o ammo
        for ammo in listas.ammo_list:

            # Ve se  acerta o block/inimigo
            ammo_hit_list = pygame.sprite.spritecollide(player, listas.ammo_list, False)

            # Para cada ammo coletado, remove a ammo e adiciona ao pente
            for ammo in ammo_hit_list:
                listas.ammo_list.remove(ammo)
                listas.all_sprites_list.remove(ammo)
                ammo.get_sound.play()
                pente += 7
                print("Munição:: %3d\n" % (pente))

        # Checa se o player colidiu com o Block. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        blocks_hit_list = pygame.sprite.spritecollide(player, listas.block_list, False)

        # Loop da lista de collisões (blocos --> player).
        for block in blocks_hit_list:
            player.life -= 2
            print("Vida:: %3d\n" % (player.life))
            listas.block_list.remove(block)
            listas.all_sprites_list.remove(block)
            block.dead_sound.play()

        # Condição para passar de fases
        if len(listas.block_list) <= 0:
            done = True
            if start_level == 3:
                current_lvl.level_music.stop()
                show_CreditsScreen()
            else:
                start_level += 1
                current_lvl.level_music.stop()
                pause = True
                return StartLevelScreen()

        # Desenha todos os label
        screen.blit(background, background_position)
        listas.all_sprites_list.draw(screen)
        label = uiFont.render("Vida: " + str(int(player.life)), True, player_lifeColor)
        screen.blit(label, (280, 572))
        label = uiFont.render("Fase: " + str(int(start_level)), True, CYAN)
        screen.blit(label, ( screen_width - 75, 5))
        label2 = uiFont.render("Pontos: " + str(int(score)), True, CYAN)
        screen.blit(label2, (3, 572))
        label3 = uiFont.render("Balas: " + str(int(pente)), True, CYAN)
        screen.blit(label3, (400, 572))
        label4 = uiFont.render("Nitro: " + str(int(player.nitro)), True, CYAN)
        screen.blit(label4, (150, 572))

        # Limita em 60 frames por segundo
        clock.tick(48 + 2*current_lvl.level)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


# Executa as Funções Pincipais
global game
game = True

show_InicialScreenSenac()
show_InicialScreenPesadao()
while game == True:
    TitleIntro()
    Main()
    GameOver()
