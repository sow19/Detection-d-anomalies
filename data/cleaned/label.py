import pandas as pd
import re

# Charger le fichier CSV
df = pd.read_csv("final_clean_data1.csv")

def assign_label(problems_text):
    """
    Assigne un label basé sur la présence exclusive de termes liés au cœur ou au poumon.
    Retourne "coeur" si uniquement les termes cardiaques sont présents,
    "poumon" si uniquement les termes pulmonaires sont présents,
    sinon retourne une chaîne vide.
    """
    if pd.isnull(problems_text):
        return ""
    text = problems_text.lower()
    # Détection des termes liés au cœur
    heart_found = bool(re.search(r'cardiac|cardio|heart', text))
    # Détection des termes liés aux poumons
    lung_found = bool(re.search(r'pulmonary|lung', text))
    
    # Attribution du label en fonction des conditions
    if heart_found and not lung_found:
        return "coeur"
    elif lung_found and not heart_found:
        return "poumon"
    else:
        return ""

# Ajout de la colonne 'label' en appliquant la fonction sur la colonne 'Problems'
df['label'] = df['Problems'].apply(assign_label)

# Affichage des premières lignes pour vérification
print(df[['Problems', 'label']].head(30))

# (Optionnel) Sauvegarde du DataFrame modifié dans un nouveau fichier CSV
df.to_csv("final_clean_data1_labeled.csv", index=False)
