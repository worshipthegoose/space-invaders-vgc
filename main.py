"GLOBAL: Imports and Initialization"
import pygame, random, sys
pygame.init()
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
