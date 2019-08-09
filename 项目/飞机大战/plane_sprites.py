import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        # 在屏幕上的垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵创建（image、rect、speed）
        super().__init__("./images/background.png")
        # 2.判断是否交替图像，如果是，需要设置初始值
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        # 1.调用父类的方法实现
        super().update()
        # 2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时制定敌机图片
        super().__init__("./images/enemy1.png")
        # 2.指定敌机的初始速度1~3
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self, *args):
        # 1.调用父类方法，保持垂直方向飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，从精灵组删除")
            # kill方法可以将精灵从所有精灵组中移出，精灵就会自动销毁
            self.kill()

    def __del__(self):
        # print("敌机挂了%s " % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1.调用父类方法设置image&speed
        super().__init__("./images/me1.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 3.创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self, *args):

        # 英雄在水平方向移动
        self.rect.x += self.speed
        if self.rect.x < 0-40:
            self.rect.right = SCREEN_RECT.right+40
        elif self.rect.right > SCREEN_RECT.right+40:
            self.rect.x = 0-40

    def fire(self):

        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置子弹精灵位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            # 3. 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        # 调用父类方法，设置子弹图片，初始速度
        super().__init__("./images/bullet1.png", -4)

    def update(self, *args):
        # 调用父类方法，让子弹垂直飞行
        super().update()
        # 判断子弹是否飞出
        if self.rect.bottom < 0:
            self.kill()

    # def __del__(self):
    #     pass
    #     print("子弹被销毁")







