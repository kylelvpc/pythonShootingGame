# -*- coding: utf-8 -*-
# 初始规划，4个类

class Person():
    # 默认就是人有100滴血，这个是默认信息。
    def __init__(self,name):
        self.name = name
        self.blood_count=100

    # 人有安装子弹的功能。这里，安装子弹到那里，所以这里需要传入参数，穿一个弹夹进来。
    def get_gun(self,gun): # 人拿枪
        self.gun = gun

    def install_bullet(self, charger):
        pass
    # 同上，人有安装弹夹的功能，将弹夹安装在枪里面。
    def install_charger(self,gun):
        pass
    def looseblood(self): # 掉血的方法。在受到枪击以后会掉血。
        if self.blood_count == 0:
            print(self.name+"血量流失殆尽，死了")
        else:
            self.blood_count -= 10

    def trigger(self,gun): # 扣扳机，这里需要传入一个【枪的】变量，来指明 扣的是哪一把枪的扳机
        # 扣扳机以后，子弹就会少一颗，当子弹没有了以后，再扣扳机的时候，就打不出子弹了。
        # 所以这里有个判断动作。判断是否有子弹。
        gun.shoot_out_bullet()


class Gun():
    # 枪，默认是没有弹夹的，它的功能就是射击。这里我们把射击的目标作为参数放在 子弹那里，所以这里就
    # 单纯只有一个扣扳机的动作
    def __init__(self,name):
        self.name=name
    # 枪可以保存弹夹
    def install_charger(self,charger): # 枪可以安装弹夹，
        pass
    def uninstall_charger(self,charger): # 枪可以卸下弹夹
        pass

    def shoot_out_bullet(self): # 枪可以射出子弹，子弹是从弹夹里面飞出去的, bullet 表示飞出去的子弹。
        # 那么弹夹中的子弹就会减少
        pass

class Bullet():
    # 子弹的作用就是射击
    def shoot(self,person):  # 这里顶一个射击的目标，某个人
        # 我们默认为是打中了。打中以后，被打中的这个人就会掉血，后面可能根据场景的不一样，掉的血也不一样
        person.looseblood()

class Charger():
    # 在step4 中， 设计 弹夹的方法有两个，一个是保存子弹，一个是弹出子弹
    # 定义个队列来保存子弹实例
    bullet_list=[]
    def install_bullet(self,bullet):
        self.bullet_list.append(bullet)
    def uninstall_bullet(self): # 弹出子弹
        pass

# 规划好类以后，定义实例，抢劫犯和警察，
# 抢劫犯受伤没有强， 警察手上有枪，并且安装了子弹。
#默认的话人既没有子弹也没有弹夹
# 定义一个初始的场景，一个警察，默认100滴血，一个抢劫犯，警察安装好 子弹和弹夹，警察开一枪，抢劫犯少10滴血
# 当抢劫犯没有血的时候，抢劫犯就死了。 游戏结束。

robber = Person("麻子")
policeman = Person("李刚")
gun=Gun("AK47")
bullet=Bullet() #子弹
charger=Charger() #弹夹+

# 定义好类以后。定义方法。
# 把警察把子弹安装在弹夹里面。所以警察有把子弹安装在弹夹中的方法
# 弹夹有安装子弹的方法。
policeman.install_bullet(charger)  # 这是安装子弹的动作，每次安装一颗的话，需要安装2
# 警察有射击的功能，当警察射击的时候，抢劫犯就会掉血。 射击的目标是抢劫犯，所以把抢劫犯作为参数传进来。
policeman.install_charger(gun)
policeman.trigger(gun)



