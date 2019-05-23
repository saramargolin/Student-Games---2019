#The Panda
#Frozen in Time
#Thomas Hsu
#Avoid and dodge obstacles, reach the portal at the end of levels

from gamelib import*

game=Game(800,600, "Frozen in Time",100)

bk = Image("background7withground.png",game)
bk.resizeBy(300)
game.setBackground(bk)
game.setMusic("gothic.mp3")
game.playMusic()
#scrolling
t = 1

item = 0

#variable for jumps
jh = 9 #jump height
fa = 0.96 #factor*

#miner title screen
minerst = Animation("miner2sprite.png",12,game,152/4,162/3)
minerst.resizeBy(50)
minerst.stop()
minerst.x = -20
minerst.y = 500
minerst.setSpeed(3,270)

#Cutscene miner
minercs = Animation("miner2sprite.png",12,game,152/4,162/3)
minercs.resizeBy(50)
minercs.stop()
minercs.x = -20
minercs.y = 500
minercs.setSpeed(3,270)

#main miner
miner = Animation("miner2sprite.png",12,game,152/4,162/3)
miner.resizeBy(50)
miner.stop()
miner.x = 100
miner.y = 500
miner.setSpeed(t,90)

#miner flipped
minerf = Animation("miner2spriteflip.png",12,game,152/4,162/3)
minerf.resizeBy(50)
minerf.stop()
minerf.visible = False
minerf.x = miner.x
minerf.y = miner.y
minerf.setSpeed(t,90)

miners = []

for index in range(10):
    miners.append(Image("miner2p.png",game))

for index in range(len(miners)):
    x = randint(400,750)
    miners[index].moveTo(x,500)
    miners[index].resizeBy(50)

logo = Image("logo3.png",game)
logo.resizeBy(30)
logo.y = 100

ptp = Image("play2.png",game)
ptp.y = 300

htp = Image("htp.png",game)
htp.resizeBy(-55)
htp.x = 110
htp.y = 580

#fonts
f1=Font(white,25,blue,"Impact")
f2=Font(white,50,blue,"MS Gothic")
f3=Font(white,50,red,"MS Gothic")

#variable for jumping action        
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = .5  #Used for a slowing effect of the jumping

arrow = Image("arrow3.png",game)

arrows = []

for index in range(25):
    arrows.append(Image("arrow3.png",game))

for index in range(len(arrows)):
    x = randint(805,4592)
    y = randint(250,500)
    arrows[index].moveTo(x,y)
    #s = randint(3,6)
    arrows[index].setSpeed(5,90)
    arrows[index].resizeBy(200)

arrowm = Image("arrow3f.png",game)
arrowm.setSpeed(10,270)
arrowm.resizeBy(150)
arrowm.x = miner.x
arrowm.y = miner.y
arrowm.visible = False

arrowmf = Image("arrow3.png",game)
arrowmf.setSpeed(10,90)
arrowmf.resizeBy(150)
arrowmf.x = miner.x
arrowmf.y = miner.y
arrowmf.visible = False

boss1 = Animation("skeletonbosssprite.png",24,game,880/4,840/6)
boss1.setSpeed(2,90)
boss1.resizeBy(75)
boss1.x = 950
boss1.y = 435

boss1t = Animation("skeletonbosssprite.png",24,game,880/4,840/6)
boss1t.resizeBy(75)
boss1t.x = boss1.x
boss1t.y = boss1.y
boss1t.visible = False

boss1.health = 50

ufost = Image("ufo.png",game)
ufost.resizeBy(-80)
ufost.setSpeed(10,90)
ufost.x = 900
ufost.y = 200

knightst = Animation("knightwalkingsprite.png",21,game,1740/3,3500/7)
knightst.resizeBy(-70)
knightst.setSpeed(5,270)
knightst.x = -150
knightst.y = 475

htpit = Image("howtoplay3.png",game)
htpit.x = 400
htpit.y = 150

