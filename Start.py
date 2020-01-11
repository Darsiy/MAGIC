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
        self.megapoint = uroven / 5# очки навыков
        self.pd = uroven + self.sila + self.intelekt
        self.inventar = []
        self.snarasheinie = {'shlem': None, 'kirasa' : None, 'posoh_or_mech': None} # снаряжение персонажа(None значит нету)

    def monstr_ubit(self, monstr):
        hxp = monstr.dxp
        self.xp -= hxp
        while self.xp >= self.nxp:
            self.uroven += 1
            if self.uroven % 5 == 0:
                self.megapoint += 1
            self.hsuperpoint += 1
            self.nxp *= 2
        x = random.choice(['shlem', 'kirasa', 'posoh', 'mech'])
        self.inventar.append(Snaraga(x, x+'_'+str(monstr.level)+'.jpg', monstr.level))

    def odet_snaraga(self, snaraga):
        t = snaraga.tip
        if self.snarashenie[t] is None:
            self.snarashenie[t] = snaraga
            self.sila += snaraga.haracteristik[-1]
            self.lovkost += snaraga.haracteristik[1]
            self.intelekt += snaraga.haracteristik[0]
            self.shizn += snaraga.haracteristik[2]
            self.hp = self.shizn * 10
        else:
            self.inventar.append(self.snarashenie[t])
            self.snarashenie[t] = snaraga
            self.sila += snaraga.haracteristik[-1]
            self.lovkost += snaraga.haracteristik[1]
            self.intelekt += snaraga.haracteristik[0]
            self.shizn += snaraga.haracteristik[2]
            self.hp = self.shizn * 10
        del self.inventar[self.inventar.index(snaraga)]
class Monstr:
    def __init__(self, textura, level, soundpack):
        self.textura = textura
        self.napravlenie = 'sila' if level <= 3 else (random.choice(['sila', 'fire', 'water', 'sila', 'fire', 'dark']))
        self.dxp = level * 3**(['sila', 'fire', 'water', 'dark'].index(self.napravlenie))
        self.level = level
        self.uron = 2**level
        self.hp = 2**level * random.randint(1, 5)
class Bitva_c_monstr:
    def __init__(self, igrok, monstr):
        vd = igrok.getnav()
        kd = igrok.pd
        while monstr.hp != 0 and igrok.hp != 0:
            for i in range(kd):
                a = 0#не ноль а запрпос ноиера навыка из предварительно показанного игроку списка, соответствующего списку выдаваемому igrok.getnav()
                vd[a - 1](monstr)
                if monstr.hp > 0:
                    pass
                else:
                    igrok.monstr_ubit(monstr)
                    igrok.hp = igrok.shizn*10
                    return 1
            igrok.attack(monstr)
            if igrok.hp <= 0:
                igrok.hp = igrok.shizn*10
                return 1#тут завершение боя, игрок не может умереть, если хп в ноль - битва завершается, игрок уходит, готовится, и возвращается
class Snaraga:
    def __init__(self, tip, textura, level):
        self.tip = tip
        if tip == 'kirasa':
            i, l, sh, s = 0, -3, level, -1
        elif tip == 'mech':
            i, l, sh, s = -1, -1, 1, level
        elif tip == 'posoh':
            i, l, sh, s = level, -1, 0, 1
        elif tip == 'shlem':
            i, l, sh, s = level + 1, -1, level // 3, -1
        self.haracteristik = [i, l, sh, s]
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
#картинки снаряги - тип('shlem' и т.д), '_', уровень, '.jpg'
        
