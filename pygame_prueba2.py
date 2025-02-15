import pygame,random

black=(0,0,0)
white=(255,255,255)

#background = pygame.image.load("Mexico.png").convert()

class Meteor(pygame.sprite.Sprite):
    def __init__(self,*sprite):
        super().__init__(*sprite)
        self.image= pygame.image.load("Mexico.png").convert()
        self.image.set_colorkey(white)
        self.rect=self.image.get_rect()
    
    def update(self):
        self.rect.y += -1

        if self.rect.y > 600:
            self.rect.y=-10
            self.rect.x=random.randrange(900)


class Player(pygame.sprite.Sprite):
    def __init__(self,*sprite):
        super().__init__(*sprite)
        self.image= pygame.image.load("Nave.jpeg").convert()
        self.image.set_colorkey(white)
        self.rect=self.image.get_rect()

    def update(self):
        mouse_pos=pygame.mouse.get_pos()
        player.rect.x=mouse_pos[0]
        player.rect.y=mouse_pos[1]

pygame.init()

screen =pygame.display.set_mode([515,515])
clock = pygame.time.Clock()
score=0
done= False

meteor_list = pygame.sprite.Group()
all_sprite_list=pygame.sprite.Group()

for i in range(500):
    meteor=Meteor()
    meteor.rect.x=random.randrange(900)
    meteor.rect.y=random.randrange(600)
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player=Player()
all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    
    all_sprite_list.update()

    meteor_hit_list =pygame.sprite.spritecollide(player,meteor_list,True)
    for meteor in meteor_hit_list:
        score+=1
        print(score)

    screen.fill(white)

    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
