#!/usr/bin/python3
'''2 scripts débiles pour faire des statistiques et recommandations sur les positions sexuelles'''
def load_db():
    import json
    with open('activites.json', encoding="utf-8") as f:
        return json.load(f)
    
        #return json.loads(file_data)

def find_position_type(position):
    '''Trouver une position sexuelle dans la base de données'''
    positions = load_db()
    results = [{x:y} for x,y in positions.items() if y["activité"]== "sexe" and position in y["position_famille"]]
    if len(results) == 0:
        raise ValueError(f"Position {position} non trouvée dans la base de données.")
    return results
def find_position(position):
    '''Trouver une position sexuelle dans la base de données'''
    positions = load_db()
    results = [{x:y} for x,y in positions.items() if y["activité"]== "sexe" and position in x]
    names = [x for x,y in positions.items() if y["activité"]== "sexe" and position in x]
    if len(results) == 0:
        raise ValueError(f"Position {position} non trouvée dans la base de données.")
    if len(results) > 1:

        raise ValueError(f"Plusieurs positions pour '{position}' trouvées dans la base de données: {", ".join(names)}.")
    return results[0]

def post_coit(position, duréee, poids1, poids2):
    '''Calculer les effets post-coïtaux sur les *deux personnes
    Nombre de kilocalories dépensées, fatigue musculaire, risque de blessure, recommandations d'étirements yoga et taichi post coït pour récupération.
    Retourne un dictionnaire avec les résultats pour chaque personne 
    '''
    
    return 

if __name__ == '__main__':
    # print(load_db())
    pos = find_position("Missionnaire")
    print(pos)