portal = Image("portal3.png",game)
portal.setSpeed(t,90)
portal.resizeBy(-35)
portal.x = 950
portal.y = 425

sword = Image("sword.png",game)
axe = Image("axe.png",game)
spear = Image("spear.png",game)
smash = Image("smash thingy.png",game)

weapons = []

for index in range(5):
    weapons.append(Image("sword.png",game))
    weapons.append(Image("axe.png",game))
    weapons.append(Image("spear.png",game))
    weapons.append(Image("smash thingy.png",game))
    
for index in range(len(weapons)):
    x = randint(815,3842)
    y = randint(300,500)
    weapons[index].moveTo(x,y)
    weapons[index].setSpeed(6,90)
    weapons[index].resizeBy(200)

spear = Image("spearangle.png",game)

spears = []

for index in range(100):
    spears.append(Image("spearangle.png",game))

for index in range(len(spears)):
    x = randint(600,7000)
    y = -randint(50,2500)
    spears[index].moveTo(x,y)
    spears[index].resizeBy(200)
    spears[index].setSpeed(7,135)


canb = Image("cannonball2.png",game)

canb = []

for index in range(5):
    canb.append(Image("cannonball2.png",game))

for index in range(len(canb)):
    x = randint(850,9575)
    y = randint(400,500)
    canb[index].moveTo(x,y)
    canb[index].setSpeed(15,90)
    canb[index].resizeBy(-75)

boss2 = Animation("bossknight.png",21,game,3000/3,10500/7)
boss2.setSpeed(3,90)
boss2.resizeBy(-70)
boss2.x = 950
boss2.y = 450

boss2t = Animation("bossknight.png",21,game,3000/3,10500/7)
boss2t.resizeBy(-70)
boss2t.x = boss2.x
boss2t.y = boss2.y
boss2t.visible = False

boss2.health = 100

arrowt = []

for index in range(50):
    arrowt.append(Image("arrow3.png",game))

for index in range(len(arrowt)):
    x = randint(805,13428)
    y = randint(250,500)
    arrowt[index].moveTo(x,y)
    arrowt[index].setSpeed(5,90)
    arrowt[index].resizeBy(200)

#text top
y = 50
a = 450

neo = Image("10000BC.png",game)
neo.x = a
neo.y = y
neo.setSpeed(1,90)

neoo = Image("the neo was a.png",game)
neoo.resizeBy(-50)
neoo.x = a+1075
neoo.y = y
neoo.setSpeed(1,90)

b = 390

mdle = Image("middle ages.png",game)
mdle.x = b
mdle.y = y
mdle.setSpeed(1,90)

mdlee = Image("middle ages sig.png",game)
mdlee.resizeBy(-50)
mdlee.x = b + 1255
mdlee.y = y
mdlee.setSpeed(1,90)

gold = Animation("treasureCoinPileSprite.png",16,game,1000/2,1528/8)
gold.resizeBy(-45)
gold.x = 500
gold.y = 500

gold1 = Animation("treasureCoinPileSprite.png",16,game,1000/2,1528/8)
gold1.resizeBy(-45)
gold1.x = 650
gold1.y = 485

mess = Image("message2.png",game)
mess.resizeBy(250)
mess.x = 575
mess.y = 425

rclick = Image("CRtS.png",game)
rclick.resizeBy(-60)
rclick.x = 150
rclick.y = 575

healthbar = Animation("Healthbar2.png",100,game,1040/10,160/10)
healthbar.stop()
healthbar.resizeBy(125)
healthbar.x = 150
healthbar.y = 575

healthbarb = Animation("Healthbar2.png",100,game,1040/10,160/10)
healthbarb.stop()
healthbarb.resizeBy(125)
healthbarb.x = 650
healthbarb.y = 575

back = Image("back.png",game)
back.resizeBy(-45)
back.x = 700
back.y = 575

go = Image("game over.png",game)
go.resizeBy(100)
go.y = 490
go.setSpeed(6,270)

