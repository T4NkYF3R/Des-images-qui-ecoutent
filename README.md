# 🧠 **Expérience cognitive:** Des images qui écoutent
*Le lien entre induction musicales et perception de stimuli picturaux neutres*
---
![Python](https://img.shields.io/badge/Python-3.13.9-green?logo=python&style=plastic)
![Tkinter](https://img.shields.io/badge/Tkinter-8.6-orange?style=plastic)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-blue?style=plastic)  
![Release](https://img.shields.io/github/v/release/T4NkYF3R/Des-images-qui-ecoutent?style=plastic)
![Contact](https://img.shields.io/badge/Github-@T4NkYF3R-black?logo=github&logoColor=white&style=plastic)
![Email](https://img.shields.io/badge/Email-contact-yellow?logo=gmail&logoColor=white&style=plastic)

---
> Ce projet est une contribution à une **expérience de psychologie cognitive** de deuxième année de psychologie.  
Il vise à explorer **le lien entre induction musicale et perception visuelle** à travers des stimulis picturaux neutre.

---
## 🔧 **Architecture projet**
```bash
.
│   # Code source
├── /app
│   ├── /assets
│   ├── /window
│   ├── __init__.py
│   ├── config.py
│   ├── data.py
│   └── main.py
│   # Assets du projet
├── /assets
│   ├── /image
│   └── /music
│   # Sauvegarde des résultats
├── /data
│   └── reponses.csv
├── README.md
└── requirement.txt
```

---
## 🛠️ **Installation**
### 1️⃣ **Créer un environnement virtuel**
- **Windows :**
```bash
python3.13 -m venv .venv
.venv\Scripts\activate
```
- **Linux *(Fedora)* :**
```bash
python3.13 -m venv .venv
source .venv/bin/activate
```
### 2️⃣ **Installer les dépendances**
```bash
pip install -r requirements.txt
```
`requirements.txt` contient les bibliotèques nécessaires (`pygame`, etc.)  
`Tkinter` n'est pas inclus car il fait partie de Python standard.
### 3️⃣ **Vérifier que `Tkinter` est installé**
- **Windows :** `Tkinter` est généralement inclus avec Python
- **Linux *(Fedora)* :**
```bash
sudo dnf install python3-tkinter
```
### 4️⃣ **Lancer l'application**
```bash
python -m app.main
```

---
## 📊 **Récupérations des données**
Les données de l'expérience sont enregistrées au format `csv` dans dans le fichier:
```bash
./data/reponse.csv
```
Vous pouvez ouvrir ce fichier avec **Excel** ou un autre tableur.  
Sélectionnez **le point virgule (`;`)** comme séparateur de colonnes.

---
## 👤 **Crédits**
### 👨‍💻 **Equipe de développement**
- **Nicolas Négron ·** [📧 Email](mailto:nicolas.negron@laposte.net) **·** [🌐 Github](https://www.github.com/T4NkYF3R)
### 🎓 **Equipe de recherche**
- **Etudiantes en psychologie cognitive**  
**X ·** [📧 Email](mailto:X@laposte.net)  
**X ·** [📧 Email](mailto:X@laposte.net)  
**X ·** [📧 Email](mailto:X@laposte.net)  
**X ·** [📧 Email](mailto:X@laposte.net)  

---
## ⚖️ **Licence**
© 2025 Nicolas Négron et l'équipe de recherche - Tous droits réservés.
> Le code source est la propriété de Nicolas Négron.  
Le protocole expérimental et la conception scientifique appartient à l'équipe de recherche en psychologie cognitive.  
Toute utilisation, modification ou diffusion nécessite une autorisation préalable.