import os
from .models import Pathology, User, Classes, Molecules, Medicaments

### Renvoie la liste de toutes les maladies
def pathologyChoices():

    temp = Pathology.query.with_entities(Pathology.id, Pathology.name, Pathology.other_name).all()
    other_name_temp = []

    for x in temp:
        if x[2]:
            array = x[2].split(",")

            for i in range(len(array)):
                if array[i] is not None:
                    other_name_temp.append((x[0], array[i].strip()))

    choices = [(x[0], x[1]) for x in temp] + other_name_temp

    i = 0
    l = len(choices)
    while (i < l and choices[i]):
        if choices[i][1] == '':
            del choices[i]
            l -= 1
        else:
            i += 1

    return choices

#renvoie la liste de tous les users
def userChoices():
    temp = User.query.with_entities(User.id, User.forename).all()
    choices = [(x[0], x[1]) for x in temp]
    return choices


#Renvoie la liste de toutes les classes de médicaments
def getClasses():
    temp = Classes.query.with_entities(Classes.name, Classes.icd).all()
    classes = [(x[0], x[1]) for x in temp]
    return classes

#Renvoie la liste de toutes les molécules
def getMolecules():
    temp = Molecules.query.with_entities(Molecules.name, Molecules.link, Molecules.test, Molecules.id_molecule).all()
    molecules = [(x[0], x[1]) for x in temp]
    return molecules


#Renvoie la liste de tout les médicaments
def getMedicaments():
    temp = Medicaments.query.with_entities(Medicaments.id, Medicaments.name, Medicaments.molecule_id);
    Medicaments = [(x[0], x[1]) for x in temp]
    return Medicaments
