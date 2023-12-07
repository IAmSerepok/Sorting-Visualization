import pygame as pg
from random import randint
from SortFunction import *


class App:
    def __init__(self, size, num_range, delay):
        self.clock = pg.time.Clock()
        self.size = size
        self.arr = [randint(1, num_range) for i in range(size)]
        self.screen_size = self.screen_width, self.screen_height = 1200, 700
        self.width, self.height = self.screen_width // size, self.screen_height // num_range
        self.screen = pg.display.set_mode(self.screen_size)
        self.time, self.delay = 0, delay
        self.colors = {}
        self.running = False

        self.sort = InsertionSort(self)  # sort type

    def draw(self):
        self.screen.fill(pg.Color('black'))
        for i, num in enumerate(self.arr):
            col = self.colors.get(i, "gray")
            pg.draw.rect(self.screen, col, (i * self.width, self.screen_height - num * self.height,
                                            self.width - 2, num * self.height))

    def run(self):

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.running = not self.running
            
            if self.running and (self.time % self.delay == 0):
                self.sort.sort_step()
            self.draw()

            pg.display.flip()
            if self.running:
                self.time += 1
            self.clock.tick(self.clock.get_fps())


app = App(size=100, num_range=350, delay=1)
app.run()
