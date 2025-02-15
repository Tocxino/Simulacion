import pygame, sys, random
pygame.init()

#Definir colores
BLACK =(0,0,0)
WHITE =(255,255,255)
GREEN =(0,255,0)
RED =(255,0,0)
BLUE =(0,0,255)

size = (700,700)
background = pygame.image.load("Mexico.png").convert()
#background = pygame.image.load("Mexico.png").convert()

# Crear ventana
screen = pygame.display.set_mode(size)

background = pygame.image.load("Mexico.png").convert()

#Controlar los fps 
clock =pygame.time.Clock()

#coordenadas del cuadro
cord_x=10
cord_y=10

#velocidad a la que e movera mi cuadrado
speed_x=0
speed_y=0

pygame.mouse.set_visible(0)
coord_list=[]
for i in range (60):
        x =random.randint(0,800)
        y =random.randint(0,500)
        coord_list.append([x,y])
        pygame.draw.circle(screen,RED,(x,y),2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #eventos teclado}
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x=-3
            if event.key == pygame.K_RIGHT:
                speed_x=3
            if event.key == pygame.K_UP:
                speed_y=-3
            if event.key == pygame.K_DOWN:
                speed_y=3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x=0
            if event.key == pygame.K_RIGHT:
                speed_x=0
            if event.key == pygame.K_UP:
                speed_y=0
            if event.key == pygame.K_DOWN:
                speed_y=0
    # ---- LOGICA
    if (cord_x>720 or cord_x < 0):
        speed_x *=-1
    if (cord_y>420 or cord_y<0):
        speed_y*=-1

    cord_x+=speed_x
    cord_y+=speed_y



    # ---- LOGICA

    #Color de fondo
    #mouse_pos=pygame.mouse.get_pos()
    #x=mouse_pos[0]
    #y=mouse_pos[1]

    screen.blit(background, [0, 0])    #poner color de fondo
    ### ----- ZONA DE DIBUJO
    #for j in coord_list:
    #    pygame.draw.circle(screen,RED,j,2)
    #    j[1]+=1
    #    if j[1]>500:
    #        j[1]=0
    #pygame.draw.line(screen, GREEN, [0,100], [100,100], 5)
    #pygame.draw.rect(screen, BLACK, (100,100,80,80))
    #pygame.draw.circle(screen,RED,(100,100),5)
    #pygame.draw.rect(screen, BLACK, (x,y,80,80))
    #for i in range (100,700,100):
        #pygame.draw.rect(screen,BLACK,(i,230,50,50))
        #pygame.draw.line(screen, GREEN, [i,0], [i,100], 5)
    
    pygame.draw.rect(screen,RED,(cord_x,cord_y,80,80))
    
    
    ### ----- ZONA DE DIBUJO
    pygame.display.flip()   #actualizar pantalla 
    clock.tick(60)

pygame.quit()
sys.exit