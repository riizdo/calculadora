import pygame, sys
from pygame.locals import * 

class Calculadora():
    
    def __init__(self):
        
        #iniciamos pygame
        pygame.init()
        
        #inicializamos la pantalla
        self.__screenSize = (400, 600)
        self.__screen = pygame.display.set_mode(self.__screenSize)
        pygame.display.set_caption("Calculadora")
        
        
    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.fin()
                    
                    
    def fin(self):
        pygame.quit()
        sys.exit()
        
        
if __name__ == '__main__':
    calculadora = Calculadora()