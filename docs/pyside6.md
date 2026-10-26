# UI avec Pyside6 PYTHON

## installer et lancer

```bash
. venv/bin/activate
pip3 install Pyside6
pyside6-designer &
```

```powershell
.\.venv\Scripts\Activate.ps1
pip install Pyside6
start pyside6-designer
```

## dessiner

* *sélectionner* `Main window`
* *Drag & Drop* : 
  + `TextEdit` 
  + `SpinBox` 
  + `ListWidget`
  + `PushButton` => à droite
  + 2 `Labels`
  + 2 `Spacers`

* *répartir*:
  + sélection "spacer horizontal" + "bouton"
  + click-droit > "Layout" ou "mise en page" > "horizontal" 
  + sélection de tout
  + click-droit > "Layout" ou "mise en page" > "Formulaire"

* *redimensionner*
  + click en dehors du widget 
  + click-droit > "Layout" ou "mise en page" > "grid"

* *nommer* dans le python
  + `Labels`: `Texte` et `Nb Mots Signifiants`
  + `PushButton`: `OK`
  + `PushButton`: `objectName: okBtn` dans `QObject` à droite
  + `SpinBox`: `objectName: signWords` dans `QObject` à droite
  + `SpinBox`: `minimum: 1` dans `QSpinBox` à droite
  + `SpinBox`: `maximum: 10` dans `QSpinBox` à droite
  + `SpinBox`: `value: 3` dans `QSpinBox` à droite

* sauvegarder: `Ctrl + s` analyzer.ui dans le dossier gui

## générer le layout

```powershell
# exécuter: pyside6-uic analyzer.ui et voir le nom de la classe
# générée: Ui_MainWindow
pyside6-uic gui_analyser.ui -o gui_MainWindow.py
```

## dans le module gui_starter_init pour dynamiser le widget

1. ajouter la classe `Ui_MainWindow` 
   * dans la classe "fenêtre" `MyWindow`
   * avec un `héritage multiple`

2. exécuter la méthode héritée `self.setupUi(self)` 
   * de ``Ui_MainWindow`
   * dans le `__init__`

3. ajouter une gestion d'évènement sur le bouton
   * utiliser l'attribut `okBtn` hérité
   * *connecter* l'évènenement `clicked` de cet l'attribut
   * avec une méthode à écrire `on_okBtn_clicked` dans la classe `MyWindow`
   * cette méthode va trouver le contenu du `TextEdit`
   * instancier le `Counter`
   * ajouter les résultats dans `listWidget`

4. lancer l'application `gui_app.py` avec python

### mise à jour du layout

1. ouvrir `analyzer.ui` dans `pyside6-designer`
   récents > `analyzer.ui` ou fichier > ouvrir > `analyzer.ui`
2. effectuer les modifications nécessaires sur les widgets
   + le plus efficace est de casser la mise en page courante: clic-droit sur mettre en page > "Casser la mise en page"
   + refaire le layout/mise en page (verticale / horizontale / formulaire ==> grille)
3. sauvegarder le fichier
4. régénérer le fichier Python avec `pyside6-uic gui_analyser.ui -o gui_MainWindow.py`

### transformer l'application python en .exe

1. installer `pyinstaller` si ce n'est pas déjà fait:

```bash
pip install pyinstaller
```
2. créer le fichier exécutable:

```bash
pyinstaller --onefile --windowed ./gui_app.py
```

3. les dossier build et dist vont être créés mais doivent être gitignorés

4. l'exécutable est dans le dossier `dist`