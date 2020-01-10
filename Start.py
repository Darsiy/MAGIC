import random
class Persona:
    def __init__(self, textura, drevo, uroven, supersoundpack):
        self.textura = textura
        self.drevo = drevo.drevo
        self.uroven = uroven
        self.sila = 1
        self.lovkost = 1
        self.intelekt = 1
        self.shizn = 1
        self.hp = self.shizn*10
        self.nxp = 2**uroven
        self.xp = 0
        self.oburon = (self.sila + self.lovkost) * 10
        self.maguron = (self.intelect + self.shizn) * 10
        self.hsuperpoint = uroven# очки характеристик
        self.megapoin = uroven / 5# очки навыков
        self.snarasheinie = {'shlem': None, 'kirasa' : None, 'posoh': None, 'kolco': [None for i in range(5)]} # снаряжение персонажа(None значит нету)
class Monstr:
    def __init__(self, textura, level, soundpack):
        self.textura = textura
        self.napravlenie = 'sila' if level <= 3 else (random.choice(['sila', 'fire', 'water', 'sila', 'fire', 'dark']))
        self.dxp = level * 3**(['sila', 'fire', 'water', 'dark'].index(self.napravlenie))
        self.level = level
        self.uron = 2**level
        self.hp = 2**level * random.randint(1, 5)
class Drevo:
    def __init__(self, specialsoundpack):
        self.drevo = {'magic': [0, {'energy ball': [0, {'fireball': [0],
                                                        'waterball': [0],
                                                        'lightning ball': [0],
                                                        }],
                                'energy wall': [0, {'firewall': [0],
                                                    'waterwall': [0],
                                                    'lightning wall': [0],
                                                    }],
                                'energy wave': [0, {'fire wave': [0],
                                                    'water wave': [0],
                                                    'lightning': [0],
                                                    }],
                                'positive charge': [0, {'treatment': [0],
                                                        'beneficial effect': [0],
                                                        'call of God': [0],},
                                                    ]},
                                ],
                      'sword': [0, {'fast attack': [0, {'the cycle of swords': [0]}],
                                'slow attack': [0, {'a fatal puncture': [0],
                                                    }],
                                'normal attack': [0, {'blood to the God of swords': [0],
                                                      }],
                                'counterattack': [0],
                                                    },
                                    ]}
#соундпаки - списки с музыкой, прогигрываемой при определённых ситуациях. soundpack = [получение урона, нанесение урона]\
#        supersoundpack = [получение урона, нанесение урона, лечение, шаги, переход на новый уровень] specialsoundpack = [поднятие уровня навыка, изучение навыка]
        
