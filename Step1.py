# -*- coding: utf-8 -*-
# 初始规划，4个类

class Person():
    pass
class Gun():
    pass
class Bullet():
    pass
class Charger():
    pass

# 规划好类以后，定义实例，抢劫犯和警察，
# 抢劫犯受伤没有强， 警察手上有枪，并且安装了子弹。
#默认的话人既没有子弹也没有弹夹
# 定义一个初始的场景，一个警察，默认100滴血，一个抢劫犯，警察安装好 子弹和弹夹，警察开一枪，抢劫犯少10滴血
# 当抢劫犯没有血的时候，抢劫犯就死了。 游戏结束。

robber = Person()
policeman = Person()
gun=Gun()
bullet=Bullet() #子弹
charger=Charger() #弹夹+

# 定义好类以后。定义方法。
# 把警察把子弹安装在弹夹里面。所以警察有把子弹安装在弹夹中的方法
# 弹夹有安装子弹的方法。
policeman.install_bullet()
# 警察有射击的功能，当警察射击的时候，抢劫犯就会掉血。 射击的目标是抢劫犯，所以把抢劫犯作为参数传进来。
policeman.shot(robber)



