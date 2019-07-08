class StarwarsUniverse:
# creates a member of the starwars universe

    def __init__(self, name, birth, gender):
        self._name = name
        self.birth = birth
        self.gender = gender

    def says(self, words):
        return f"{self.name} says {words}"

class Robot(StarwarsUniverse):
# creates a robot from the startwars universe

    def __init__(self, name, birth, gender, classification, sidekick=None):
        super() .__init__(name, birth, gender)
        self.birth = birth
        self.classification = classification

        if sidekick is not None:
            self.sidekick_name, self.sidekick_type = sidekick

        self._skills = {
            'Language Translation': False,
            'Facial Recognition': False,
            'Emotion Sensing': False,
            'Mechanical Repair': False,
            'Flying': False,
            'Cleaning': False,
            'Medical Assistance': False,
            'Surveillance': False,
            'Combat': False,
            'Communications': False,
            'Meal Preperation': False,
            'Search and Rescue': False,
            'Infiltration': False,
        }

class Human(StarwarsUniverse):
#creates a human from the starwarsuniverse
    def __init__(self, name, birth, gender, expertise, side=None):
        super() .__init__(name, birth, gender)
        self.expertise = expertise
        self.side = side

class Alien(StarwarsUniverse):
# Creates an alien
    def __init__(self, name, birth, gender, species, side=None):
        super() .__init__(name, birth, gender)
        self.species = species

        if side is not None:
            self.side = side

if __name__ == "__main__":
    rey = StarwarsUniverse("Rey", "2015", "female")
    print(rey.says("I don't know your name"))

    c3po = Robot(name="C-3PO", birth=1977, gender="NB", classification="droid", sidekick=("R2D2", "droid"))



    