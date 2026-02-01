import sys
import os
from game_interface import WordleGameInterface
from dictionary_manager import DictionaryManager
from csp_solver import WordleCSPSolver

# Charger le dictionnaire complet
dict_mgr = DictionaryManager()
dict_mgr.load_from_file('../data/wordle_english_5letters.txt')

print(f"📚 Dictionnaire Wordle officiel: {dict_mgr.size()} mots")
print()

# Créer le jeu
game = WordleGameInterface(word_length=5, language="english", use_llm=False)
game.dict_manager = dict_mgr
game.solver = WordleCSPSolver(5, dict_mgr.get_words())

# Menu
print("Choose mode:")
print("  1. Assistant Mode")
print("  2. Solver Mode")

choice = input("\nYour choice (1 or 2): ").strip()

if choice == "1":
    game.play_assistant_mode()
elif choice == "2":
    secret = input("Enter secret word: ").strip().lower()
    if len(secret) == 5:
        game.play_solver_mode(secret)
    else:
        print("Word must be 5 letters!")
else:
    print("Invalid choice!")
