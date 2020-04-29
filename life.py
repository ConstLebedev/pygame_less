import pygame


class Field:
    def __init__(self, screen, rows, cols, left=0, top=0, cell_size=30):
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.left = left
        self.top = top
        self.field = [[0] * cols for _ in range(rows)]

    def render(self):
        for y in range(self.rows):
            for x in range(self.cols):
                if self.field[x][y]:
                    pygame.draw.rect(self.screen, pygame.Color('red'),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size + self.left, self.cell_size + self.top), )
                pygame.draw.rect(self.screen, pygame.Color('white'),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size + self.left, self.cell_size + self.top), 1)

    def on_click(self, cell):
        y, x = cell
        self.field[x][y] = not self.field[x][y]

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= cell_x <= self.cols and 0 <= cell_y <= self.rows:
            return cell_y, cell_x

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    size = 320, 320
    screen = pygame.display.set_mode(size)

    board = Field(screen, 10, 10, 10, 10)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render()
        pygame.display.flip()

    pygame.quit()