shine = Animation("shine2.png",30,game,400/5,360/6)
shine.resizeTo(game.width,game.height)

ydi = Image("youdidit.png",game)
ydi.resizeBy(100)
ydi.y = 200

shooting = Sound("shooting.wav",1)
clash = Sound("swordclash.wav",2)

#title screen -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while not game.over:
    game.processInput()
    #game.playMusic()
    game.scrollBackground("left",1)
    bk.draw()
    logo.draw()
    ufost.move()
    minerst.move()
    knightst.move()
    htp.draw()
    ptp.draw()
   
    
    if minerst.move:
        minerst.nextFrame()
    if minerst.isOffScreen("right"):
        minerst.x = -100
        item +=1

    if ufost.isOffScreen("left"):
        ufost.x = 900
        item +=1
        
    if knightst.isOffScreen("right"):
        knightst.x = -150
        item +=1

    #game.drawText("Items: " + str(item), 600, 500, f1)

    #tutorial    
    if mouse.collidedWith(htp,"rectangle") and mouse.LeftClick:
        while not game.over:#tutorial game loop within game loop
            game.processInput()
            game.scrollBackground("left",0)
            htpit.draw()
            back.draw()
            arrowm.move()
            arrowmf.move()
            miner.draw()
            minerf.draw()
                
            if mouse.LeftClick and miner.visible:                                                #miner shoots when press how to play // find how to cancel shoot when press how to play
                arrowm.visible = True
                arrowm.moveTo(miner.x,miner.y)

            if mouse.LeftClick and minerf.visible:
                arrowmf.visible = True
                arrowmf.moveTo(miner.x,miner.y)

            if keys.Pressed[K_RIGHT] or keys.Pressed[K_d]:
                minerf.visible = False
                miner.visible = True
                miner.nextFrame()
                minerf.x = miner.x
                minerf.y = miner.y
                miner.x+=4
        
            elif keys.Pressed[K_LEFT] or keys.Pressed[K_a]:
                miner.visible = False
                minerf.visible = True
                minerf.nextFrame()
                miner.x = minerf.x
                miner.y = minerf.y        
                minerf.x-=5
        
            if miner.visible:
                if miner.y< 500:
                    landed = False#not landed

                else:
                    landed = True
            
                if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
                    jumping = True

                if jumping:
                    miner.y -=27*factor#adjust for the drop
                    #Make the character go up.  Factor creates a slowing effect to the jump
                    factor*=fa#fall slowly
                    landed = False
                    #Since you are jumping you are no longer staying on land
                    if factor < .18:
                        jumping = False
                        #Stop jumping once the slowing effect finishes
                        factor = 1
            
                if not landed: #is jumping
                    miner.y +=jh#adjust for the height of the jump - lower number higher jump

            if minerf.visible:
                if minerf.y< 500:
                    landed = False#not landed
    
                else:
                    landed = True
            
                if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
                    jumping = True

                if jumping:
                    minerf.y -=27*factor#adjust for the drop
                    #Make the character go up.  Factor creates a slowing effect to the jump
                    factor*=fa#fall slowly
                    landed = False
                    #Since you are jumping you are no longer staying on land
                    if factor < .18:
                        jumping = False
                        #Stop jumping once the slowing effect finishes
                        factor = 1
            
                if not landed: #is jumping
                    minerf.y +=jh#adjust for the height of the jump - lower number higher jump

            if mouse.collidedWith(back) and mouse.LeftClick:
                game.over = True
  
            game.update(30)
            
    game.over=False
        
    if mouse.collidedWith(ptp) and mouse.LeftClick:
        game.over = True
        
    if mouse.RightClick:
        game.over = True

    game.update(30)

game.over = False

game.time = 100

