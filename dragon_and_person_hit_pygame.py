import pygame,random
import pygame.freetype

sx,sy,FPS = 800 , 500 , 60                                                   #螢幕長、寬
role_img = ['images/dragon_girl.png','images/person_boy.png']                #匯入角色圖片
role_img_dead = ['images/dragon_girl_dead.png', 'images/person_boy_dead.png']#匯入角色死亡圖片
skill_img = ['images/potion.png', 'images/sword.png', 'images/sword2.png', 'images/magic.png','images/magic_fire.png','images/magic_fire2.png']#匯入技能圖片
sound = ['fire_ball.mp3', 'dark_magic.mp3', 'light_magic.mp3', 'hit.mp3']    #匯入音效
bg = pygame.image.load('images/bg_dragon_hit_person.png')                    #匯入背景圖片
king = pygame.image.load('images/king.png')                                  #匯入圖片王冠
rounds = 1                                                                   #設定回合數的數字

#建立角色
class role():
    def __init__(self, name, img1, img2, img3, skill1, skill2, skill3, sound1,sound2):
        self.name = name                                                     #角色名稱
        self.img = pygame.image.load(img1)                                   #載入圖片
        self.skill_img1 = pygame.image.load(img2)                            #技能圖片1
        self.skill_img2 = pygame.image.load(img3)                            #技能圖片2
        self.rect = self.img.get_rect()                                      #取得位置
        self.pen = pygame.freetype.Font("images/msjh.ttc", 30)               #繪製文字
        self.skill1 = self.pen.render(skill1, '#CAE9FF', 'black')[0]         #技能1
        self.skill2 = self.pen.render(skill2, '#CAE9FF', 'black')[0]         #技能2
        self.skill3 = self.pen.render(skill3, '#CAE9FF', 'black')[0]         #技能3
        self.say_ing = 0                                                     #顯示技能時間
        self.status = False                                                  #顯示技能是否爆擊
        self.status_time = 0                                                 #顯示技能爆擊時間
        self.hp = 20                                                         #生命
        self.skillchose = 0                                                  #技能選擇
        self.sound = 0                                                       #音效時間
        self.sound1 = pygame.mixer.Sound('images/'+sound1)                   #音效1
        self.sound2 = pygame.mixer.Sound('images/'+sound2)                   #音效2


