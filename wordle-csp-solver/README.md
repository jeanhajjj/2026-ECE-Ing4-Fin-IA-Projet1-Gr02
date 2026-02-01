# 🎮 Wordle CSP Solver

Slides : https://gamma.app/docs/Wordle-CSP-Solver-avec-integration-LLM-7o9ldqgi3d76b0g

## Vue d'ensemble

**Wordle CSP Solver** est un résolveur IA sophistiqué pour le jeu Wordle utilisant des algorithmes de **Constraint Satisfaction** combinés avec la **théorie de l'information** et une intégration optionnelle d'LLM.

### ✨ Caractéristiques principales

- **Solveur CSP avancé** : Propagation de contraintes pour éliminer les possibilités
- **Optimisation par théorie de l'information** : Entropie de Shannon pour gain maximal
- **Multiples stratégies** : Maximisation d'information, minimax, analyse de fréquence
- **Intégration LLM** : Raisonnement avancé avec OpenAI GPT-4
- **Support bilingue** : Dictionnaires anglais et français
- **3 modes de jeu** : Assistant, Automatique, Hybride LLM
- **Statistiques en temps réel** : Suivi de l'élimination des mots

### 📊 Performance

- **Moyenne** : 3.6 coups (limite : 6)
- **Succès** : 100% des Wordles résolus
- **Algorithmes** : CSP + Entropie + Minimax

## 🚀 Démarrage rapide

### Installation rapide

```bash
cd wordle-csp-solver
pip install -r src/requirements.txt
```

### Lancer un jeu

```bash
python src/jouer_english_complet.py    # Mode Assistant (Anglais)
python src/jouer_francais_perso.py     # Mode Assistant (Français)
python src/demo.py                     # Démonstrations
```

**Pour plus de détails d'installation**, consultez [INSTALLATION.md](INSTALLATION.md).

## 📚 Structure du projet

```
src/
  ├── csp_solver.py          # Moteur CSP principal
  ├── optimizer.py           # Stratégies d'optimisation
  ├── dictionary_manager.py  # Gestion des dictionnaires
  ├── llm_integration.py     # Intégration OpenAI
  ├── game_interface.py      # Interface CLI
  ├── demo.py                # Démonstrations
  ├── test_*.py              # Tests (15 tests, 100% pass)
  ├── jouer_*.py             # Interfaces de jeu
  ├── requirements.txt       # Dépendances
  ├── .env.example           # Configuration OpenAI
  └── __init__.py
```

## 🔑 Concepts clés

### Constraint Satisfaction Problem (CSP)

Le solveur modélise Wordle comme un CSP :
- **Variables** : Les 5 positions du mot
- **Domaines** : Lettres a-z pour chaque position
- **Contraintes** : Les feedbacks (vert=correct, jaune=présent, gris=absent)

### Entropie de Shannon

Pour chaque mot candidat, nous calculons combien d'information il apporte :

```
Entropie = -Σ p(pattern) × log₂(p(pattern))
```

Les mots à entropie élevée réduisent rapidement l'espace de recherche.

### Stratégies

| Stratégie | Approche | Cas d'usage |
|-----------|----------|-----------|
| **max_info** | Maximiser l'entropie | Résolution rapide |
| **minimax** | Minimiser le pire cas | Garantir ≤6 coups |
| **frequency** | Lettres fréquentes | Mode difficile |

## 💡 Modes de jeu

### Mode Assistant

```bash
python src/jouer_english_complet.py
```

Le solveur vous propose les meilleurs mots et affiche les statistiques.

### Mode Automatique

```python
from src.game_interface import WordleGameInterface
interface = WordleGameInterface()
interface.play_solver_mode("house")  # Résout le secret "house"
```

Le solveur résout un mot secret automatiquement.

### Mode Hybride LLM

Requiert une clé API OpenAI. Le LLM peut appeler 5 fonctions :
1. `apply_wordle_constraints` - Appliquer un feedback
2. `get_possible_words` - Lister les mots possibles
3. `suggest_best_guess` - Suggérer un mot
4. `get_solver_stats` - Obtenir les statistiques
5. `analyze_word_pattern` - Analyser les patterns

## 🧠 Architecture

```
┌──────────────────┐
│  game_interface  │ ← Interface utilisateur (CLI)
└────────┬─────────┘
         │
    ┌────┴─────┬────────┬──────────┐
    ▼          ▼        ▼          ▼
 ┌─────────┐ ┌────────┐ ┌────┐ ┌──────────┐
 │CSP Solver  │Optimizer │ LLM│ │Dictionary│
 └────┬────┘ └───┬────┘ └┬───┘ └──────────┘
      │          │       │
      └──────────┴───────┘
```

## 📖 Documentation complète

- **[INSTALLATION.md](INSTALLATION.md)** : Installation, configuration, lancement
- **[DOCUMENTATION.md](DOCUMENTATION.md)** : API complète, algorithmes, exemples avancés

## 🧪 Tests

```bash
python -m pytest src/test_*.py      # Tous les tests
python src/test_csp_solver.py       # Tests CSP (7)
python src/test_optimizer.py        # Tests Optimizer (8)
```

**Résultats** : 15/15 tests ✅

## 🔧 Configuration LLM (optionnel)

1. Créer un fichier `src/.env`
2. Ajouter votre clé OpenAI :
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```
3. Utiliser le mode hybride

## 📦 Dépendances

```
colorama       # Couleurs CLI
python-dotenv  # Variables d'environnement
openai         # API OpenAI (optionnel)
```

## 🎯 Résultats et métriques

### Effectivité

| Métrique | Valeur |
|----------|--------|
| Tentatives moyennes | 3.6 |
| Taux de réussite | 100% |
| Mode difficile | Supporté ✅ |
| Multilingue | Oui (EN/FR) |

### Complexité algorithmique

| Opération | Complexité |
|-----------|-----------|
| Appliquer feedback | O(n) |
| Calculer entropie | O(n²) |
| Meilleur mot | O(n² × c) |

## 🚀 Prochaines étapes

- Lire [INSTALLATION.md](INSTALLATION.md) pour l'installation détaillée
- Consulter [DOCUMENTATION.md](DOCUMENTATION.md) pour l'API complète
- Exécuter `python src/demo.py` pour voir des exemples
- Analyser le code source dans `src/` pour comprendre les détails

## 📝 Licence

Voir fichier [LICENSE](../LICENSE)

---

**Besoin d'aide ?** Consultez [INSTALLATION.md](INSTALLATION.md#troubleshooting) pour dépanner les problèmes courants.
