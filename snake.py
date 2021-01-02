import pygame
import time
import random

pygame.init()

screen=pygame.display.set_mode((400,300))
done=False
x=50;y=50;h=0;r=0;u=0;d=0;l=0;s=1;score=0;g=0;flag=0
X=random.randrange(10,380)
Y=random.randrange(45,280)
l1=[]
clock=pygame.time.Clock()
start=time.time()

sound1=pygame.mixer.Sound('eat.wav')
sound2=pygame.mixer.Sound('gameover.wav')
font1=pygame.font.SysFont('comicsancms',50)
font2=pygame.font.SysFont('comicsancms',35)
text1=font1.render('GAME OVER',True,(200,200,200))
text3=font2.render('Press Spacebar To Exit',True,(200,200,200))

while not done:

    screen.fill((0,0,0))
    stop=time.time()
    text2=font2.render('SCORE= %d'%(score),True,(150,150,150))
    pygame.draw.rect(screen,(100,100,100),pygame.Rect(0,0,10,300))
    pygame.draw.rect(screen,(100,100,100),pygame.Rect(0,0,400,10))
    pygame.draw.rect(screen,(100,100,100),pygame.Rect(0,290,400,10))
    pygame.draw.rect(screen,(100,100,100),pygame.Rect(390,0,10,300))

    if h==0:
        x+=1
    
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            done=True

    clock.tick(60)
    press=pygame.key.get_pressed()

    if s==0 and press[pygame.K_SPACE]: done=True

    if press[pygame.K_RIGHT]:
        r=1
        d=0
        l=0
        u=0
        h=1
    elif press[pygame.K_DOWN]:
        d=1
        r=0
        l=0
        u=0
        h=1
    elif press[pygame.K_LEFT]:
        l=1
        d=0
        r=0
        u=0
        h=1
    elif press[pygame.K_UP]:
        u=1
        d=0
        r=0
        l=0
        h=1

    if s==1:
        t=1
        if u==1: y-=t
        elif d==1: y+=t
        elif r==1: x+=t
        elif l==1: x-=t

    else:
        t=0
        if u==1: y-=t
        elif d==1: y+=t
        elif r==1: x+=t
        elif l==1: x-=t

    pygame.draw.rect(screen,(10,200,10),pygame.Rect(X,Y,10,10))
    pygame.draw.rect(screen,(0,10,200),pygame.Rect(x,y,10,10))

    if x==10 or x==380:
        s=0
        screen.blit(text1,(200-text1.get_width()//2,100-text1.get_height()//2))
        screen.blit(text3,(200-text3.get_width()//2,150-text2.get_height()//2))
    if y==10 or y==280:
        s=0
        screen.blit(text1,(200-text1.get_width()//2,100-text1.get_height()//2))
        screen.blit(text3,(200-text3.get_width()//2,150-text2.get_height()//2))
    if (x>=X-9 and x<=X+9) and (y>=Y-9 and y<=Y+9):
        sound1.play(0)
        score+=1
        X=random.randrange(10,380)
        Y=random.randrange(45,280)
    if (stop-start)>=0.5:
        g+=1
        start=time.time()

    t+=1
    if s==1:
        l1.append([x,y])

    for i in l1:
        pygame.draw.rect(screen,(0,10,200),pygame.Rect(i[0],i[1],10,10))

    if len(l1)>(30+g):
        l1.remove(l1[0])

    for i in range(len(l1)-1):
        if x==l1[i][0] and y==l1[i][1]:
            s=0
            screen.blit(text1,(200-text1.get_width()//2,100-text1.get_height()//2))
            screen.blit(text3,(200-text3.get_width()//2,150-text2.get_height()//2))

    screen.blit(text2,(365-text2.get_width(),20))

    if s==0 and flag==0:
        sound2.play(0)
        flag=1

    pygame.display.flip()
    
print('Score= %d'%(score))