# Simulation d'un mécanisme de budget cap cloud
# Inspiré du service AWS Budgets d'Amazon Web Services
# Tarifs basés sur AWS EC2 On-Demand région Europe (m5.large : 0.096$/heure)
# Source : https://aws.amazon.com/ec2/pricing/on-demand/
# Hypothèse : La Banque Postale utilise un hébergement cloud avec auto-scaling
# Note : l'infrastructure réelle de La Banque Postale n'est pas publiquement connue
# Ce script illustre le risque de surfacturation applicable à tout hébergeur cloud
# Il fonctionne en complément de moniteur_ddos.py
# Auteur : Mathilde Burgaud

import time
import random

# --- PARAMÈTRES ---
# INSTANCES_BASE : nombre d'instances qui tournent en temps normal
# INSTANCES_MAX : plafond d'instances autorisées pendant un pic
# BUDGET_CAP : plafond financier en dollars sur la durée de simulation
# Au-delà de ce plafond, l'auto-scaling est bloqué automatiquement
# Tarif On-Demand choisi car lors d'un pic de trafic — qu'il soit
# d'origine malveillante (attaque DDoS) ou légitime (période de fêtes,
# forte affluence) — le nombre de requêtes peut dépasser la capacité
# des instances réservées à l'avance. Un hébergeur cloud peut alors
# lancer automatiquement des instances supplémentaires facturées à la seconde.

COUT_PAR_INSTANCE_HEURE = 0.096
INSTANCES_BASE = 10
INSTANCES_MAX = 500
BUDGET_CAP = 1000
DUREE_SIMULATION = 12

SEUIL_ALERTE = 500
SEUIL_CRITIQUE = 2000

# --- FONCTIONS ---

def simuler_requetes():
    # Simule le trafic reçu par seconde sur le serveur
    return random.randint(50, 3000)

def calculer_instances(requetes):
    # Plus le trafic augmente, plus l'hébergeur lance d'instances automatiquement
    if requetes < SEUIL_ALERTE:
        return INSTANCES_BASE
    elif requetes < SEUIL_CRITIQUE:
        return INSTANCES_BASE * 10
    else:
        return INSTANCES_MAX

def calculer_cout(instances):
    # Coût par seconde = coût horaire divisé par 3600 secondes
    return (COUT_PAR_INSTANCE_HEURE / 3600) * instances

def statut_trafic(requetes):
    # Reprend la logique de filtrage de moniteur_ddos.py
    # True = trafic bloqué par le système de monitoring
    if requetes < SEUIL_ALERTE:
        return "NORMAL", "✅", False
    elif requetes < SEUIL_CRITIQUE:
        return "ALERTE", "⚠️", False
    else:
        return "CRITIQUE", "🚨", True

# --- PROGRAMME PRINCIPAL ---
print("=== Simulation budget cap cloud - La Banque Postale ===")
print("=== Complément de moniteur_ddos.py ===\n")

cout_total = 0
cout_evite = 0

for cycle in range(1, DUREE_SIMULATION + 1):
    requetes = simuler_requetes()
    statut, emoji, bloque = statut_trafic(requetes)
    instances = calculer_instances(requetes)
    cout_cycle = calculer_cout(instances)

    if bloque:
        cout_evite += cout_cycle
        print(f"[Seconde {cycle:02d}] {emoji} {requetes} req/sec → {statut}")
        print(f"           Bloqué par monitoring — coût évité : ${cout_cycle:.4f}")
    else:
        cout_total += cout_cycle
        print(f"[Seconde {cycle:02d}] {emoji} {requetes} req/sec → {statut}")
        print(f"           Coût : ${cout_cycle:.4f} | Total : ${cout_total:.4f}")

    if cout_total >= BUDGET_CAP:
        print(f"\n🚨 BUDGET CAP ATTEINT : ${cout_total:.2f}")
        print("   Auto-scaling bloqué — alerte équipe FinOps envoyée")
        break

    time.sleep(0.5)

print(f"\n=== Résumé final ===")
print(f"Coût total engagé           : ${cout_total:.4f}")
print(f"Coût évité grâce au blocage : ${cout_evite:.4f}")
print(f"\nDans un système réel : un service de budget cap enverrait")
print(f"une alerte automatique avant d'atteindre le plafond.")
