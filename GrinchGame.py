import pygame
import sys

size = width, height = (550, 550)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60


def load_image(name):
    fullname = "images" + "/" + name
    try:
        if name[-2:] == "jpg":
            image = pygame.image.load(fullname).convert()
        else:
            image = pygame.image.load(fullname).convert_alpha()
    except:
        print("non lo trovo imagine: ", name)
        raise SystemExit()
    return image

def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    text = [
        "schermo",
        "",
        "il Grinch Rapisce il Natale",
        "Regole del gioco",
        "Regole del gioco2"]

    background = pygame.transform.scale(load_image("background.jpg"), (width, height))
    #background = load_image("background.jpg")
    screen.blit(background, (0, 0))

    pygame.font.init()
    font = pygame.font.Font(None, 40)
    text_coord = 50
    for line in text:
        string = font.render(line, 1, pygame.Color("blue"))
        string_rect = string.get_rect()
        text_coord += 10
        string_rect.top = text_coord
        string_rect.x = 135
        text_coord = text_coord + string_rect.height
        screen.blit(string, string_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)


def load_level(name):
    fullname = "images/" + name
    with open(fullname, "r") as map_file:
        level_map = []
        for line in map_file:
            line = line.strip()
            level_map.append(line)
    return level_map

def draw_level(level_map):
    new_player, x, y =None, None, None
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == ".":
                Tile("box.png", x, y)
            elif level_map[y][x] == "#":
                Tile("dark.png", x, y)
            elif level_map[y][x] == "@":
                Tile("box.png", x, y)
                new_player = Player(x, y)
    return new_player, x, y

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = load_image(tile_type)
        self.rect = self.image.get_rect().move(50 * pos_x, 50 * pos_y)
        self.add(tiles_group, all_sprites)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = load_image("grinch.png")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(50 * pos_x, 50 * pos_y)
        self.add(player_group, all_sprites)

    def move_up(self):
        self.rect = self.rect.move(0, -50)
    def move_down(self):
        self.rect = self.rect.move(0, +50)
    def move_left(self):
        self.rect = self.rect.move(-50, 0)
    def move_right(self):
        self.rect = self.rect.move(+50, 0)

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()

player, level_x, level_y = draw_level(load_level("level.txt"))

start_screen()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.move_up()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            player.move_down()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player.move_left()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player.move_right()

        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()
    clock.tick(fps)
terminate()

