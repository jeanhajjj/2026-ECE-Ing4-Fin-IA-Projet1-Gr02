import sys
sys.path.insert(0, 'src')

# Lire le fichier
with open('src/game_interface.py', 'r') as f:
    content = f.read()

# Chercher et remplacer
old_code = '''        if language.lower() == "french":
            self.dict_manager.load_default_french()
        else:
            self.dict_manager.load_default_english()'''

new_code = '''        # Essayer de charger depuis les fichiers, sinon utiliser les dictionnaires par défaut
        if language.lower() == "french":
            try:
                self.dict_manager.load_from_file('data/mon_dictionnaire_francais.txt')
                print(f"✅ Dictionnaire français personnalisé chargé ({self.dict_manager.size()} mots)")
            except FileNotFoundError:
                self.dict_manager.load_default_french()
                print(f"⚠️  Utilisation du dictionnaire français par défaut ({self.dict_manager.size()} mots)")
        else:
            try:
                self.dict_manager.load_from_file('data/wordle_english_5letters.txt')
                print(f"✅ Dictionnaire anglais complet chargé ({self.dict_manager.size()} mots)")
            except FileNotFoundError:
                self.dict_manager.load_default_english()
                print(f"⚠️  Utilisation du dictionnaire anglais par défaut ({self.dict_manager.size()} mots)")'''

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('src/game_interface.py', 'w') as f:
        f.write(content)
    print("✅ Fichier game_interface.py modifié avec succès!")
else:
    print("❌ Code d'origine non trouvé. Modification manuelle nécessaire.")
