####################################
# ken.py
# rev. 1
####################################

# definitions
import sys
import pygame

# functions
def load_frame(fname):
  img=pygame.image.load(fname)
  return img

# the Ken class (inherits from Sprite class) and its member functions
class Ken(pygame.sprite.Sprite):
  def __init__(self): # this gets called when a Ken object is instantiated
    super(Ken, self).__init__()
    self.frames=[] # create a member list called images
    # the frames for the sprite!
    self.frames.append(load_frame("assets/ken_idle_1.gif"))
    self.frames.append(load_frame("assets/ken_idle_2.gif"))
    self.frames.append(load_frame("assets/ken_idle_3.gif"))
    self.frames.append(load_frame("assets/ken_idle_4.gif"))

    self.idx=0 # create an idx member variable to reference the frame
    self.incr=0 # create a variable to pace the sprite animation
    self.frame_period=800 # set frames to update at this period
    self.image=self.frames[self.idx]
    self.rect=pygame.Rect(5, 100, 50, 90) # defines an area sixe 50x90 at pos (5,100)

  def getrect(self):
    return self.rect

  def movepos(self, loc):
    self.rect.move_ip(loc[0], loc[1]);

  def update(self):
    self.incr=self.incr+1
    if (self.incr>self.frame_period): # is it time for incrementing the frame?
      self.incr=0
      self.idx=self.idx+1 # increment the frame reference (idx)
      if (self.idx >= len(self.frames)): # loop animation so that it restarts
        self.idx=0

    self.image=self.frames[self.idx] 


