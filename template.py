import pygame, sys, time

from setup import BLACK

class Game:
    def __init__(self, title: str, full_screen=False, fps=60) -> None:        
        pygame.init()
        pygame.display.set_caption(title)

        info = pygame.display.Info()

        if full_screen:
            self.width = info.current_w
            self.height = info.current_h
        else:
            self.width = info.current_w//2
            self.height = info.current_h//2

        self.res_scale_x = self.width/1920
        self.res_scale_y = self.height/1080
             
        self.fps = fps
        self.window = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()

    def main_loop(self):
        self.start_time = time.perf_counter()
        while True:          
    
            self.manage_time()
            self.manage_mouse()
            self.manage_keyboard()
            self.show_to_screen()
            self.event_loop()
            
            self.clock.tick(self.fps)

    # Classes to overwrite
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  

    def manage_time(self):
        self.delta_t= (time.perf_counter()-self.start_time)*self.fps
        self.start_time = time.perf_counter()
    
    def manage_mouse(self):
        self.mx, self.my = pygame.mouse.get_pos()
        self.left, self.middle, self.right = pygame.mouse.get_pressed()

    def manage_keyboard(self):
        self.keys = pygame.key.get_pressed()
    
    
    def show_to_screen(self):
    
        self.window.fill(BLACK)
        pygame.display.update()


if __name__ == "__main__":
    Game("Test Title").main_loop()
