#Team Drive Name:Emergency Inc
#Group members:Edward Huang,Shaun Liberatore
#Game Name:Fruit Frenzy
from gamelib import*
#Problems in the game:
#LAGGGGGGGGGGGGGGGGGG
#The bite sound is very quit
#More lagggggggggggggggg
#The theme is currently disabled, turn back on at your own risk
#Not sure what else other other than that  

#All the Images
game=Game(800,600,"Fruit Frenzy")
bk=Image("FarmImage.jpg",game)
banana=Image("Banana1.png",game)
basket=Image("basket.png",game)
onion=Image("onion.png",game)
pepper=Image("redpepper.png",game)
pineapple=Image("pineapple1.png",game)
farmer=Animation("farmer.png",10,game,546/3,676/4)
burger=Image("burger1.png",game)
fries=Image("fries1.png",game)
hotdog=Image("dog1.png",game)
title=Image("Gametitle.png",game)
logo=Image("Company.png",game)
play=Image("Play1.png",game)
story=Image("Story1.png",game)
story1=Image("Story2.png",game)
gamestory=Image("gamestory3.png",game)
htp=Image("Howtoplay.png",game)
htp2=Image("Htp2.png",game)
htp3=Image("htp6.png",game)
f=Font(black,20,black,"Comic Sans MS")
F=Font(black,40,black,"Comic Sans MS")
wormr=Animation("worms2.png",8,game,440/2,640/4)
worml=Animation("worms1.png",8,game,440/2,640/4)
#Sound O.o
rooster=Sound("Rooster.wav",1)
laugh=Sound("hyena.wav",2)
bite=Sound("Biting_Apple.wav",3)
theme=Sound("cartoon_birds.wav",4)
win=Sound("slot_machine.wav",5)
#Lists
bananas=[]
peppers=[]
onions=[]
pineapples=[]
burgers=[]
hotdogs=[]
Fries=[]
#Resizing images,seting speeds and all those kinds of things
bk.resizeTo(800,600)
gamestory.resizeTo(700,300)
farmer.resizeBy(-50)
onion.resizeBy(-70)
pineapple.resizeBy(-65)
pepper.resizeBy(-65)
banana.resizeBy(-80)
basket.resizeBy(-20)
basket.moveTo(400,500)
s=randint(3,8)
wormr.setSpeed(s,270)
worml.setSpeed(s,90)
fruits=0
health=100
#Appending stuff
for index in range(500):
               bananas.append(Image("Banana1.png",game))
for index in range(500):
               speed=randint(4,8)
               bananas[index].setSpeed(speed,180)
               x=randint(100,700)
               y=-randint(100,10000)
               bananas[index].moveTo(x,y)
               bananas[index].resizeBy(-60)
               if bananas[index].isOffScreen("bottom"):
                                             banana.visible=False 
for index in range(500):
               pineapples.append(Image("pineapple1.png",game))
for index in range(500):
               speed=randint(4,8)
               pineapples[index].setSpeed(speed,180)
               x=randint(100,700)
               y=-randint(100,10000)
               pineapples[index].moveTo(x,y)
               pineapples[index].resizeBy(-60)
               if pineapples[index].isOffScreen("bottom"):
                                             pineapple.visible=False 
for index in range(500):
               onions.append(Image("onion.png",game))
for index in range(500):
               speed=randint(4,8)
               onions[index].setSpeed(speed,180)
               x=randint(100,700)
               y=-randint(100,10000)
               onions[index].moveTo(x,y)
               onions[index].resizeBy(-70)
               if onions[index].isOffScreen("bottom"):
                                             onion.visible=False
for index in range(500):
               peppers.append(Image("redpepper.png",game))
for index in range(500):
               speed=randint(4,8)
               peppers[index].setSpeed(speed,180)
               x=randint(100,700)
               y=-randint(100,10000)
               peppers[index].moveTo(x,y)
               peppers[index].resizeBy(-75)
               if peppers[index].isOffScreen("bottom"):
                                             pepper.visible=False
for index in range(500):
               burgers.append(Image("burger1.png",game))
for index in range(500):
               speed=randint(4,8)
               burgers[index].setSpeed(speed,180)
               x=randint(100,700)
               y=-randint(100,10000)
               burgers[index].moveTo(x,y)
               burgers[index].resizeBy(-65)
               if burgers[index].isOffScreen("bottom"):
                                             burger.visible=False
