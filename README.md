# Étude de cas — Cybersécurité & La Banque Postale

## Contexte

Entre le 22 décembre 2025 et le 5 janvier 2026, La Banque Postale a subi la plus grande cyberattaque DDoS jamais menée contre un établissement bancaire français, revendiquée par le groupe pro-russe NoName057(16).

En tant que future candidate en école d'ingénieur et en pleine autoformation, j'ai souhaité analyser cet incident pour proposer une approche d'ingénierie défensive complète : **détecter, filtrer et protéger financièrement.**

---

## Les deux scripts

### 1. moniteur_ddos.py — Détection et filtrage applicatif
C'est le premier rempart technique. Ce script simule une analyse intelligente des flux pour différencier un pic de trafic normal d'une agression saturante de type ddos. Ce script se concentre sur l'analyse du taux de requêtes pour protéger la disponibilité du service.

| Niveau | Seuil | Action Technique |
|--------|-------|------------------|
| ✅ **NORMAL** | < 500 req/sec | Surveillance passive et archivage des logs. |
| ⚠️ **ALERTE** | 500 - 2000 req/sec | **Analyse active** : le script identifie les hausses suspectes en temps réel. |
| 🚨 **CRITIQUE** | > 2000 req/sec | **Blocage** : Interruption du trafic pour éviter l'effondrement du serveur. |

### 2. budget_cap.py — Protection contre l'EDoS (Economic Denial of Sustainability)
Ce script traite de la dimension "Cloud" de la cybersécurité. Lors d'un DDoS, les systèmes d'auto-scaling peuvent créer des serveurs en boucle pour absorber l'attaque, faisant exploser la facture. C'est ce qu'on appelle un **EDoS** (Denial of Service financier).

Cette approche est directement inspirée de mon **Bootcamp AWS réalisé en Espagne**, où j'ai appris à manipuler les concepts de plafonnement budgétaire. Le script agit comme un "coupe-circuit" :
- Il comptabilise les coûts engagés selon le trafic.
- Il mesure les pertes évitées grâce au filtrage du premier script.
- Il déclenche une alerte de sécurité si le plafond financier est atteint.

---

## Pourquoi cette approche ?

Pour un ingénieur en cybersécurité, la défense ne s'arrête pas au blocage technique. Ce projet démontre une vision globale de la protection d'un système :
1. **La Disponibilité :** Garantir que les clients accèdent à leurs comptes (Rôle de `moniteur_ddos.py`).
2. **L'Intégrité financière :** Empêcher qu'une attaque ne ruine l'entreprise par sa propre infrastructure Cloud (Rôle de `budget_cap.py`).
3. **La Résolution de problème :** Transformer un incident réel en une solution logicielle structurée.

---

## Environnement technique

Projet réalisé dans des conditions proches de l'administration système réelle :
*   **Langage :** Python 3.
*   **Système :** Environnement Linux (Ubuntu).
*   **Édition :** Travail direct en terminal via **Vim** et **Nano**.
*   **Compétences Cloud :** Logique de monitoring et gestion de budget (Culture AWS).

---

## Auteur

**Mathilde Burgaud**
Candidate en cybersécurité
Mai 2026