#技能攻擊
    def attack(self,enemy):
        choose1 = random.random()

        #技能1
        if choose1 > 0.3:
            self.skillchose = 1
            #查看是否爆擊
            if random.randint(1,10) == 2:
                enemy.hp -= 4
                self.status = True                                           #設定顯示技能爆擊為 True
                self.status_time = 60                                        #設定顯示技能爆擊時間為 60s
            else:
                enemy.hp -= 2
        #技能2
        elif 0.1 < choose1 < 0.3 or self.hp == 1:
            self.skillchose = 2
            self.hp += 4
        #技能3
        else:
            self.skillchose = 3
            if random.randint(1,10) == 2:
                enemy.hp -= 10
                self.status = True
                self.status_time = 60
            else:
                enemy.hp -= 5
                enemy.status_time = 60

    def __repr__(self):
        return self.name

    #播放音效
    def say(self):
        if self.sound <= 0:                                                  #如果音效時間 = 0
            self.sound = 110                                                 #音效時間設為 1.9s
        if self.sound > 0:                                                   #如果音效時間 > 0
            if self.skillchose == 1:                                         #如果技能選擇到技能1
                self.sound1.play()                                           #播放技能1的音效
            if self.skillchose == 3:                                         #如果技能選擇到技能3
                self.sound2.play()                                           #播放技能3的音效

    #更新畫面
    def update(self,screen):
        screen.blit(self.img, self.rect)                                     #把圖片畫出來

        run = self.pen.render(f'回合數：第{rounds}回', 'white')[0]            #設定回合數
        screen.blit(run,(10,10))                                             #繪製回合數

        if self.say_ing <= 0:                                                #如果顯示技能時間 <= 0
            self.say_ing = 170                                               #技能時間設為 2.9s
        if self.say_ing>0:                                                   #如果顯示技能時間 > 0
            if self.skillchose == 1:                                         #如果技能選擇到技能1
                screen.blit(self.skill_img1,self.skill_img1.get_rect(center=(sx//2,sy//2)))                                  #畫出技能1的圖片
                screen.blit(self.skill1,self.rect.bottomleft)                                                                #畫出技能1的文字
            if self.skillchose == 2:                                                                                         #如果技能選擇到技能2
                screen.blit(pygame.image.load(skill_img[0]),pygame.image.load(skill_img[0]).get_rect(center=(sx//2,sy//2)))  #畫出技能2的圖片
                screen.blit(self.skill2,self.rect.bottomleft)                                                                #畫出技能2的文字
            if self.skillchose == 3:                                                                                         #如果技能選擇到技能3
                screen.blit(self.skill_img2,self.skill_img2.get_rect(center=(sx//2,sy//2)))                                  #畫出技能3的圖片
                screen.blit(self.skill3,self.rect.bottomleft)                                                                #畫出技能3的文字
            self.say_ing-=1

        if self.status_time >0:                                                     #如果顯示技能爆擊時間 > 0
            dodge_pen = pygame.freetype.Font("images/msjh.ttc", 25)
            dodge_img,dodge_rect = dodge_pen.render(f'爆擊成功!','red', 'black')     #設定紅色的字來顯示爆擊成功
            self.status_time-=1

            if self.status_time == 0:                                               #如果顯示技能爆擊時間 = 0
                self.status = False                                                 #設定顯示技能爆擊為 False

            if self.status == True:                                                 #如果顯示技能爆擊為 True
                dodge_rect.center=self.rect.center
                screen.blit(dodge_img,dodge_rect)                                   #繪製紅色的字來顯示爆擊成功
        hp_pen = pygame.freetype.Font("images/msjh.ttc", 20)
        self.hpimage = hp_pen.render(f'hp：{self.hp}', '#96E072', 'black')[0]
        screen.blit(self.hpimage, self.hpimage.get_rect(topright=self.rect.topright)) # 加hp文字
        self.nameimg = self.pen.render(f'{self.name}', '#F7B538', 'black')[0]
        screen.blit(self.nameimg, self.nameimg.get_rect(topleft=self.rect.topleft))   #加角色名字

#遊戲初始化
pygame.init()
screen = pygame.display.set_mode((sx,sy))
clock = pygame.time.Clock()
pygame.key.stop_text_input()
pygame.display.set_caption(u"勇者對戰龍王")

win_lose_pen = pygame.freetype.Font("images/msjh.ttc", 30)                                                          #建立輸贏的筆

dragon = role('龍王' , role_img[0], skill_img[4], skill_img[5], '火之咆嘯', '治癒', '惡龍吐息', sound[0], sound[1])   #建立角色 龍王
person = role('勇者' , role_img[1], skill_img[1], skill_img[2], '光之斬擊' , '治癒' , '勝利之斬', sound[2], sound[3]) #建立角色 勇者

#把角色放到畫面的地方
dragon.rect.move_ip(550,150)
person.rect.move_ip(100,150)

#設定回合制
last = pygame.time.get_ticks()

#game_state 為遊戲模式
running, game_state = True, 0
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if not running:
        break

    #畫出背景
    screen.blit(bg,(0,0))

    #遊戲中
    if game_state == 0:

        dragon.update(screen)
        person.update(screen)

        now = pygame.time.get_ticks()
        if now-last >= 3000:                           #每3秒一回合
            last = now                                 #更新 last，預備下一次回合

            rounds += 1                                #更新目前回合數
            dragon.attack(person)
            person.attack(dragon)
            dragon.say()
            person.say()
            if dragon.hp <= 0:
                dragon.hp = 0
            if person.hp <= 0:
                person.hp = 0

    #如果其中一個生命歸 0，設定遊戲模式為 1
    if dragon.hp <= 0 or person.hp <= 0:
        game_state = 1

    #遊戲結束
    if game_state == 1:
        dragon.update(screen)
        person.update(screen)
        winner = pygame.mixer.Sound('images/winner.mp3')                  #設定勝利歌
        winner.play()
        #平手
        if dragon.hp <= 0 and person.hp <= 0:
            txt_over = win_lose_pen.render(f'平手','gold','black')[0]
            screen.blit(txt_over,txt_over.get_rect(center=(sx//2,sy//2)))

        #dragon勝利
        elif person.hp <= 0:
            txt_over = win_lose_pen.render(f'dragon勝利','gold','black')[0]
            # dragon.update(screen)
            person.img = pygame.image.load(role_img_dead[1])
            screen.blit(person.img,(100,150))
            screen.blit(txt_over,txt_over.get_rect(center=(sx//2,sy//2)))
            screen.blit(king,(520,10))

        #person勝利
        elif dragon.hp <= 0 :
            txt_over = win_lose_pen.render(f'person勝利','gold','black')[0]
            # person.update(screen)
            dragon.img = pygame.image.load(role_img_dead[0])
            screen.blit(dragon.img, (550,150))
            screen.blit(txt_over,txt_over.get_rect(center=(sx//2,sy//2)))
            screen.blit(king,(70,10))

    pygame.display.flip()

pygame.quit()