for index in range(500):
               Fries.append(Image("fries1.png",game))
for index in range(500):
               speed=randint(4,8)
               Fries[index].setSpeed(speed,180)
               x=randint(100,700)
               y=-randint(100,10000)
               Fries[index].moveTo(x,y)
               Fries[index].resizeBy(-65)
               if Fries[index].isOffScreen("bottom"):
                                             fries.visible=False
for index in range(500):
               hotdogs.append(Image("dog1.png",game))
for index in range(500):
               speed=randint(4,8)
               hotdogs[index].setSpeed(speed,180)
               x=randint(100,700)
               y=-randint(100,10000)
               hotdogs[index].moveTo(x,y)
               hotdogs[index].resizeBy(-65)
               if hotdogs[index].isOffScreen("bottom"):
                                             hotdog.visible=False 
#Title Screen
while not game.over:
               game.processInput()
               bk.draw()
               title.draw()
               title.moveTo(400,90)
               play.draw()
               play.moveTo(400,500)
               logo.draw()
               logo.moveTo(400,175)
               story.draw()
               story.moveTo(400,400)
               htp.draw()
               htp.moveTo(400,300)
               htp2.draw()
               htp2.visible=False
               htp3.draw()
               htp3.visible=False
               story.visible=True
               htp.visible=True
               logo.visible=True
               title.visible=True
               play.visible=True
               story1.draw()
               story1.visible=False
               gamestory.draw()
               gamestory.visible=False
               if mouse.collidedWith(htp)and mouse.LeftButton:
                              htp3.visible=True
                              htp2.visible=True
                              htp2.moveTo(400,75)
                              logo.visible=False
                              play.visible=False
                              htp.visible=False
                              title.visible=False
                              story.visible=False
               if mouse.collidedWith(story) and mouse.LeftButton:
                              gamestory.visible=True
                              story1.visible=True
                              story1.moveTo(400,75)
                              logo.visible=False
                              play.visible=False
                              htp.visible=False
                              title.visible=False
                              story.visible=False
               if mouse.collidedWith(play)and mouse.LeftClick:
                              game.over=True
                              rooster.play()

               game.update(60)

game.over=False

#Practice(level 0)
while not game.over:
               game.processInput()
               bk.draw()
               farmer.draw()
               'theme.play()'
               farmer.moveTo(50,75)
               for index in range(100):
                              bananas[index].move()
               for index in range(100):
                              pineapples[index].move()
               basket.draw()
               game.drawText("Level 0",300,50,f)
               game.drawText("Food Collected:" +str(fruits),75,100)
               game.drawText("Farmer Health:"+str(health),75,75)
               for index in range(100):
                              if bananas[index].collidedWith(basket)and banana.visible:
                                             fruits+=1
                                             bananas[index].visible=False
                              if pineapples[index].collidedWith(basket)and pineapple.visible:
                                             fruits+=1
                                             pineapples[index].visible=False  
                                             
               if keys.Pressed[K_LEFT]:
                              basket.x-=5
               if keys.Pressed[K_RIGHT]:
                              basket.x+=5
               if keys.Pressed[K_UP]:
                              basket.y-=5
               if keys.Pressed[K_DOWN]:
                              basket.y+=5
               if fruits>99:
                              game.over=True
               game.update(60)

game.over=False

