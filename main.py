import backdrop as backdrop
import pygame
import os
import sys


'''
Variables
'''

main = True

worldx = 960
worldy = 720
fps = 20
ani = 4
world = pygame.display.set_mode([worldx, worldy])

pygame.display.set_caption("3 FAZ Dungeon Crawler")

BLUE  = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)



'''
Objects
'''

class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames
        self.images = []
        img = pygame.image.load(os.path.join('images', 'player.png'))
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.frame = 0
        self.health = 10

    def control(self, x, y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
        update sprite position
        '''
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            self.health -= 1
            print(self.health)

class Enemy(pygame.sprite.Sprite):
    """
        Spawn an enemy
        """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'monster2.png'))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0  # counter variable

    def move(self):
        '''
        enemy movement
        '''
        distance = 80
        speed = 8

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1

class Level():
    def bad(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'monster2.png') # spawn enemy
            enemy_list = pygame.sprite.Group()  # create enemy group
            enemy_list.add(enemy)  # add enemy to group
        if lvl == 2:
            print("Level " + str(lvl))

        return enemy_list


'''
Setup
'''

clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'background.png'))
backdropbox = world.get_rect()
main = True


player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 30   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10 # how many pixels move



enemy = Enemy(300,0,' monster2.png')    # spawn enemy
eloc = []
eloc = [300, 0]
enemy_list = Level.bad(1, eloc)
enemy_list = pygame.sprite.Group()   # create enemy group
enemy_list.add(enemy)                # add enemy to group




'''
Main loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'): # left
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'): # right
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'): # jump
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == ord('a'): # left
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'): # right
                player.control(steps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    player.update()
    world.blit(backdrop, backdropbox)
    player_list.draw(world)
    enemy_list.draw(world)
    for e in enemy_list:
        e.move()
    pygame.display.flip()
    clock.tick(fps)