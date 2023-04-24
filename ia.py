import random

def make_move(cases):
    """Cette fonction choisit une case aléatoire vide pour l'IA"""
    liste_cases = []
    for i in range(3):
        for j in range(3):
            if cases[i][j] == 0:
                liste_cases.append((i,j))
    if liste_cases:
        case_ia = random.choice(liste_cases)
        return case_ia
    else:
        return None