#level 1
while not game.over:
               game.processInput()
               bk.draw()
               'theme.play()'
               farmer.draw()
               farmer.moveTo(50,75)
               for index in range(50):
                              bananas[index].move()
               for index in range(50):
                              pineapples[index].move()
               for index in range(50):
                              onions[index].move()
               for index in range(50):
                              peppers[index].move()
               for index in range(15):
                              burgers[index].move()
               for index in range(15):
                              Fries[index].move()
               for index in range(15):
                              hotdogs[index].move() 
               basket.draw()
               game.drawText("Level 1",300,50,f)
               game.drawText("Food Collected:" +str(fruits),75,100)
               game.drawText("Farmer Health:"+str(health),75,75)
               for index in range(50):
                              if bananas[index].collidedWith(basket)and banana.visible:
                                             fruits+=1
                                             bananas[index].visible=False
                              if pineapples[index].collidedWith(basket)and pineapple.visible:
                                             fruits+=1
                                             pineapples[index].visible=False 
               for index in range(50):
                              if onions[index].collidedWith(basket)and onion.visible:
                                             fruits+=1
                                             onions[index].visible=False
                              if peppers[index].collidedWith(basket)and pepper.visible:
                                             fruits+=1
                                             peppers[index].visible=False
               for index in range(25):
                              if burgers[index].collidedWith(basket)and burger.visible:
                                             health-=5
                                             burgers[index].visible=False
                                             farmer.resizeBy(5)
                              if hotdogs[index].collidedWith(basket)and hotdog.visible:
                                             health-=5
                                             hotdogs[index].visible=False
                                             farmer.resizeBy(5)
                              if Fries[index].collidedWith(basket)and fries.visible:
                                             health-=5
                                             Fries[index].visible=False
                                             farmer.resizeBy(5)
               if keys.Pressed[K_LEFT]:
                              basket.x-=5
               if keys.Pressed[K_RIGHT]:
                              basket.x+=5
               if keys.Pressed[K_UP]:
                              basket.y-=5
               if keys.Pressed[K_DOWN]:
                              basket.y+=5
               if fruits>149:
                              game.over=True
               if health<5:
                              game.over=True
               game.update(60)
game.over=False

x=-randint(300,5000)
y=randint(100,500)
wormr.moveTo(x,y)
#Level 2
while not game.over and health>0:
               game.processInput()
               bk.draw()
               'theme.play()'
               farmer.draw()
               farmer.moveTo(50,75)
               wormr.move()
               if wormr.isOffScreen("right"):
                              x=-randint(300,5000)
                              y=randint(100,500)
                              wormr.moveTo(x,y) 
               for index in range(100):
                              bananas[index].move()
               for index in range(100):
                              pineapples[index].move()
               for index in range(100):
                              onions[index].move()
               for index in range(100):
                              peppers[index].move()
               for index in range(30):
                              burgers[index].move()
               for index in range(30):
                              Fries[index].move()
               for index in range(30):
                              hotdogs[index].move()
               basket.draw()
               game.drawText("Level 2",300,50,f)
               game.drawText("Food Collected:" +str(fruits),75,100)
               game.drawText("Farmer Health:"+str(health),75,75)
               for index in range(100):
                              if bananas[index].collidedWith(basket)and banana.visible:
                                             fruits+=1
                                             bananas[index].visible=False
                              if pineapples[index].collidedWith(basket)and pineapple.visible:
                                             fruits+=1
                                             pineapples[index].visible=False
                              if wormr.collidedWith(bananas[index]):
                                             bananas[index].visible=False
                                             bite.play()
                              if wormr.collidedWith(pineapples[index]):
                                             pineapples[index].visible=False
                                             bite.play()
               for index in range(100):
                              if onions[index].collidedWith(basket)and onion.visible:
                                             fruits+=1
                                             onions[index].visible=False
                              if peppers[index].collidedWith(basket)and pepper.visible:
                                             fruits+=1
                                             peppers[index].visible=False
                              if burgers[index].collidedWith(basket)and burger.visible:
                                             health-=5
                                             burgers[index].visible=False
                                             farmer.resizeBy(5)
                              if Fries[index].collidedWith(basket)and fries.visible:
                                             health-=5
                                             Fries[index].visible=False
                                             farmer.resizeBy(5)
                              if hotdogs[index].collidedWith(basket)and hotdog.visible:
                                             health-=5
                                             hotdogs[index].visible=False
                                             farmer.resizeBy(5)
                              if wormr.collidedWith(onions[index]):
                                             onions[index].visible=False
                                             bite.play()
                              if wormr.collidedWith(peppers[index]):
                                             peppers[index].visible=False
                                             bite.play()
               if keys.Pressed[K_LEFT]:
                              basket.x-=5
               if keys.Pressed[K_RIGHT]:
                              basket.x+=5
               if keys.Pressed[K_UP]:
                              basket.y-=5
               if keys.Pressed[K_DOWN]:
                              basket.y+=5
               if fruits>199:
                              game.over=True
               if health<5:
                              game.over=True
               game.update(60)
game.over=False

