class Character:
    def __init__(self, name, health, attack_power, defense, level, experience):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.experience = experience


    def attack_enemy(self, m):
        if self.health > 0 and m.health > 0:
            damage = self.attack_power - m.defense
            if damage < 0:
              damage = 0
              
            m.take_damage(damage)
            print(self.name, "attacked", m.name)


    def heal(self , n):
        if self.health > 0 and n > 0:
            self.health += n    
            if self.health > 100:
              self.health = 100                    
 
    def take_damage(self , x):
        if self.health > 0:
            self.health -= x
            if self.health <= 0:
              self.health = 0
              print(f'{self.name} died')

    def gain_experience(self , y):
        if y > 0:
             self.experience += y
             print(f'Your experience increased by {y} units.')
             self.level_up()

    def level_up(self):
        oldlevel = self.level
        while self.experience >= 20:
            self.level += 1
            self.experience -= 20

        if self.level > oldlevel:
            print(f'You leveled up! Current level: {self.level}')

    def show_status(self):
        print("Name:", self.name)
        print("Level:", self.level)
        print("Health:", self.health)
        print("experience:", self.experience)
