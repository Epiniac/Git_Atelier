# Git_Atelier
Un tableau de bord collaboratif affichant les performances et contributions des membres d’une équipe.

## 🎯 Objectif
Construire une application web interactive qui affiche des statistiques d’activité d’équipe à partir de données. Le projet est conçu pour encourager la collaboration via Git & GitHub et renforcer les compétences en développement web et traitement de données.

## 🚀 Fonctionnalités
- Affichage des métriques de contribution
- Visualisation des tâches accomplies et de l’activité
- Filtres dynamiques (ex. : par date)
- Graphiques interactifs
- Intégration optionnelle avec une API Flask

## 🛠️ Instructions de démarrage
- Ouvrir `frontend/index.html` dans un navigateur (version statique)
- Ou lancer le backend Flask : `python backend/app.py`

## 📝 Tâches à réaliser (TODO)
- [ ] Ajouter un champ de filtre de dates sur le tableau de bord
- [ ] Afficher un graphique (commits par membre, tâches complétées, etc.)
- [ ] Appliquer un design responsive
- [ ] Implémenter un tri par nombre de tâches ou de commits
- [ ] Côté backend : permettre de filtrer via des paramètres dans l’URL

## 📁 Structure du projet
```
/Git_Atelier
├── frontend/         # Interface web (HTML/CSS/JS ou React)
├── data/             # Sources de données JSON ou CSV
├── backend/          # API Flask (facultative)
├── .gitignore
└── README.md
```


## 🤝 Contribution
- Créer une branche pour chaque tâche (`feature/filtre-date`, `fix/bug-affichage`...)
- Ouvrir une Pull Request et demander une revue
- Valider les PRs des coéquipiers

## 📚 Bonnes pratiques Git
- Branches nommées :
  - `feature/<nom>` pour les nouvelles fonctionnalités
  - `fix/<nom>` pour les corrections de bugs
  - `refactor/<nom>` pour les améliorations de code
