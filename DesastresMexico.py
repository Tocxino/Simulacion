import pygame,random
import time
size = (515, 515)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done= False
black=(0,0,0)

# Cargar imagen de fondo
background = pygame.image.load("Mexico.png").convert()
rayo=pygame.image.load("RayoPequeño.png")
volcan=pygame.image.load("Volcan.png")
meteorito=pygame.image.load("Meterito.png")

class Meteor(pygame.sprite.Sprite):
    def __init__(self,*sprite):
        super().__init__(*sprite)
        self.image= pygame.image.load("Meterito.png").convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
    
    def update(self):
        self.rect.y +=1
        a=random.randrange(500)
        if self.rect.y > 600:
            self.rect.y=-10
            self.image= pygame.image.load("Meterito.png").convert()
            self.rect.x=random.randrange(500)
        elif self.rect.y == a:
            self.rect.y=0
            self.image= pygame.image.load("Volcan.png").convert()




class Rayos(pygame.sprite.Sprite):
    def __init__(self,*sprite):
        super().__init__(*sprite)
        self.image= pygame.image.load("RayoPequeño.png").convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.x=random.randrange(50,400)
        self.rect.y=random.randrange(110,400)

class Volcanes(pygame.sprite.Sprite):
    def __init__(self,*sprite):
        super().__init__(*sprite)
        self.image= pygame.image.load("Volcan.png").convert()
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()

volcanes_list=pygame.sprite.Group()
rayos_list = pygame.sprite.Group()
meteorito_list = pygame.sprite.Group()
all_sprite_list=pygame.sprite.Group()

for i in range(10):
    rayos=Rayos()
    rayos.rect.x=random.randrange(50,400)
    rayos.rect.y=random.randrange(110,400)
    rayos_list.add(rayos)
    all_sprite_list.add(rayos)


for i in range(5):
    volcanes=Volcanes()
    volcanes.rect.x=random.randrange(100,250)
    volcanes.rect.y=random.randrange(110,250)
    volcanes_list.add(volcanes)
    all_sprite_list.add(volcanes)

for i in range(15):
    meteorito=Meteor()
    meteorito.rect.x=random.randrange(500)
    meteorito.rect.y=random.randrange(500)
    meteorito_list.add(meteorito)
    all_sprite_list.add(meteorito)


while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.blit(background, [0, 0])
    all_sprite_list.draw(screen)
    all_sprite_list.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()