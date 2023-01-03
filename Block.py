import pygame as pg
import Constants as c


class Block:
    def __init__(self, mass, size, x, vx, y=c.block_y):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.size = size
        self.rect = None

    def draw_on(self, surface):
        self.rect = pg.Rect((self.x - self.size//2, self.y - self.size//2, self.size, self.size))
        border = pg.Rect((self.x - 0.1 - self.size//2, self.y - 0.1 - self.size//2, self.size + 0.1, self.size + 0.1))
        s = pg.Surface((self.size, self.size))
        b = pg.Surface((self.size+0.1, self.size+0.1))
        s.fill((255, 255, 255))
        b.fill((0, 0, 0))

        surface.blit(s, self.rect)
        # surface.blit(b, border)

