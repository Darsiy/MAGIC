import random
def magic_start(self, igrok, monstr, level):
    if level:
        monstr.hp -= level*2+igrok.maguron
    else:
        g = random.randint(0, 2)
        monstr.hp -= g*igrok.maguron
        if g != 1:
            igrok.hp -= igrok.maguron//2
def magic_energy_ball(self, igrok, monstr, level):
    if level:
        monstr.hp -= igrok.maguron*(2 + level / 10)
    else:
        g = random.randint(0, 2)
        monstr.hp -= g*igrok.maguron
        if g != 1:
            igrok.hp -= igrok.maguron//2
def magic_energy_wave(self, igrok, monstr, level):
    if level:
        monstr.sposobnosti += 1
    else:
        g = random.randint(0, 2)
        monstr.sposobnosti += g
        if g != 1:
            igrok.sposobnosti += 1
def magic_wall(self, igrok, monstr, level):
    if level:
        igrok.hp += level * 20
    else:
        igrok.sposobnosti += 1
def sword_start(self, igrok, monstr, level):
    if level:
        monstr.hp -= level*2+igrok.oburon
    else:
        g = random.randint(0, 2)
        monstr.hp -= g*igrok.oburon
        if g != 1:
            igrok.hp -= igrok.oburon // 2
def sword_fast_attack(self, igrok, monstr, level):
    if level:
        g = random.randint(0, 2)
        monstr.hp -= igrok.oburon
        if g:
            monstr.krovotechenie += level
    else:
        pass
def sword_slow_attack(self, igrok, monstr, level):
    if level:
        g = random.randint(0, 2)
        monstr.hp -= igrok.oburon*level
        if g:
            monstr.sposobnosti += 1
    else:
        pass
def sword_normal_attack(self, igrok, monstr, level):
    if level:
        g = random.randint(0, 2)
        monstr.hp -= igrok.oburon*level
        if g:
            igrok.hp += level * 40
    else:
        pass
class Navk:
    def __init__(self, func, level):
        self.level = level
        self.func = func

    def deistvie(self, igrok, monstr):
        self.func(igrok, monstr, self.level)

    def level_up(self, g):
        self.level += g
class Persona:
    def __init__(self, textura, drevo, uroven, supersoundpack):
        self.krovotechenie = 0
        self.sposobnosti = 0
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
        self.megapoint = uroven // 5# очки навыков
        self.pd = level
        self.inventar = []
        self.snarasheinie = {'shlem': None, 'kirasa' : None, 'posoh_or_mech': None} # снаряжение персонажа(None значит нету)

    def monstr_ubit(self, monstr):
        hxp = monstr.dxp
        self.xp += hxp
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
            self.sila -= self.snarashenie[t].haracteristik[-1]
            self.lovkost -= self.snarashenie[t].haracteristik[1]
            self.intelekt -= self.snarashenie[t].haracteristik[0]
            self.shizn -= self.snarashenie[t].haracteristik[2]
            self.snarashenie[t] = snaraga
            self.sila += snaraga.haracteristik[-1]
            self.lovkost += snaraga.haracteristik[1]
            self.intelekt += snaraga.haracteristik[0]
            self.shizn += snaraga.haracteristik[2]
            self.hp = self.shizn * 10
        del self.inventar[self.inventar.index(snaraga)]
class Monstr:
    def __init__(self, textura, level, soundpack):
        self.sposobnosti = 0
        self.krovotechenie = 0
        self.textura = textura
        self.napravlenie = 'sila' if level <= 3 else (random.choice(['sila', 'fire', 'water', 'sila', 'fire', 'dark']))
        self.dxp = level * (['sila', 'fire', 'water', 'dark'].index(self.napravlenie)+1)
        self.level = level
        self.uron = 2**level
        self.hp = 2**level * random.randint(1, 5)
class Boss:
    def __init__(self, textura, level, soundpack, igrok):
        self.sposobnosti = 0
        self.krovotechenie = 0
        self.textura = textura
        self.napravlenie = 'sila' if level <= 3 else (random.choice(['sila', 'fire', 'water', 'sila', 'fire', 'water', 'dark']))
        self.dxp = level * (['sila', 'fire', 'water', 'dark'].index(self.napravlenie)+1) * (1 if self.napravlenie != 'dark' else 3)
        self.level = level
        self.uron = 2**level
        self.hp = 2**level * random.randint(1, 5)
        if self.napravlenie == 'sila':
            self.hp *= 3
        if self.napravlenie == 'fire':
            self.uron *= 3
        if self.napravlenie == 'water':
            self.uron *= 3
            self.hp *= 3
        if self.napravlenie == 'dark':
            self.level += igrok.level
            self.uron = 2**level
            self.hp *= 2**igrok.level
class Bitva_c_monstr:
    def __init__(self, igrok, monstr):
        vd = igrok.getnav()
        kd = igrok.pd
        while monstr.hp != 0 and igrok.hp != 0:
            if igrok.sposobnosti != 0:
                for i in range(3):
                    a = 0#не ноль а запрпос номера навыка из предварительно показанного игроку списка, соответствующего списку выдаваемому igrok.getnav()
                    vd[a - 1].deistvie(monstr)
                    if monstr.hp > 0:
                        pass
                    else:
                        igrok.monstr_ubit(monstr)
                        igrok.hp = igrok.shizn*10
                        return 1
            else:
                igrok.sposobnosti -= 1
            if monstr.krovotechenie:
                monstr.hp *= (1 - monstr.krovotechenie/10)
                monstr.krovotechenie = 0
            if igrok.krovotechenie:
                igrok.hp *= (1 - igrok.krovotechenie/10)
                igrok.krovotechenie = 0
            if monstr.sposobnosti != 0:
                igrok.attack(monstr)
            else:
                monstr.sposobnosti -= 1
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
        self.drevo = {'magic': [Navk(magic_start, 0), {'energy ball': [Navk(magic_energy_ball, 0)],
                                'energy wall': [Navk(magic_energy_wall, 0)],
                                'energy wave': [Navk(magic_energy_wave, 0)]}],
                      'sword': [Navk(sword_start, 0), {'fast attack': [Navk(sword_fast_attack, 0)],
                                'slow attack': [Navk(sword_slow_attack, 0)],
                                'normal attack': [Navk(sword_normal_attack, 0)]}]}
class Karta:
    def __init__(self, x, y, level, soundpackmonstr, igrok, soundpackboss):
        self.karta = [[None if random.randint(0, 5) != 0 else (Monstr('Monstr' + str(level) + '.jpg', level, soundpackmonstr) if random.randint(0, 10) != 0 else Boss('Boss' + str(level) + '.jpg', level, soundpackboss, igrok)) for i in range(x)] for i in range(y)]
        self.karta[y//2][x//2] = igrok
    def check(self):
        for i in self.karta:
            for j in i:
                if type(j) in (type(Monstr(1, 1, 1)), type(Boss(1, 1, 1, 1))):
                    return False
        return True
#соундпаки - списки с музыкой, прогигрываемой при определённых ситуациях. soundpack = [получение урона, нанесение урона, стан]\
#        supersoundpack = [получение урона, нанесение урона, стан, шаги, переход на новый уровень] specialsoundpack = [поднятие уровня навыка, изучение навыка]
#названия картинки снаряги - тип('shlem' и т.д) + '_' + уровень + '.jpg'
#sposobnosti - уровень стана, сколько ходов пропустит self
