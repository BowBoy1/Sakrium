# SAKRIUM
# 2023 Charlie's Game Jam

#Normal Imports
# from superwires import games (not used currently)

#Imports from other files
import LibraryInstaller
from consts import *

# Libraries to check and install
# libraries = ['pygame', 'pygame_gui', 'superwires']
libraries = ['pygame', 'pygame_gui']

# Check and install libraries if necessary
for library in libraries:
   LibraryInstaller.check_library(library)

# Imports from external libraries
import pygame
import pygame_gui
import sys
import os
from enum import Enum

# Begin game

pause = False

# Differentiate which screen the player is in (pause, main menu, in-game, etc)
class Page(Enum):
   START = 0
   GAME = 1

pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Sakrium - Charlie's Game Jam 2023")

bg = pygame.Surface(screen_size) # Background
bg.fill(pygame.Color(grey))

manager = pygame_gui.UIManager(screen_size, os.path.join(os.getcwd(), "./source/theme.json"))

clock = pygame.time.Clock()

page = Page.START

# Text Boxes
game_title = pygame_gui.elements.UILabel(text="Sakrium", relative_rect=pygame.Rect((340, 32), (600, 150)), manager=manager, object_id=pygame_gui.core.ObjectID(class_id="@main_menu", object_id="#game_title"))

# Buttons
start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((490, 285), (300, 150)), text="Play", manager=manager, object_id=pygame_gui.core.ObjectID(class_id="@main_menu", object_id="#start_button"))

# Pause Menu
pause_overlay = pygame_gui.elements.UIPanel(
   relative_rect=pygame.Rect((0, 0), screen_size),
   manager=manager,
   object_id=pygame_gui.core.ObjectID(class_id="@pause_overlay", object_id="#pause_overlay"),
   visible=pause
)

paused_label = pygame_gui.elements.UILabel(
   relative_rect=pygame.Rect((16, 16), (110, 40)),
   text="Paused",
   manager=manager,
   container=pause_overlay,
   object_id=pygame_gui.core.ObjectID(class_id="@pause_overlay", object_id="#paused_label")
)

ui_by_page = {
   Page.START: [game_title, start_button],
   Page.GAME: []
}

# Game loop
while True:
   dt = clock.tick(fps) / 1000
   
   for event in pygame.event.get():
      match event.type:
         case pygame.QUIT:
            pygame.quit()
            sys.exit()
         
         case pygame.KEYDOWN:
            match event.key:
               case 27: # Esc
                  pause = not pause
                  if page == Page.GAME:   
                     if pause:
                        pause_overlay.show()
                     else:
                        pause_overlay.hide()
                  else:
                     pause_overlay.hide()
                     
         
         case pygame_gui.UI_BUTTON_PRESSED:
            match event.ui_element:
               case start_button:
                  page = Page.GAME
      
      manager.process_events(event)
   
   manager.update(dt)
   
   screen.blit(bg, (0, 0))
   
   for elements in ui_by_page.values():
      for element in elements:
         element.hide()

   for element in ui_by_page.get(page, []):
      element.show()
      
   # if not pause:
      # game calculations
      
   # match page:
   #    case Page.GAME:
         # draw the game itself
   
   manager.draw_ui(screen)
   pygame.display.update()