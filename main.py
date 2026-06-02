"GLOBAL: Imports and Initialization + Fill Display"
import pygame
pygame.init()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")
FPS = 60
clock = pygame.time.Clock()

"Riker: ALIEN CLASS"
class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # More
        self.starting_x = x
        self.starting_y = y
        self.direction = 1
        self.velocity = velocity 
        self.bullet_group = bullet_group
        self.shoot_sound = pygame.mixer.Sound("assets/alien_fire.wav")
    def update(self):
        self.rect.x = self.rect.x + self.direction * self.velocity
        if random.randint(0,1000) > 999 and len(self.bullet_group) < 3:
            self.shoot_sound.play()
            self.fire()
        def fire(self):
            # Fire in the hole
            AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)
        def reset(self):
            self.rect.topleft = (self.starting_x, self.starting_y)
            self.direction = 1
class PlayerBullet (pygame.sprite.Sprite):
    def __init__(self,x,y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("green_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = 10
        bullet_group.add(self)
    def update(self):
        self.rect.y -= self.velocity
        if self.rect.bottom < 0:
            self.kill()

class AlienBullet (pygame.sprite.Sprite):
    def __init__(self,x,y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("red_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = 10
        bullet_group.add(self)
    def update(self):
        self.rect.y += self.velocity
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

class Player(pygame.sprite.Sprite):
    """A class to model a spaceship the user can control"""
    def __init__(self, bullet_group):
        """Initialize the player"""
        super().__init__()
        self.image = pygame.image.load("player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT
        self.lives = 5
        self.velocity = 8
        self.bullet_group = bullet_group
        self.shoot_sound = pygame.mixer.Sound("player_fire.wav")
    def update(self):
        """Update the player"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
    def fire(self):
        """Fire a bullet"""
        if len(self.bullet_group) < 2:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)
    def reset(self):
        """Reset the players position"""
        self.rect.centerx = WINDOW_WIDTH//2
"Riker: Create Bullets"
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()

#Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group)
my_player_group.add(my_player)

#Create an alien group.  Will add Alien objects via the game's start new round method
my_alien_group = pygame.sprite.Group()

#Create a Game object
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
my_game.start_new_round()
"Riker: MAIN game loop"
def main():
    global display_surface
    BLACK = (0, 0, 0)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
                break
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    my_player.fire()
        display_surface.fill(BLACK)
        my_player_group.update()
        my_player_group.draw(display_surface)
        my_alien_group.update()
        my_alien_group.draw(display_surface)
        my_player_bullet_group.update()
        my_player_bullet_group.draw(display_surface)
        my_alien_bullet_group.update()
        my_alien_bullet_group.draw(display_surface)
        #Update and draw Game object
        my_game.update()
        my_game.draw()
        #Update the display and tick clock by FPS
        pygame.display.flip()
        clock.tick(FPS)
if __name__ == "__main__":
    main()
pygame.quit() # Quits pygame.

