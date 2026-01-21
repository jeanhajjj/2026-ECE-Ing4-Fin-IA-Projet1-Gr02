import sys
sys.path.insert(0, 'src')
from game_interface import WordleGameInterface
from dictionary_manager import DictionaryManager
from csp_solver import WordleCSPSolver

# Charger votre dictionnaire personnalisé
dict_mgr = DictionaryManager()
dict_mgr.load_from_file('data/mon_dictionnaire_francais.txt')

print(f"🇫🇷 Dictionnaire personnel chargé: {dict_mgr.size()} mots")
print(f"✅ FLEUR présent: {dict_mgr.contains('fleur')}")
print(f"✅ COEUR présent: {dict_mgr.contains('coeur')}")
print(f"✅ SULLY présent: {dict_mgr.contains('sully')}")
print()

# Créer le jeu avec votre dictionnaire
game = WordleGameInterface(word_length=5, language="french", use_llm=False)
game.dict_manager = dict_mgr
game.solver = WordleCSPSolver(5, dict_mgr.get_words())

# Lancer le menu
print("🎮 Bienvenue au Wordle CSP Solver !")
print("=" * 60)
print()
print("Choisissez un mode:")
print("  1. Mode Assistant - Je vous aide à résoudre")
print("  2. Mode Auto - Regardez-moi résoudre")
print()

choice = input("Votre choix (1 ou 2): ").strip()

if choice == "1":
    print("\n🎮 Mode Assistant activé\n")
    game.play_assistant_mode()
elif choice == "2":
    secret = input("\nEntrez le mot secret (5 lettres): ").strip().lower()
    if len(secret) == 5:
        print(f"\n🤖 Je vais trouver '{secret.upper()}'...\n")
        game.play_solver_mode(secret)
    else:
        print("❌ Le mot doit faire 5 lettres!")
else:
    print("❌ Choix invalide!")
