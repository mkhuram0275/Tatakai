from gamelib import *

game = Game(1024,384,"Tatakai")
bk = Animation ("images//bk1.png",120,game,7168/7,6912/18)
bk.resizeTo(game.width,game.height)
game.setBackground (bk)

Menubk = Image("images//Tlogo.png",game)
Menubk.resizeBy(-10)
KO = Image("images//KO!!!.png",game)
KO.resizeBy(-60)



Ryubreathe = Animation("images//Ryubreathe.png",6,game,198/3,196/2,1.5)
Ryubreathe.resizeBy(40)
Ryuwalk = Animation("images//Ryuwalk.png",6,game,246/3,212/2,4)
Ryuwalk.resizeBy(40)
Ryukick = Animation("images//Ryuforwardkick.png",6,game,462/3,258/2,3)
Ryukick.resizeBy(40)
Ultra = Animation("images//Ryuultra.png",19,game,1134/3,1015/7,2)
Ultra.resizeBy(40)
Ryujab = Animation("images//Ryupunch.png",4,game,226/2,210/2,3)
Ryujab.resizeBy(40)

Ryux = 280
Ryuy = 300
Ryustatus = "stand"

Rapbreathe = Animation("images//Rapbreathe.png",68,game,828/9,864/8,2)
Rapbreathe.resizeBy(40)
Rapwalk = Animation("images//rapwalk.png",12,game,384/4,342/3,3)
Rapwalk.resizeBy(40)
Rapfierce = Animation("images//rapfierce.png",9,game,534/3,468/3,2)
Rapfierce.resizeBy(40)
Rapkick = Animation("images//rapkick.png",18,game,524/4,500/5,2)
Rapkick.resizeBy(40)
Rappunch = Animation("images//rappunch.png",4,game,254/2,388/4,3)
Rappunch.resizeBy(40)
                      
Rapx =680
Rapy =300


Rapstatus = "stand"

title = Image("images//Tlogo.png",game)
Menubk.draw()
title.draw()
game.drawText("Press (SPACE) to play",320,300)
game.update(1)
game.wait(K_SPACE)


while not game.over:
    game.processInput()
    
    bk.draw()
    #ryulogic
    if keys.Pressed[K_d]:
        Ryustatus = "walkright"
        Ryux +=4

    elif keys.Pressed[K_a]:
        Ryustatus = "walkleft"
        Ryux -=4

    elif keys.Pressed[K_h]:
        Ryustatus = "kick"

    elif keys.Pressed[K_t]:
        Ryustatus = "ultra"

    elif keys.Pressed[K_f]:
        Ryustatus = "jab"

    elif keys.Pressed[K_b]:
        Ryustatus = "block"
    
    
        
        
    if not keys.Pressed[K_a] and not keys.Pressed[K_d]and not keys.Pressed[K_f]and not keys.Pressed[K_h] and not keys.Pressed[K_h] and not keys.Pressed[K_t]:
        Ryustatus = "stand"

    if Ryustatus == "walkleft":
        Ryuwalk.x = Ryux
        Ryuwalk.y = Ryuy
        Ryuwalk.prevFrame()

    elif Ryustatus == "walkright":
        Ryuwalk.x = Ryux
        Ryuwalk.y = Ryuy
        Ryuwalk.nextFrame()

    elif Ryustatus == "kick":
        Ryukick.moveTo(Ryux,Ryuy)
        if Ryux + 90 > Rapx:
            Rapbreathe.health -= 1


    elif Ryustatus == "ultra":
        Ultra.moveTo(Ryux,Ryuy)
        if Ryux + 150 > Rapx:
            Rapbreathe.health -= 1

    elif Ryustatus == "jab":
        Ryujab.moveTo(Ryux,Ryuy)
        if Ryux + 90 > Rapx:
            Rapbreathe.health -= 1


    elif Ryustatus == "block":
        Ryublock.x = Ryux
        Ryublock.y = Ryuy
        Ryublock.draw()
    
         
    else:
        Ryubreathe.moveTo(Ryux,Ryuy)
      
        
    #Raptorlogic
    if keys.Pressed[K_RIGHT]:
        Raptorstatus = "walkright"
        Rapx +=4

    elif keys.Pressed[K_LEFT]:
        Raptorstatus = "walkleft"
        Rapx -=4

    elif keys.Pressed[K_l]:
        Raptorstatus = "kick"

    elif keys.Pressed[K_i]:
        Raptorstatus = "ultra"

    elif keys.Pressed[K_j]:
        Raptorstatus = "jab"

        
    
        
        
    if not keys.Pressed[K_LEFT] and not keys.Pressed[K_RIGHT]and not keys.Pressed[K_l]and not keys.Pressed[K_i] and not keys.Pressed[K_j]:
        Raptorstatus = "stand"

    if Raptorstatus == "walkleft":
        Rapwalk.x = Rapx
        Rapwalk.y = Rapy
        Rapwalk.nextFrame()
    elif Raptorstatus == "walkright":
        Rapwalk.x = Rapx
        Rapwalk.y = Rapy
        Rapwalk.prevFrame()

    elif Raptorstatus == "kick":
        Rapkick.moveTo(Rapx,Rapy)
        if Rapx - 100 < Ryux:
            Ryubreathe.health -= 1

    elif Raptorstatus == "ultra":
        Rapfierce.moveTo(Rapx,Rapy)
        if Rapx - 100 < Ryux:
            Ryubreathe.health -= 1

    elif Raptorstatus == "jab":
        Rappunch.moveTo(Rapx,Rapy)
        if Rapx - 90 < Ryux:
            Ryubreathe.health -= 1
    else:
        Rapbreathe.moveTo(Rapx,Rapy)

    if Rapbreathe.health < 0 :
        game.over = True
        KO.draw()
        
    if Ryubreathe.health < 0 :
        game.over = True
        KO.draw()





    game.drawText("RH: " + str(Ryubreathe.health),5,5)
    game.drawText("RH: " + str(Rapbreathe.health),505,5)


    game.update(20)
#game.drawText("Game Over", 512,190)

game.update(1)
game.wait(K_SPACE)
game.quit()  
