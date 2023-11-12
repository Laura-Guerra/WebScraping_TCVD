# Pràctica 1. Web Scrapping
Aquest projecte s'ha realitzat per a l'assignatura Tipologia i cicle de vida de les dades del Màster Universitari en Ciència de Dades de la Universitat Oberta de Catalunya. L’objectiu de la pràctica és aplicar tècniques de web scraping mitjançant Python per tal d’extreure les dades del portal immobiliari pisos.ad, que s’utilitzaran posteriorment per analitzar el mercat immobiliari andorrà des de diferents perspectives. 

## Estructura del projecte

El repositori consta de les carpetes següents:
* data: conté un fitxer en format csv amb els identificadors, tipus de transaccions (venda o lloguer), zones i enllaços de les diferents propietats publicades al portal. 
* dataset: conté un fitxer en format csv amb les dades extretes de la pàgina. A la memòria de la pràctica es pot trobar una descripció detallada del conjunt de dades.
* report: conté la memòria de la pràctica. 
  * images: conté el diagrama del projecte.
* source: conté el codi utilitzat per realitzar el web scraping. El codi està dividit en els següents fitxers:
  * constants.py: fitxer on es defineixen les diferents constants necessàries al llarg del procés (enllaços base, classes, filtres, rutes...).
  * utils_files.py: fitxer on es defineixen les funcions necessàries per generar i llegir els fitxers csv. 
  * utils_scraping.py: fitxer on es defineixen les funcions d'obtenció dels enllaços i del contingut d'aquests.
  * utils_url.py: fitxer on es defineix la funció que genera els diferents enllaços sobre els quals s'itera. 
  * main.py: codi principal a través del qual es criden les diferents funcions necessàries per realitzar el procés de scraping. 


## Autors
Aquest projecte ha estat desenvolupat per Àlex Tort i Laura Guerra.

## Llicència
Aquest projecte està disponible sota la Llicència Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0). 

La utilització d'aquesta llicència té l'objectiu de fomentar un ús lliure, obert i transparent de les dades, així com promoure la compartició de coneixement.

Aquesta llicència permet a tercers:

* Copiar i redistribuir el material en qualsevol mitjà o format
* Adaptar, modificar i transformar el material

Per a qualsevol propòsit, inclòs comercial, sempre que es compleixin amb els següents termes:

* S'ha de reconèixer l'autoria de manera apropiada, proporcionar un enllaç a la llicència i indicant si s'han realitzat canvis al material original.
* En el cas de modificar o crear a partir del material original, s'han de distribuir sota la mateixa llicència que l'original.

Per més informació sobre la llicència visitar [Creative Commons](https://creativecommons.org/licenses/by-sa/4.0/deed.es)