for index in range(500):
               bananas[index].visible=True
               peppers[index].visible=True
               onions[index].visible=True
               pineapples[index].visible=True
               Fries[index].visible=True
               burgers[index].visible=True
               hotdogs[index].visible=True
x=-randint(300,5000)
y=randint(100,500)
wormr.moveTo(x,y)
x=randint(300,5000)
y=randint(100,500)
worml.moveTo(x,y)

#Level 3
while not game.over and health>0:
               game.processInput()
               bk.draw()
               'theme.play()'
               farmer.draw()
               farmer.moveTo(50,75)
               wormr.move()
               if wormr.isOffScreen("right"):
                              x=-randint(300,5000)
                              y=randint(100,500)
                              wormr.moveTo(x,y)
               worml.move()
               if worml.isOffScreen("left"):
                              x=randint(300,5000)
                              y=randint(100,500)
                              worml.moveTo(x,y) 
               
               for index in range(100):
                              bananas[index].move()
               for index in range(100):
                              pineapples[index].move()
               for index in range(100):
                              onions[index].move()
               for index in range(100):
                              peppers[index].move()
               for index in range(50):
                              burgers[index].move()
               for index in range(50):
                              Fries[index].move()
               for index in range(50):
                              hotdogs[index].move()
               basket.draw()
               game.drawText("Level 3",300,50,f)
               game.drawText("Food Collected:" +str(fruits),75,100)
               game.drawText("Farmer Health:"+str(health),75,75)
               for index in range(100):
                              if bananas[index].collidedWith(basket)and banana.visible:
                                             fruits+=1
                                             bananas[index].visible=False
                              if pineapples[index].collidedWith(basket)and pineapple.visible:
                                             fruits+=1
                                             pineapples[index].visible=False
                              if wormr.collidedWith(bananas[index]):
                                             bananas[index].visible=False
                                             bite.play()
                              if wormr.collidedWith(pineapples[index]):
                                             pineapples[index].visible=False
                                             bite.play()
                              if worml.collidedWith(bananas[index]):
                                             bananas[index].visible=False
                                             bite.play()
                              if worml.collidedWith(pineapples[index]):
                                             pineapples[index].visible=False
                                             bite.play()
               for index in range(100):
                              if onions[index].collidedWith(basket)and onion.visible:
                                             fruits+=1
                                             onions[index].visible=False
                              if peppers[index].collidedWith(basket)and pepper.visible:
                                             fruits+=1
                                             peppers[index].visible=False
                                             farmer.resizeBy(5)
                              if burgers[index].collidedWith(basket)and burger.visible:
                                             health-=5
                                             burgers[index].visible=False
                                             farmer.resizeBy(5)
                              if Fries[index].collidedWith(basket)and fries.visible:
                                             health-=5
                                             Fries[index].visible=False
                                             farmer.resizeBy(5)
                              if hotdogs[index].collidedWith(basket)and hotdog.visible:
                                             health-=5
                                             hotdogs[index].visible=False
                                             farmer.resizeBy(5)
                              if wormr.collidedWith(onions[index]):
                                             onions[index].visible=False
                                             bite.play()
                              if wormr.collidedWith(peppers[index]):
                                             peppers[index].visible=False
                                             bite.play()
                              if worml.collidedWith(onions[index]):
                                             onions[index].visible=False
                                             bite.play()
                              if worml.collidedWith(peppers[index]):
                                             peppers[index].visible=False
                                             bite.play()
               if keys.Pressed[K_LEFT]:
                              basket.x-=5
               if keys.Pressed[K_RIGHT]:
                              basket.x+=5
               if keys.Pressed[K_UP]:
                              basket.y-=5
               if keys.Pressed[K_DOWN]:
                              basket.y+=5
               if fruits>224:
                              game.over=True
               if health<5:
                              game.over=True
               game.update(60)
game.over=False


#Ze End Screen if you lose

while not game.over and health<5 and fruits<225:
               game.processInput()
               game.drawText("You ate too much Fast food (^_^)",150,250,F)
               laugh.play()
               
               game.update(60)

game.over=False

#The end screen if you win
while not game.over and fruits>224 and health>0:
               game.processInput()
               game.drawText("You Win!",200,300,F)
               win.play()


               game.update(60)

game.quit()
