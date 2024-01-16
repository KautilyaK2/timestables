import pygame
import pygame_textinput
import random
pygame.init()
display=pygame.display.set_mode((800,800))
def question(level):
    par1=round(level*3*random.random())
    par2=round(level*3*random.random())
    return str(par1)+' * '+str(par2)
done=0
level=1
font = pygame.font.Font(None, 120)
vis=pygame_textinput.TextInputVisualizer(font_object=font)
q=question(level)
while not done:
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            done=1
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                if int(vis.value)==eval(q):
                    level+=1
                else:
                    print(eval(q))
                    level-=0.5
                q=question(level)
    vis.update(events)
    surf=font.render(q,0,(0,0,0))
    display.fill((255,255,255))
    display.blit(surf,(200,200))
    display.blit(vis.surface,(400,400))
    pygame.display.update()
pygame.quit()