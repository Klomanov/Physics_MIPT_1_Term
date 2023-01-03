import pygame as pg
import pygame.draw

from Block import Block
import Constants as c


class App:

    def __init__(self):
        self.finished = False
        self.screen = pg.display.set_mode((c.screen_weight, c.screen_height))
        self.clock = pg.time.Clock()
        self.block1 = Block(c.block1_mass, c.block1_size, 100, 0, y=c.block_y-c.line_size//2)
        self.block2 = Block(c.block2_mass, c.block2_size, 300, -0.05, y=c.block_y-c.block2_size//2 + c.block1_size//2 - c.line_size//2)
        self.count = 0
        self.colliding = False
        pg.font.init()

    def run(self):
        while not self.finished:
            self.clock.tick(c.FPS)
            self.draw_all()
            self.physics_processes()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.finished = True

    def draw_all(self):
        self.screen.fill(c.grey)
        f1 = pg.font.Font(None, 36)
        text1 = f1.render(str(self.count), True,
                          (255, 255, 255))
        self.screen.blit(text1, (20 + c.border_align + c.line_size, 50))
        pygame.draw.line(self.screen, c.line_color, (c.border_align, c.block_y + c.block1_size//2), (c.screen_weight, c.block_y + c.block1_size//2), c.line_size)
        pygame.draw.line(self.screen, c.line_color, (c.border_align, 0), (c.border_align, c.block_y + c.block1_size//2), c.line_size)
        pygame.draw.rect(self.screen, c.black, (0, 0, c.border_align, c.screen_height))
        pygame.draw.rect(self.screen, c.black, (0, c.block_y + c.line_size//2 + c.block1_size//2, c.screen_weight, c.screen_height))
        self.block1.draw_on(self.screen)
        self.block2.draw_on(self.screen)
        pg.display.update()

    def physics_processes(self):
        def bump():
            old_vx1 = self.block1.vx
            self.block1.vx = (self.block1.mass - self.block2.mass) / (self.block1.mass + self.block2.mass) * \
                             self.block1.vx + 2 * self.block2.mass / (
                                     self.block1.mass + self.block2.mass) * self.block2.vx
            self.block2.vx = (self.block2.mass - self.block1.mass) / (self.block1.mass + self.block2.mass) * \
                             self.block2.vx + 2 * self.block1.mass / (
                                     self.block1.mass + self.block2.mass) * old_vx1
            self.count += 1
        if self.block1.x + self.block1.vx <= self.block1.size//2 + c.line_size//2 + c.border_align:
            self.block1.x = self.block1.size//2 + c.line_size//2 + c.border_align
            self.block1.vx = - self.block1.vx
            self.count += 1

        if self.block1.x + self.block1.size//2 + self.block1.vx >= self.block2.x + self.block2.vx - self.block2.size//2:
            bump()
            if self.block1.vx != 0 and self.block2.vx != 0:
                dx1 = (self.block1.size//2 + self.block2.size//2 + self.block1.x - self.block2.x)/(self.block2.vx/self.block1.vx - 1)
                dx2 = self.block2.vx * dx1 / self.block1.vx
                self.block1.x += dx1
                #self.block2.x += dx2

        elif self.block1.x + self.block1.vx >= self.block1.size//2 + c.line_size//2 + c.border_align:
            self.block1.x += self.block1.vx
            self.block2.x += self.block2.vx


if __name__ == "__main__":
    App().run()
