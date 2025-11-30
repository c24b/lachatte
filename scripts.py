#!/usr/bin/python3
'''2 scripts débiles pour faire des statistiques et recommandations sur les positions sexuelles'''
import json
from typing import List, Dict, Any


def load_db():
    import json
    with open('activites.json', encoding="utf-8") as f:
        return json.load(f)


def kcal_from_met(met: float, weight_kg: float, duration_min: float) -> float:
    """Return kcal burned using ACSM formula.

    kcal/min = (MET * 3.5 * weight_kg) / 200
    total = kcal/min * duration_min
    """
    return float(met) * 3.5 * float(weight_kg) * float(duration_min) / 200.0


DEFAULT_ROLE_FACTORS = {
    'actif': 1.10,
    'passif': 0.90,
    'neutral': 1.0,
}


def kcal_with_role(base_met: float, role: str, weight_kg: float, duration_min: float,
                   role_factors: Dict[str, float] = None) -> float:
    """Compute kcal after applying a role multiplier to the base MET."""
    rf = (role_factors or DEFAULT_ROLE_FACTORS).get(role, DEFAULT_ROLE_FACTORS['neutral'])
    adjusted_met = float(base_met) * rf
    return kcal_from_met(adjusted_met, weight_kg, duration_min)


def load_nutrition_db() -> List[Dict[str, Any]]:
    with open('nutrition_table.json', encoding='utf-8') as f:
        return json.load(f)


def equivalents_from_kcal(kcal: float, max_results: int = 10) -> List[Dict[str, Any]]:
    """Return a list of food equivalents for a given kcal amount.
    kcal : amount of kcal to match.
    max_results : maximum number of results to return.  
    """
    nutrit = load_nutrition_db()
    out = []
    for item in nutrit:
        kpp = item.get('kcal_per_portion')
        if not kpp:
            continue
        portions_needed = float(kcal) / float(kpp) if kpp else None
        match = round(portions_needed,2)
        out.append({
            'aliment': item.get('aliment'),
            'ratio': match,
            'nearest': abs(round(1-match,2))
        })
    best_equivalent =sorted(out, key= lambda x: x['nearest'])
    return best_equivalent[:max_results]
def load_taichi():
    import json
    with open('taichi_positions.json', encoding="utf-8") as f:
        return json.load(f)
def load_yoga():
    import json
    with open('yoga_positions.json', encoding="utf-8") as f:
        return json.load(f)

def load_stretches():
    import json
    with open('stretching_positions.json', encoding="utf-8") as f:
        return json.load(f)
def find_yoga(position):
    '''Trouver une position de yoga dans la base de données'''
    yogas = load_yoga()
    results = [{x:y} for x,y in yogas.items() if position in x]
    if len(results) == 0:
        raise ValueError(f"Position de yoga {position} non trouvée dans la base de données.")
    return results
def find_taichi(position):
    '''Trouver une position de taichi dans la base de données'''
    taichis = load_taichi()
    results = [{x:y} for x,y in taichis.items() if position in x]
    if len(results) == 0:
        raise ValueError(f"Position de taichi {position} non trouvée dans la base de données.")
    return results
def find_stretch(position):
    '''Trouver une position d'étirement dans la base de données'''
    stretches = load_stretches()
    print(stretches)
    results = [{x:y} for x,y in stretches.items() if position in x]
    if len(results) == 0:
        raise ValueError(f"Position d'étirement {position} non trouvée dans la base de données.")
    return results        
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

def filter_position_type_by_genre_and_role(position, genre, role):
    '''Filtrer une liste de positions sexuelles par rôle (HF, HM, F, MM, MF, FF)'''
    positions = find_position_type(position)
    filtered = []
    for pos in positions:
        for name, details in pos.items():
            if "genre" not in details:
                continue
            if genre in details["genre"]:
                if role == "actif" and details["genre"].index(genre) == 0:
                    filtered.append({name: details})
                elif role == "passif" and details["genre"].index(genre) == 1:
                    filtered.append({name: details})
            else:
                continue
        
    if len(filtered) == 0:
        raise ValueError(f"Aucune position '{position}' trouvée qui corresponde au genre '{genre}' et au rôle '{role}'.")
    if len(filtered) > 1:
        names = [list(pos.keys())[0] for pos in filtered]
        raise ValueError(f"Plusieurs positions pour '{position}' trouvées dans la base de données: {", ".join(names)} qui correspond au genre '{genre}' et au rôle '{role}'.")
    return filtered[0]
