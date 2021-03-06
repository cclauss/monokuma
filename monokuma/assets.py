from datetime import date
from measurement.measures.mass import Mass
from measurement.measures.distance import Distance

genders = ['male', 'female', 'na']


class Character(object):
    def __init__(self, first_name: str, last_name: str, gender: str, talent: str, height: Distance, birth_month: int,
                 birth_day: int, chest: Distance, weight: Mass, main_game: str):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.talent = talent
        self.height = height
        self.b_day = (birth_month, birth_day)
        self.chest = chest
        self.weight = weight
        self.main_game = main_game

    @property
    def next_birthday(self):
        now = date.today()
        this_year_bday = date(now.year, self.b_day[0], self.b_day[1])
        if this_year_bday < now:
            return date(now.year + 1, self.b_day[0], self.b_day[1])
        else:
            return this_year_bday


characters = [
    Character('Junko', 'Enoshima', 'Female', 'Ultimate Fashionista', Distance(cm=169), 12, 24, Distance(cm=90),
              Mass(kg=45), "Danganronpa 1: Trigger Happy Havoc"),
    Character('Kyoko', 'Kirigiri', 'Female', 'Ultimate ???', Distance(cm=167), 10, 6, Distance(cm=82),
              Mass(kg=48), "Danganronpa 1: Trigger Happy Havoc"),
    Character('Makoto', 'Naegi', 'Male', 'Ultimate Lucky Student', Distance(cm=160), 2, 5, Distance(cm=75),
              Mass(kg=52), 'Danganronpa 1: Trigger Happy Havoc'),
    Character('Byakuya', 'Togami', 'Male', 'Ultimate Affluent Progeny', Distance(cm=185), 5, 5, Distance(cm=81),
              Mass(kg=68), 'Danganronpa 1: Trigger Happy Havoc'),
    Character('Chihiro', 'Fujisaki', '?', 'Ultimate Programmer', Distance(cm=148), 3, 14, Distance(cm=70),
              Mass(kg=41), 'Danganronpa 1: Trigger Happy Havoc')
]

MONOKUMA_QUOTES = ["It's the Monokuma File!", "I am Monokuma!"]


def to_feet(in_measure: Distance):
    inches = int(in_measure.inch)
    feet = inches // 12
    remaining = inches - (feet * 12)

    return feet, remaining