#Cutscene
while not game.over:
    game.processInput()
    game.scrollBackground("left",0)
    bk.draw()
    minercs.move()
    gold1.draw()
    gold.draw()
    rclick.draw()

    if minercs.move:
        minercs.nextFrame()

    if minercs.x >=gold.x - 193:
        minercs.setSpeed(0,270)
        minercs.prevFrame()
        mess.draw()

    if game.time <= 95:
        shine.draw()

    if game.time <=94:
        game.over = True

    if mouse.RightClick:
        game.over = True
    
    game.update(30)
    
game.over = False

item = 0
miner.x = 100
arrowm.x = miner.x
arrowm.y = miner.y

#Level 1 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while not game.over:
    game.processInput()
    game.scrollBackground("left",t)
    bk.draw()
    if item >= len(arrows):
        boss1.move()
        boss1t.move()
        healthbarb.draw()
    neo.move()
    neoo.move()
    arrowm.move()                           #shoots an arrow from how to play
    miner.move()
    minerf.move()
    healthbar.draw()
    
    for index in range(len(arrows)):
        arrows[index].move()
        if miner.collidedWith(arrows[index],"rectangle") or minerf.collidedWith(arrows[index],"rectangle"):
            arrows[index].visible = False
            miner.health -=1
            item +=1
            healthbar.nextFrame()

        if arrows[index].isOffScreen("left") and arrows[index].visible:
            arrows[index].visible = False
            item +=1

    if boss1.collidedWith(miner) or boss1.collidedWith(minerf):
        boss1.visible = False
        boss1t.visible = True
        boss1t.x = boss1.x 
        miner.health -=10
        boss1t.setSpeed(3,270)
        for times in range(10):
            healthbar.nextFrame()
        clash.play()

    if item >= len(arrows):
        if mouse.LeftClick and miner.visible:
            arrowm.visible = True
            arrowm.moveTo(miner.x,miner.y)
            shooting.play()

    #to move boss back
    if arrowm.collidedWith(boss1) or arrowm.collidedWith(boss1t):
        boss1.visible = False
        boss1t.visible = True
        boss1t.x = boss1.x
        boss1t.setSpeed(3,270)
        clash.play()

    if boss1t.x > 650 and boss1t.visible:
        boss1.visible = True
        boss1t.visible = False
        boss1.x = boss1t.x
        boss1.setSpeed(2,90)

    #actual damage
    if arrowm.collidedWith(boss1) or arrowm.collidedWith(boss1t):
        arrowm.visible = False
        boss1.health -=5
        for times in range(10):
            healthbarb.nextFrame()

    if boss1.health <=0:
        if boss1.visible:
            boss1.visible = False
        if boss1t.visible:
            boss1t.visible = False
        healthbarb.visible = False
        portal.move()     
        
    if keys.Pressed[K_RIGHT] or keys.Pressed[K_d]:
        minerf.visible = False
        miner.visible = True
        miner.nextFrame()
        minerf.x = miner.x
        minerf.y = miner.y
        miner.x+=4
        
    elif keys.Pressed[K_LEFT] or keys.Pressed[K_a]:
        miner.visible = False
        minerf.visible = True
        minerf.nextFrame()
        miner.x = minerf.x
        miner.y = minerf.y        
        minerf.x-=5

    else:
        minerf.visible = False
        miner.visible = True
        minerf.x = miner.x
        minerf.y = miner.y
        
    if miner.visible:
        if miner.y< 500:
            landed = False#not landed

        else:
            landed = True
            
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True

        if jumping:
            miner.y -=27*factor#adjust for the drop
            #Make the character go up.  Factor creates a slowing effect to the jump
            factor*=fa#fall slowly
            landed = False
            #Since you are jumping you are no longer staying on land
            if factor < .18:
                jumping = False
                #Stop jumping once the slowing effect finishes
                factor = 1
            
        if not landed: #is jumping
            miner.y +=jh#adjust for the height of the jump - lower number higher jump

    if minerf.visible:
        if minerf.y< 500:
            landed = False#not landed

        else:
            landed = True
            
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True

        if jumping:
            minerf.y -=27*factor#adjust for the drop
            #Make the character go up.  Factor creates a slowing effect to the jump
            factor*=fa#fall slowly
            landed = False
            #Since you are jumping you are no longer staying on land
            if factor < .18:
                jumping = False
                #Stop jumping once the slowing effect finishes
                factor = 1
            
        if not landed: #is jumping
            minerf.y +=jh#adjust for the height of the jump - lower number higher jump

    #game.drawText("Items: " + str(item), 550, 300, f1)

    if miner.x >= portal.x + 2:
        for times in range(100 - miner.health):
            healthbar.prevFrame()
        game.over = True

    if miner.health <=0:
        while not game.over:
            game.processInput()
            game.scrollBackground("left",1)
            bk.draw()
            go.move()
            minerst.move()
            minerst.setSpeed(6,270)

            if minerst.move:
                minerst.nextFrame()
                
            if go.isOffScreen("right"):
                minerst.x = -100
                item +=1
                
            go.moveTo(minerst.x - 425,490)
            
            if mouse.LeftClick:
                game.quit()
    
            game.update(30)
            
    if mouse.RightClick:
        game.over = True

    game.update(30)

