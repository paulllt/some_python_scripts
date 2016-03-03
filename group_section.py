#!/usr/bin/env python

import random

bsit3a = ['Agnahe, Josie B.',
'Balong, Norilyn Tacio',
'Berras, Jhamieca C.',
'Besa, Evie Marie S.',
'Cabar,Christian Joe P.',
'Cadang, Lindsey Erol C.',
'Calimlim, Sarah Gay C.',
'Camungao, Louella Gaye V.',
'Capitulo, John Vincent Peregrino',
'Colisao, Jhazel Ann T.',
'Dulawan, Novelyn G.',
'Dulay, Carlo C.',
'Dulnuan , Sharon T.',
'Gin-om , Joylyn L.',
'Gramaje , Abel D.',
'Huerta , Beverly Grace Ila',
'Jaronel, Rosie May B.',
'Juan, Josie-lyn B.',
'Lucero , Angelica T.',
'Natividad, Guiller P.',
'Niemes, Krissa A.',
'Novida , Arsenio Jr. P.',
'Obra, Oliver C.',
'Pascua, Sheryl Joy S.',
'Payuyo, Julie Ann N.',
'Pimentel, Myrelle D.',
'Planas , Jobelle C.',
'Santiago, Abegail M.',
'Sunio, Mark Laurence D.',
'Uhuad, Carl Christian P.',
'Velasco, April Jemely A.'
]

bsit3b = ['Ampat, Jefrey C.',
'Balicwadang, Joy D.',
'Banta , Ryan H.',
'Barbero, Alexander B.',
'Bulusan , Rosalyn',
'Casumpang, Acemark M.',
'Corbe,Kurt John P.',
'Delfin , Jinky Mae R.',
'Domenden, Jonah Y.',
'Guiab, EJ Christopher',
'Guillermo, John Paulo A.',
'Gundran , Reynaldo G.',
'Guyong, Salvador Jr L.',
'Haggod, Genoveva B.',
'Hipolito , Brian James',
'Ilarde, Arlene B.',
'Mallanao, Rusell Calalung',
'Palolan, Erwin B.',
'Ramos, Renniel Jay R.',
'Santiago , Odessa B.',
'Simple, Robertson A.',
'Toledo, Myrene F.',
'Torio , Gian Vincent P.',
'Valdez, Jayson P.',
'Virtudez , Junard A.']


def Bsit3a():
    random.shuffle(bsit3a)
    rand_bsit3a = [i for i in bsit3a]

    def GrouperA(seq, size):
        return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

    grp_bsit3a = [group for group in GrouperA(rand_bsit3a, 5)]

    for i in grp_bsit3a:
        print `i` + "\n"

def Bsit3b():
    random.shuffle(bsit3b)
    rand_bsit3b = [i for i in bsit3b]

    def GrouperB(seq, size):
        return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

    grp_bsit3b = [group for group in GrouperB(rand_bsit3b, 5)]

    for i in grp_bsit3b:
        print `i` + "\n"

##Bsit3a()
Bsit3b()
