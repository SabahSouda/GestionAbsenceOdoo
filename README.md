SABAH SOUDA - G2 
# 📚 Gestion des Absences des Professeurs 

## 📌 Description
Ce projet est un **mini-module Odoo** permettant de gérer les absences des professeurs.  
Il propose un tableau de bord simple avec deux espaces :
- **Espace Professeur** : déclaration rapide des absences.
- **Espace Responsable** : consultation des statistiques et validation des demandes et gestion des professeurs.

Ce projet a été réalisé dans un cadre académique afin de mettre en pratique le développement de modules Odoo, la conteneurisation avec Docker et la documentation technique avec LaTeX.

---

## 🛠️ Outils et technologies
- **Odoo** : ERP open-source utilisé comme framework principal.
- **Python** : logique métier et définition des modèles.
- **Docker** : conteneurisation pour un déploiement reproductible.
- **PostgreSQL** : base de données relationnelle.
- **VS Code** : environnement de développement.
- **LaTeX** : rédaction du rapport académique.

---

## ⚙️ Installation et démarrage

1. **Cloner le projet :**
   ```bash
   git clone https://github.com/SabahSouda/GestionAbsenceOdoo.git
   cd GestionAbsenceOdoo

2. **Lancer les conteneurs Docker :**
docker-compose up -d

3. **Accéder à Odoo :**
http://localhost:8069

4. **Mettre à jour la liste des modules et installer :**

Aller dans le menu Apps.

Cliquer sur Update Apps List.

Rechercher Gestion des Absences des Professeurs.

Cliquer sur Activate.

