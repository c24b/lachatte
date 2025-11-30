# LA CHATTE

Tout est parti d'un sketch potache, pourquoi ne considère t on pas l'activité sexuelle comme une pratique sportive à part entière?

Après le chat, voici la chatte votre assistant coach sportif sexuel personnalisé.

A chaque position sexuelle: 
- informer sur le nombre de calories dépensées
- leur équivalent nutritionnel (3 suggestions)
- les zones du corps mobilisées sollicitées
- recommander des étirements, position de Yoga, mouvements de Taichi appropriés


- [x] Script de caclul de dépense énergétique
- [x] Equivalent alimentaire
- [x] Retour de zones du corps mobilisées avec pondération
- [x] Recommandation de mouvements d'étirements
- [x] Suggestion de postures de Yoga de mouvements de Taichi
- [ ] Schema pour les position et video pour les recommandations

Les 12 positions sont classés par combinaisons de genre il faudrait ajouter genre comme filtre et actif/passif comme role et filtre additionnels: on a mis une pondération et trouver une structure pour posture classique et variantes (les variantes ne mobilsent pas les mêmes endroits)

#### Dépense énergétique (MET) et equivalent kcal

METs = metabolic equivalents.
One MET is defined as the energy you use when you’re resting or sitting still.
An activity that has a value of 4 METs means you’re exerting four times the energy than you would if you were sitting still. 

One MET is approximately 3.5 milliliters of oxygen consumed per kilogram (kg) of body weight per minute. 
But it is a simple table ref
Transform MET in kcal burnt
The formula to use is: METs x 3.5 x (your body weight in kilograms) / 200 = calories burned per minute.
def compute_kcal(met, kg, duration_in_minutes):
    return (MET*3.5*kg/200)*duration_in_minute

#### Correspondance alimentaire
- Table kcal aliment par portion
- Les aliments le plus proche de l'effort

#### Correspondances positions etirements /yoga taïchi

Verification du croisement des données normalisation des zones tendons et muscles
Variation en fonction de la posture


## TO DO

- Fichiers aux propres. S'assurer que les données soient croisables complètes. Pas de données scientifiques HH FF et pas de données -18 +de 35 extrapolation justifiées 
- Ajouter des positions et variantes
- Normalisation des "mouvements_articulaires","tendons","zones_mobilisées" pour affiner les suggestions

> L'idéal se serait d'avoir une distinction dans les mouvements et les aspects mécaniques 
> en fonction de position, variantes, H/F et status actif passif mutuel 

> mais il faut ajouter aussi une pondération MET pour les positions: tranquille, modéré, intense
cf MET_table extrapolation a partir des données scientifiques

## MUST

- Combiner les positions en séquence. Analyse post et recommandations
- Inverser: plan d'activité en fonction des kcal/aliments à bruler

## NICE TO HAVE

- Prendre en compte le nombre de participants (pourquoi seulement deux?)


## WTF

- Ajouter une "méthode kilomètre de bite" (Module a part)