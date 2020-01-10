class Persona:
    def __init__(self, textura, drevo, uroven):
        self.textura = textura
        self.drevo = drevo.drevo
        self.uroven = uroven
        self.sila = 1
        self.lovkost = 1
        self.intelekt = 1
        self.shizn = 1
        self.hp = self.shizn*10
        self.oburon = (self.sila + self.lovkost) * 10
        self.maguron = (self.intelect + self.shizn) * 10
        self.hsuperpoint = uroven# очки характеристик
        self.megapoin = uroven / 5# очки навыков
        self.snarasheinie = {'shlem': None, 'kirasa' : None, 'posoh': None, 'kolco': [None for i in range(5)]} # снаряжение персонажа(None значит нету)
class Drevo:
    def __init__(self):
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
        
