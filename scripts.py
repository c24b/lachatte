#!/usr/bin/python3
'''2 scripts débiles pour faire des statistiques et recommandations sur les positions sexuelles'''
def load_db():
    import json
    from pymongo import MongoClient

    client = MongoClient('localhost', 27017)
    db = client['chatte_db']
    with open('activites.json') as f:
        file_data = json.load(f)

    collection_currency = db['activity']
    collection_currency.insert_many(file_data)
    client.close()
    return db['activity']

def find_position(db, position):
    '''Trouver une position sexuelle dans la base de données'''
    result = db.find_one({'position_famille': position, 'activité': 'sexe'})
    return result

def post_coit(position, duréee, poids1, poids2,):
    '''Calculer les effets post-coïtaux sur les *deux personnes
    Nombre de kilocalories dépensées, fatigue musculaire, risque de blessure, recommandations d'étirements yoga et taichi post coït pour récupération.
    Retourne un dictionnaire avec les résultats pour chaque personne 
    '''
    db.find_one(position)

    return 

if __name__ == '__main__':
    db = load_db()
    pos = find_position(db, 'Missionnaire')
    print(pos)  