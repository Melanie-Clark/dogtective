import pygame as p
# from logic.components.entity import Entity
from user_interface.game_config import HEIGHT, WIDTH

# class for NPC and player entities
class Character(p.sprite.Sprite):

    def __init__(self, name, health=5):
        super().__init__()
        self.health = health
        self.x = 50
        self.y = HEIGHT / 2
        self.vel = 4
        self.width = 100
        self.height = 50

        self.dog1 = p.image.load('../logic/assets/images/characters/dogtective_sprite/Idle.png').convert_alpha()
        # set width and height for dog image 1
        self.dog1 = p.transform.scale(self.dog1, (self.width, self.height))
        # set width and height for dog image 2
        self.dog2 = p.transform.flip(self.dog1, True, False)  # flips dog image 1 to face the other direction

        self.image = self.dog1
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)

    def update(self):
        self.movement()
        self.correction()
        # self.checkCollision()
        self.rect.center = (self.x, self.y)

    def movement(self):
        keys = p.key.get_pressed()

        if keys[p.K_LEFT]:
            self.x -= self.vel
            #left key pressed negative velocity
            self.image = self.dog2 #switch to dog image 2


        elif keys[p.K_RIGHT]:
            self.x += self.vel
            #right key pressed positive velocity
            self.image = self.dog1 #switch to dog image 1

        if keys[p.K_UP]:
            self.y -= self.vel
            # left key up negative velocity

        elif keys[p.K_DOWN]:
            self.y += self.vel
            # right key down positive velocity

    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2 #prevents dog from going off of the screen on the right side of the screen

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2 #prevents dog from going off of the screen on the left side of the screen

        if self.y - self.width / 2 < 0:
            self.y = self.width / 2 #prevents dog from going off of the screen on the top of the screen

        elif self.y + self.width / 2 > WIDTH:
            self.y = WIDTH - self.width / 2 #prevents dog from going off of the screen on the bottom of the screen

    # def checkCollision(self):
    #     car_check = p.sprite.spritecollide(self, car_group, False, p.sprite.collide_mask)
    #     if car_check:
    #         # explosion.explode(self.x, self.y)
    #         print("hit by car")

    def collision_damage(self, damage):
        self.health -= damage
        # print(f"{self.name} took {damage} damage. Remaining health: {self.health}")

    def __str__(self):
        return f"{self.name}: Health ({self.health})"


# sample outputs for testing only:
if __name__ == "__main__":
    a = Character("Kharma Chameleon")
    print(a)
    a.collision_damage(10)