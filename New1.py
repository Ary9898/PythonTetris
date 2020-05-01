import os
import random

import pygame

import MINE as Player

game_dir = os.path.dirname(__file__)
img_folder = os.path.join(game_dir, "img")
pygame.init()
pygame.mixer.init(44100)
Sound = pygame.mixer.Sound(os.path.join(img_folder, "beep.wav"))
Running = True
clk = pygame.time.Clock()
Container_List = []
Container_List.clear()
Container_List.append(Player.Container())
No_of_Entities = 1
Speed = False
while Running:
    if Container_List[No_of_Entities - 1].Lock:
        Sound.play()
        del Player.nextlist[0]
        no = 0
        deletelist = []
        for ycor in range(23):
            for i in Player.mysprites:
                if i.rect.y == ((ycor + 1) * 32):
                    no += 1
            if no >= 10:
                for i in Player.mysprites:
                    if i.rect.y == ((ycor + 1) * 32):
                        deletelist.append(i)
                for z in deletelist:
                    Player.Myspritegroup.remove(z)
                    Player.mysprites.remove(z)
                    for player in Container_List:
                        for sprite in player.mysprite:
                            if sprite == z:
                                player.mysprite.remove(sprite)
                    del z
                deletelist.clear()
                for i in Player.mysprites:
                    if i.rect.y < ((ycor + 1) * 32):
                        i.rect.y += 32
                for i in Container_List:
                    i.movey(False, True)
                Player.Score += 10
            no = 0
        for i in Player.mysprites:
            if i.rect.y <= 192:
                Running = False
        Player.nextlist.append(random.randint(0, 6))
        No_of_Entities += 1
        Container_List.append(Player.Container())
    Player.Disp.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Container_List[No_of_Entities - 1].movex(True)
            if event.key == pygame.K_LEFT:
                Container_List[No_of_Entities - 1].movex(False)
            if event.key == pygame.K_a:
                Container_List[No_of_Entities - 1].rot(False)
            if event.key == pygame.K_s:
                if Player.holdelement[0] == -1:
                    del Player.nextlist[0]
                    Player.nextlist.append(random.randint(0, 6))
                    Player.holdelement.clear()
                    Player.holdelement.append(Container_List[No_of_Entities - 1].shapevar)
                    Player.holdelement.append(Container_List[No_of_Entities - 1].rotvar)
                    Player.holdelement.append(Container_List[No_of_Entities - 1].maxrot)
                    for i in Container_List[No_of_Entities - 1].mysprite:
                        Player.Myspritegroup.remove(i)
                        Player.mysprites.remove(i)
                    del Container_List[No_of_Entities - 1]
                    Container_List.append(Player.Container())
                else:
                    for i in Container_List[No_of_Entities - 1].mysprite:
                        Player.Myspritegroup.remove(i)
                        Player.mysprites.remove(i)
                    Container_List.append(Player.Container(True))
                    Player.holdelement.clear()
                    Player.holdelement.append(Container_List[No_of_Entities - 1].shapevar)
                    Player.holdelement.append(Container_List[No_of_Entities - 1].rotvar)
                    Player.holdelement.append(Container_List[No_of_Entities - 1].maxrot)
                    del Container_List[No_of_Entities - 1]
            if event.key == pygame.K_d:
                Container_List[No_of_Entities - 1].rot(True)
            if event.key == pygame.K_DOWN:
                if not Container_List[No_of_Entities - 1].collide():
                    Speed = True
                else:
                    Container_List[No_of_Entities - 1].Lock = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                Speed = False
    Container_List[No_of_Entities - 1].movey(Speed)
    pygame.draw.rect(Player.Disp, Player.MY_MIX, (400 - 160, 32, 320, 704))
    Player.create_blocks()
    Player.Myspritegroup.draw(Player.Disp)
    Player.display_hold()
    Player.next_display()
    pygame.display.flip()
    clk.tick(60)
Player.Disp.fill((0, 0, 0))
Player.Score_Display()
pygame.display.flip()
print(Player.Score)
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
pygame.quit()
