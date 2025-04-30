import csv

def extraire_indices_anomalies(fichier_entree, fichier_sortie="indices_anomalies.csv"):
    """
    Extrait les indices des lignes contenant une anomalie (label = 1) et les enregistre dans un CSV.
    
    Args:
        fichier_entree (str): Chemin vers le fichier contenant les rapports et les labels.
        fichier_sortie (str): Nom du fichier CSV où enregistrer les indices.
    """
    indices_anomalies = []

    with open(fichier_entree, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            line = line.strip()
            if line.endswith(',1'):
                indices_anomalies.append(i)

    with open(fichier_sortie, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["indice"])
        for idx in indices_anomalies:
            writer.writerow([idx])

    print(f"{len(indices_anomalies)} indices d'anomalies enregistrés dans '{fichier_sortie}'")

if __name__ == "__main__":
    input_file = "anomalieChatGpt.csv"
    output_file = "indices_anomalies.csv"
    extraire_indices_anomalies(input_file, output_file)
