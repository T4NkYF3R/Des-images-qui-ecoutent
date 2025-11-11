# 🧠 **Hearsee**
*Des images qui écoutent: Le lien entre induction musicales et perception de stimuli picturaux neutres*
---
![Python](https://img.shields.io/badge/Python-3.12-green?logo=python&style=plastic)
![Tkinter](https://img.shields.io/badge/Tkinter-8.6-orange?style=plastic)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-blue?style=plastic)
![Pillow](https://img.shields.io/badge/Pillow-12.0.0-purple?style=plastic)  
![Release](https://img.shields.io/github/v/release/T4NkYF3R/Hearsee?include_prereleases&display_name=tag&logo=github&color=red&style=plastic)
![Contact](https://img.shields.io/badge/Github-@T4NkYF3R-black?logo=github&logoColor=white&style=plastic)
![Email](https://img.shields.io/badge/Email-contact-yellow?logo=gmail&logoColor=white&style=plastic)

---
> 🧩 Ce projet est une contribution à une **expérience de psychologie cognitive** de deuxième année de psychologie.  
Il vise à explorer **le lien entre induction musicale et perception visuelle** à travers des stimulis picturaux neutre.

---
## 🧱 **Architecture projet**
```bash
Hearsee/
│
├── .github/            # Configuration GitHub
│   └── workflows/
│
├── app/                # Code source de l'application
│   ├── assets/
│   ├── window/
│   ├── __init__.py
│   ├── config.py
│   ├── data.py
│   └── main.py
│
├── assets/             # Ressources pour l'expérience
│   ├── image/
│   └── music/
│
├── data/               # Données enregistrées pendant l'expérience
│   └── reponses.csv
│
├── devops/             # Scripts et configuration DevOps
│   └── scripts/
│
├── README.md
└── requirements.txt
```

---
## ⚙️ **Installation**
### 0️⃣ **Installer Python**
Si vous n'avez pas `Python 3.12` vous pouvez le télécharger depuis le site officiel:  
➡️ [Python 3.12](https://www.python.org/downloads/release/python-31210/)
### 1️⃣ **Cloner le dépôt**
```bash
git clone https://github.com/T4NkYF3R/Hearsee
cd Hearsee
```
### 2️⃣ **Créer un environnement virtuel**
- **Windows :**
```bash
python3.12 -m venv .venv
.venv\Scripts\activate
```
- **Linux / macOS :**
```bash
python3.12 -m venv .venv
source .venv/bin/activate
```
### 3️⃣ **Installer les dépendances**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
📦 `requirements.txt` contient les bibliotèques nécessaires (`pygame`, etc.)  
🧩 `Tkinter` fait partie de Python standard, mais peut nécessiter une installation manuelle sur Linux.
### 4️⃣ **Vérifier que `Tkinter` est installé**
- **Windows :** `Tkinter` est généralement inclus avec Python
- **Linux :**
```bash
sudo dnf install python3-tkinter
```
### 5️⃣ **Lancer l'application**
```bash
python -m app.main
```

---
## 📂 **Assets *(pour les développeurs)***
### 🖼️ **Images**
**Chemin** : `./assets/image`  
Les images fonctionnent par **pairs** 🔗.  
➡️ Vous aurez besoin de **10 pairs** d'images.  
#### 🗂️ **Nomenclature attendue**  
Les fichiers doivent suivre le format:
```css
nom_1.[png|jpeg|jpg|gif|bmp]
nom_2.[png|jpeg|jpg|gif|bmp]
```
💡 Exemple : `image_1.png` et `image_2.png`
### 🎵 **Musiques**
**Chemin** : `./assets/music`  
Il vous faut **2 musiques** 🎶  
Assurez-vous qu'elles soient prêtes avant de lancer l'expérience 🧠.
#### 🗂️ **Format acceptés**
Les fichiers doivent êtres d'un des formats suivant:
```css
.mp3
.wav
.ogg
.flac
```

---
## 🎓 **L'experience**
- L'expérience se déroule en **2 sessions** 🧩.
- Une pause est prévu entre chaque session ☕.
### 🎶 Déroulement d'une session
- La **musique** est joué pendant **tout la durée de la session** 🎧.
- La session commence par **30 secondes** sans **stimuli visuels** 🕐 afin de favoriser la **concentration sur la musique** 🎵.
- Vous devrez ensuite **enregistrer votre niveau de ressenti** pour les **10 images** présentées 🖼️💭.

---
## 📊 **Récupérations des données**
Les données de l'expérience sont enregistrées au format `csv` dans dans le fichier:
```bash
./data/reponse.csv
```
🗂️ Ce fichier peut être ouvert avec **Excel** ou un autre tableur.  
➡️ Sélectionnez **le point virgule (`;`)** comme séparateur de colonnes.

---
## 👤 **Crédits**
### 👨‍💻 **Equipe de développement**
- **Nicolas Négron ·** [📧 Email](mailto:nicolas.negron@laposte.net) **·** [🌐 Github](https://www.github.com/T4NkYF3R)
### 🎓 **Equipe de recherche**
- | **Etudiantes en psychologie cognitive** |                                                       |
  |-----------------------------------------|-------------------------------------------------------|
  | **Julia Raevesteyn**                    | **·** [📧 Email](mailto:raevesteyn.gestion@gmail.com) |
  | **Marie De Champeville**                | **·** [📧 Email](mailto:mdechampevillepro@gmail.com)  |
  | **Cléo Porta**                          | **·** [📧 Email](mailto:cleoporta2004@gmail.com)      |
  | **Cécille Queyroy**                     | **·** [📧 Email](mailto:queyroycecile.lhm@gmail.com)  |

---
## ⚖️ **Licence**
© 2025 Nicolas Négron et l'équipe de recherche - Tous droits réservés.
> 💡 Le code source est la propriété de Nicolas Négron.  
🧠 Le protocole expérimental et la conception scientifique appartient à l'équipe de recherche en psychologie cognitive.  
Toute utilisation, modification ou diffusion nécessite une autorisation préalable.

---
📦 Pour plus de détails sur l'évolution du projet, consultez la section **[Releases](https://github.com/T4NkYF3R/Hearsee/releases)** du dépôt.