def filter_position_by_genre_and_role(position, genre, role):
    '''Filtrer une liste de positions sexuelles par rôle (HF, FF, FH, HH)'''
    position = find_position(position)
    filtered = []
    for name, details in position.items():
        if "genre" not in details:
            continue
        if genre in details["genre"]:
            if role == "actif" and details["genre"].index(genre) == 0:
                filtered.append({name: details})
            elif role == "passif" and details["genre"].index(genre) == 1:
                filtered.append({name: details})
        else:
            continue
        
    if len(filtered) == 0:
        raise ValueError(f"La position '{position}' trouvée ne correspond pas au genre '{genre}' et au rôle '{role}'.")
    if len(filtered) > 1:
        names = [list(pos.keys())[0] for pos in filtered]
        raise ValueError(f"Plusieurs positions pour '{position}' trouvées dans la base de données: {", ".join(names)} qui correspond au genre '{genre}' et au rôle '{role}'.")
    return filtered[0]
def recommandation_etirements(position, duree, kg, genre, role):
    '''Fournir des recommandations d'étirements post-coïtaux en fonction de la position sexuelle, de la durée, du genre et du rôle.
    Retourne une liste d'exercices d'étirements recommandés.
    '''
    try:
        results = filter_position_by_genre_and_role(position, genre, role)
    except ValueError as e:
        results = filter_position_type_by_genre_and_role(position, genre, role)
    ponderation_role = {"actif": 1.2, "passif": 0.8, "mutual": 1}
    recommandations = []
    for name, details in results.items():
        print(f"Position: {name} - Durée: {duree} min - Poids: {kg} kg - Genre: {genre} - Rôle: {role}")
        #ponderation du MET en fonction de la durée et du poids, du role et du genre
        kcal_burnt = (details.get("MET")*3.5*kg/200)* duree * ponderation_role.get(role,1)
        print(f"Dépense énergétique estimée: {kcal_burnt} kcal")
        print(f"Equivalents consommés en portion 3 exemples:", [x.get("aliment") for x in equivalents_from_kcal(kcal_burnt, max_results=3)])
        print(f"Hormones mobilisées: {details.get("hormones_mobilisées")}")
        print(f"Mouvements: {details.get("mouvements_articulaires")}")
        print("Recommandations d'étirements post activité:")
        recommandations = sorted([d for d in details.get("recommandation_recuperation")], key=lambda x: x.get("ponderation"), reverse=True)

        for zone in recommandations:
            print(f"Zone ciblée à soulager: {zone.get("zone")}")
            print(f"Priorité: {zone.get("ponderation")*100}%")
            print(f"Objectif: {zone.get("explication")}")
            print(f"Exercices recommandés:")
            strech = zone.get("etirement")
            print(f"\tEtirements: {strech}")
            print(f"\tYoga: {zone.get("yoga")}")
            print(f"\tTaiChi: {zone.get("taichi")}")
            

    #return recommandations

def post_coit(position, duréee, poids, genre, role):
    '''Calculer les effets post-coïtaux sur une seule personne en fonction de la position sexuelle et son role
    Nombre de kilocalories dépensées, fatigue musculaire, risque de blessure, recommandations d'étirements yoga et taichi post coït pour récupération.
    Retourne un dictionnaire avec les résultats pour chaque personne 
    en fonction de la position elle nous donne un MET de référence pour une minute qu'on va convertir en kilocalories dépensées (poids, durée, pondération en fonction du genre et su status acif/passif)

    '''
    
    return 

if __name__ == '__main__':
    # pos = find_position("Missionnaire")
    # print(pos)
    # pos = filter_positions_by_genre_and_role("Missionnaire", "H", "actif")
    # print(pos)
    #pos = filter_position_by_genre_and_role("Doggy", "F", "actif")
    #pos = filter_position_by_genre_and_role("Missionnaire_inversé_FH", "F","actif")
    recommandation_etirements("Doggy",25,85, "H", "actif")
    recommandation_etirements("Cowgirl_classique",10,72, "F", "actif")    
    
    # recommandation_etirements = recommandation_etirements("Missionnaire_inversé_FH",75, 5, "F","actif")    
    # print(recommandation_etirements)
