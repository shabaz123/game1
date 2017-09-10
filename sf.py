#!/usr/bin/python3
#############################################
# Experimenting with sprites - sf.py
# rev 1
#############################################

#import modules
import pygame
from pygame.locals import *
from background import Background
from ken import Ken

#some definitions
screenwidth=320
screenheight=200
btn_left=K_o
btn_right=K_p

###########  main function  ##################
def main():
  pygame.init()
  pygame.key.set_repeat(10,10) # keypresses to auto-repeat every 10msec
  rects=[] # create a list

  screen=pygame.display.set_mode((screenwidth, screenheight))
  background=Background("assets/stage_1.gif", [0,0])
  bgsurface=pygame.Surface(screen.get_size())
  bgsurface=bgsurface.convert() # speeds up blitting
  bgsurface.fill([0,0,255]) # set background to blue
  # we only use a portion of the background image, in this case (50,8) into it:
  bgsurface.blit(background.image.subsurface(50,8,screenwidth,screenheight), (0,0))
  screen.blit(bgsurface, [0,0]) # get the bgsurface onto the screen surface
  pygame.display.update() # update the entire display

  ken_sprite=Ken() # instantiate Ken!
  rects.append(ken_sprite.getrect()) # store all sprite rects we create into this list

  characters_group=pygame.sprite.Group(ken_sprite)

  while True: # this is a forever loop
    ev=pygame.event.poll()
    if ev.type==pygame.QUIT:
        pygame.quit()
        sys.exit(0)

    if ev.type==KEYDOWN: # button pressed?
      if (ev.key==btn_left):
        kenloc=[-1,0]
        ken_sprite.movepos(kenloc)
      elif (ev.key==btn_right):
        kenloc=[1,0]
        ken_sprite.movepos(kenloc)

    # clear the sprite(s) and then update and redraw them
    characters_group.clear(screen, bgsurface)
    characters_group.update()
    characters_group.draw(screen)
    pygame.display.update(rects)


###########  end of main function  ###########

if __name__=="__main__":
  main()