game.over = False

item = 0
miner.x = 100
miner.health = 100
portal.x = 950
arrowm.x = miner.x
arrowm.y = miner.y

#level 2 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while not game.over:
    game.processInput()
    game.scrollBackground("left",t)
    bk.draw()
    if item >= len(spears) + len(canb) + len(weapons):
        boss2.move()
        boss2t.move()
        for index in range(len(arrowt)):
            arrowt[index].move()
            if miner.collidedWith(arrowt[index],"rectangle") or minerf.collidedWith(arrowt[index],"rectangle"):
                arrowt[index].visible = False
                miner.health -=1
                healthbar.nextFrame()

    if item >= len(spears) + len(canb) + len(weapons):
        healthbarb.draw()
        healthbarb.visible = True
        
    mdle.move()
    mdlee.move()
    arrowm.move()
    miner.move()
    minerf.move()
    healthbar.draw()
    
    for index in range(len(spears)):
        spears[index].move()

        if miner.collidedWith(spears[index],"rectangle") or minerf.collidedWith(spears[index]):
            spears[index].visible = False
            miner.health -=2
            item +=1
            for times in range(2):
                healthbar.nextFrame()

        if spears[index].isOffScreen("left") and spears[index].visible:
            spears[index].visible = False
            item +=1
            
        if spears[index].isOffScreen("bottom") and spears[index].visible:
            spears[index].visible = False
            item +=1

    if item >= len(spears):   
        for index in range(len(weapons)):
            weapons[index].move()

            if miner.collidedWith(weapons[index],"rectangle") or minerf.collidedWith(weapons[index]):
                weapons[index].visible = False
                miner.health -=2
                item +=1
                for times in range(2):
                    healthbar.nextFrame()

            if weapons[index].isOffScreen("left") and weapons[index].visible:
                weapons[index].visible = False
                item +=1

        for index in range(len(canb)):
            canb[index].move()

            if miner.collidedWith(canb[index],"circle") or minerf.collidedWith(canb[index]):
                canb[index].visible = False
                miner.health -=3
                item +=1
                for times in range(3):
                    healthbar.nextFrame()

            if canb[index].isOffScreen("left") and canb[index].visible:
                canb[index].visible = False
                item +=1

    if boss2.collidedWith(miner) or boss2.collidedWith(minerf):
        boss2.visible = False
        boss2t.visible = True
        boss2t.x = boss2.x 
        miner.health -=10
        boss2t.setSpeed(4,270)
        for times in range(10):
            healthbar.nextFrame()
        clash.play()

    if item >= len(spears) + len(canb) + len(weapons):
        if mouse.LeftClick and miner.visible:
            arrowm.visible = True
            arrowm.moveTo(miner.x,miner.y)
            shooting.play()

    if arrowm.collidedWith(boss2) or arrowm.collidedWith(boss2t):
        boss2.visible = False
        boss2t.visible = True
        boss2t.x = boss2.x
        boss2t.setSpeed(4,270)
        clash.play()

    if boss2t.x > 600 and boss2t.visible:
        boss2.visible = True
        boss2t.visible = False
        boss2.x = boss2t.x
        boss2.setSpeed(3,90)

    if arrowm.collidedWith(boss2) or arrowm.collidedWith(boss2t):
        arrowm.visible = False
        boss2.health -=5
        for times in range(5):
            healthbarb.nextFrame()

    if boss2.health <=0:
        if boss2.visible:
            boss2.visible = False
        if boss2t.visible:
            boss2t.visible = False
        healthbarb.visible = False
        portal.move()

    if keys.Pressed[K_RIGHT] or keys.Pressed[K_d]:
        minerf.visible = False
        miner.visible = True
        miner.nextFrame()
        minerf.x = miner.x
        minerf.y = miner.y
        miner.x+=4
        
    elif keys.Pressed[K_LEFT] or keys.Pressed[K_a]:
        miner.visible = False
        minerf.visible = True
        minerf.nextFrame()
        miner.x = minerf.x
        miner.y = minerf.y        
        minerf.x-=5

    else:
        minerf.visible = False
        miner.visible = True
        minerf.x = miner.x
        minerf.y = miner.y
        
    if miner.visible:
        if miner.y< 500:
            landed = False#not landed

        else:
            landed = True
            
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True

        if jumping:
            miner.y -=27*factor#adjust for the drop
            #Make the character go up.  Factor creates a slowing effect to the jump
            factor*=fa#fall slowly
            landed = False
            #Since you are jumping you are no longer staying on land
            if factor < .18:
                jumping = False
                #Stop jumping once the slowing effect finishes
                factor = 1
            
        if not landed: #is jumping
            miner.y +=jh#adjust for the height of the jump - lower number higher jump

    if minerf.visible:
        if minerf.y< 500:
            landed = False#not landed

        else:
            landed = True
            
        if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
            jumping = True

        if jumping:
            minerf.y -=27*factor#adjust for the drop
            #Make the character go up.  Factor creates a slowing effect to the jump
            factor*=fa#fall slowly
            landed = False
            #Since you are jumping you are no longer staying on land
            if factor < .18:
                jumping = False
                #Stop jumping once the slowing effect finishes
                factor = 1
            
        if not landed: #is jumping
            minerf.y +=jh#adjust for the height of the jump - lower number higher jump

    #game.drawText("Items: " + str(item), 550, 300, f1)
    
    if miner.x >= portal.x + 2:
        for times in range(100 - miner.health):
            healthbar.prevFrame()
        game.over = True

    if miner.health <=0:
        while not game.over:
            game.processInput()
            game.scrollBackground("left",1)
            bk.draw()
            go.move()
            minerst.move()
            minerst.setSpeed(6,270)

            if minerst.move:
                minerst.nextFrame()
                
            if go.isOffScreen("right"):
                minerst.x = -100
                item +=1
                
            go.moveTo(minerst.x - 425,490)
            
            if mouse.RightClick:
                game.quit()
    
            game.update(30)

    if mouse.RightClick:
        game.over = True
      
    game.update(30)

game.over = False

minercs.x = -20
minercs.setSpeed(3,270)

#endscene
while not game.over: #need to find how to cancel screen if game over
    game.processInput()
    game.scrollBackground("left",0)
    bk.draw()
    minercs.move()

    if minercs.move:
        minercs.nextFrame()

    for index in range(len(miners)):
        miners[index].draw()

    if minercs.x > 300:
        minercs.setSpeed(0,270)
        minercs.prevFrame()
        ydi.draw()

    if mouse.LeftClick:
        game.over = True
    
    game.update(30)

game.quit()

