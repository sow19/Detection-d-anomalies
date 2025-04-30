import os
import csv

def select_reports(input_file, start_index, num_reports_to_modify):
    """
    Sélectionne séquentiellement un groupe de rapports à modifier.
    Args:
        input_file (str): chemin vers le fichier d'entrée
        start_index (int): indice de départ
        num_reports_to_modify (int): nombre de rapports à sélectionner
    Returns:
        all_reports (list of str): tous les rapports
        selected_indices (list of int): indices des rapports sélectionnés
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        all_reports = [line.strip() for line in f if line.strip()]
        total_reports = len(all_reports)
    
    # Calculer les indices à sélectionner
    end_index = min(start_index + num_reports_to_modify, total_reports)
    selected_indices = list(range(start_index, end_index))
    
    return all_reports, selected_indices

def display_reports_for_modification(all_reports, indices_to_modify):
    """
    Affiche les rapports sélectionnés pour modification.
    """
    for idx in indices_to_modify:
        print(f"\n--- Rapport {idx+1} ---")
        print(all_reports[idx])
        print("-----------------------")

def save_modified_reports(input_file, output_file, modified_reports, indices_to_modify):
    """
    Enregistre les rapports modifiés dans le fichier final avec un label :
    0 pour un rapport non modifié, 1 pour un rapport modifié.
    Conserve les labels existants si le fichier output_file existe déjà.
    Args:
        input_file (str): chemin du fichier d'entrée
        output_file (str): chemin du fichier de sortie
        modified_reports (list of str): nouvelles versions des rapports
        indices_to_modify (list of int): indices où appliquer les modifications
    """
    # Lire les rapports originaux
    with open(input_file, 'r', encoding='utf-8') as f:
        all_reports = [line.strip() for line in f if line.strip()]
        
    # Initialiser tous les labels à 0
    labels = [0] * len(all_reports)
    
    # Si le fichier de sortie existe déjà, lire les labels existants
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                # Essayer de lire en format CSV
                try:
                    reader = csv.reader(f)
                    existing_data = list(reader)
                    if len(existing_data) > 0 and len(existing_data[0]) >= 2:
                        # Si le fichier a au moins une colonne pour les données et une pour les labels
                        for i, row in enumerate(existing_data):
                            if i < len(labels) and len(row) >= 2:
                                try:
                                    labels[i] = int(row[1])
                                except (ValueError, IndexError):
                                    # Si la conversion échoue, garder la valeur par défaut (0)
                                    pass
                except:
                    # Essayer de lire ligne par ligne en supposant format "texte,label"
                    f.seek(0)  # Revenir au début du fichier
                    for i, line in enumerate(f):
                        parts = line.strip().rsplit(',', 1)
                        if len(parts) == 2 and i < len(labels):
                            try:
                                labels[i] = int(parts[1])
                            except ValueError:
                                # Si la conversion échoue, garder la valeur par défaut (0)
                                pass
        except Exception as e:
            print(f"Erreur lors de la lecture des labels existants: {e}")
            print("Les labels sont initialisés à 0.")
    
    # Appliquer les modifications et mettre à jour les labels
    for idx, modified in zip(indices_to_modify, modified_reports):
        all_reports[idx] = modified
        labels[idx] = 1
    
    # Enregistrer les résultats
    with open(output_file, 'w', encoding='utf-8') as f:
        for report, label in zip(all_reports, labels):
            f.write(f"{report},{label}\n")
    
    print(f"Fichier final enregistré avec labels préservés : {output_file}")

if __name__ == "__main__":
    input_file = "final_clean_data1.csv"
    output_file = "radiology_reports_modified.csv"
    start_index = 3000
    num_to_modify = 5
    
    all_reports, indices_to_modify = select_reports(input_file, start_index, num_to_modify)
    display_reports_for_modification(all_reports, indices_to_modify)
    
    modified_reports = []
    for idx in indices_to_modify:
        print(f"\nEntrez le rapport modifié pour le rapport {idx+1} :")
        new_text = input()
        modified_reports.append(new_text)
    
    save_modified_reports(input_file, output_file, modified_reports, indices_to_modify)