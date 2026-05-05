# Monitoring DDoS - La Banque Postale
# Simulation d'un système d'alerte en cas d'attaque par déni de service distribué
# Auteur : Mathilde Burgaud

import time
import random

# --- PARAMÈTRES ---
# Basés sur l'incident réel de La Banque Postale (décembre 2025 - janvier 2026)

SEUIL_NORMAL = 150      # trafic habituel en req/sec sur un service bancaire
SEUIL_ALERTE = 500      # anomalie : analyse active des logs en temps réel
SEUIL_CRITIQUE = 2000   # attaque probable : blocage du trafic + alerte équipe sécurité
DUREE_SIMULATION = 12   # nombre de secondes simulées

# --- FONCTIONS ---

def simuler_requetes():
    # Simule le trafic reçu par le serveur de La Banque Postale
    # Dans la réalité : ces données viendraient des vrais logs serveur
    return random.randint(50, 3000)

def analyser_trafic(requetes):
    # Compare le trafic reçu aux seuils définis
    # Retourne le niveau de danger et l'action à entreprendre
    if requetes < SEUIL_ALERTE:
        return "NORMAL", "✅", "surveillance passive"
    elif requetes < SEUIL_CRITIQUE:
        return "ALERTE", "⚠️", "analyse active des logs en temps réel"
    else:
        return "CRITIQUE", "🚨", "blocage du trafic + équipe sécurité notifiée"

# --- PROGRAMME PRINCIPAL ---
print("=== Système de monitoring - La Banque Postale ===")
print("=== Simulation basée sur l'incident de décembre 2025 ===\n")

for cycle in range(1, DUREE_SIMULATION + 1):
    requetes = simuler_requetes()
    statut, emoji, action = analyser_trafic(requetes)
    print(f"[Seconde {cycle:02d}] {emoji} {requetes} req/sec → {statut} : {action}")
    time.sleep(0.5)

print("\n=== Fin de simulation ===")
print("Dans un système réel : ces données alimenteraient un SIEM")
print("Exemple : Splunk ou IBM QRadar utilisés dans le secteur bancaire")
