# *_* coding : UTF-8 *_*
# author  ：  Leemamas
# 开发时间  ：  2021/9/22  15:05

import pygame
import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,angle,enemtlist):
        super(Bullet, self).__init__()
        self.image=pygame.image.load('images/bullet1.png')
        self.org_image=self.image.copy()
        self.angle=angle
        self.image=pygame.transform.rotate(self.org_image,self.angle)
        self.distance=50
        self.pos_x=math.sin(math.radians(-self.angle))*self.distance+pos[0]
        self.pos_y=pos[1]-math.cos(math.radians(math.fabs(self.angle)))*self.distance
        self.pos=(self.pos_x,self.pos_y)

        self.rect=self.image.get_rect(center=self.pos)

        self.speed=3
        self.isDestory=False
        self.enemtlist=enemtlist

    def display(self, screen):
        screen.blit(self.image, self.rect)
        self.move()

    def move(self):
        self.pos_x+=math.sin(math.radians(-self.angle))*self.speed
        self.pos_y-=math.cos(math.radians(math.fabs(self.angle)))*self.speed

        self.pos = (self.pos_x, self.pos_y)
        self.rect = self.image.get_rect(center=self.pos)

        if self.pos_y<0 or self.pos_x<0 or self.pos_x>1024:
            self.isDestory=True
        self.attack(self.enemtlist)

    def attack(self,enemtlist):
        for enemy in enemtlist:
            # print(enemy.rect,self.rect)
            if pygame.sprite.collide_circle_ratio(0.5)(enemy,self):
                # enemy.isDestory=True
                enemy.isAttack=True
                enemy.y=148
                self.isDestory=True

        ##子弹攻击小鱼，子弹消失，小鱼消失
        # 先将子弹和小鱼都变成pygame的精灵类，可以使用边界碰撞判断
        ###将要攻击的鱼作为参数传入