from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height, speed):
        super().__init__()
        self.color_1 = color1
        self.color_2 = color2
        self.color_3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.speed = speed
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

   
window = display.set_mode((755, 755))
display.set_caption("Ping Pong")
background = transform.scale(image.load("bg.png"), (755, 755))
clock = time.Clock()
fps = 1050#ti
bol = GameSprite("bol.png", 333, 333, 100, 100, 5)
roketka1 = Wall(210, 105, 30, 10, 250, 5, 250, 5)
roketka2 = Wall(210, 105, 30, 745, 250, 5, 250, 5)
speed_x = bol.speed
speed_y = bol.speed
font.init()
font = font.Font(None, 50)
count1 = 0
count2 = 0
counter1 = font.render(str(count2), True, (255, 255, 255))
counter2 = font.render(str(count1), True, (255, 255, 255))


finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        bol.rect.x += speed_x
        bol.rect.y += speed_y

        if bol.rect.x <= 0:
            count2 += 1
            bol.rect.x = 333
        if bol.rect.x >= 755:
            count1 += 1
            bol.rect.x = 333

        if bol.rect.y > 755 - 100 or bol.rect.y < 0:
            speed_y *= -1
    if sprite.collide_rect(bol, roketka1):
        speed_x *= -1
    if sprite.collide_rect(bol, roketka2):
        speed_x *= -1

    window.blit(background, (0, 0))
    bol.reset()
    roketka1.draw_wall()
    roketka2.draw_wall()
    roketka1.update1()
    roketka2.update2()
    counter1 = font.render(str(count2), True, (255, 255, 255))
    counter2 = font.render(str(count1), True, (255, 255, 255))
    window.blit(counter1, (50, 0))
    window.blit(counter2, (705, 0))
    display.update()
