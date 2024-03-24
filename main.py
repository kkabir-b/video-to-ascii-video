import cv2
print('\r',end='') 
def print_gray(path):
    q=time.time()
    chars=['#'," "]
    img=cv2.imread(path,0)
    img=cv2.resize(img,(100,50))
    f=[]
    c=0
    for i in img:
        f.append([])
        for s in i:
            f[c].append(chars[int(s>=(255/2))])
        c+=1
    m=''
    q=''' '''
    p=[]
    l=0
    for i in f:
        for s in i:
            q+=s
        l+=1
        q+='\n'
    return q

import pygame
import time

screen = pygame.display.set_mode((1000, 700))
screen.fill((255,255,255))



global font
pygame.init()
font = pygame.font.Font(None, 20)


def write(text, location, color=(0, 0, 0)):
    global font
    screen.blit(font.render(text, True, color), location)




for i in range(0,6572):
    p=0
    q=print_gray(f'frame{i}.jpg')
    for s in q.split('\n'):
        write(s,(10,10+10*p))
        p+=1
    pygame.display.update()
    screen.fill((255,255,255))

