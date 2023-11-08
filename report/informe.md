# TÍTOL

## INTRODUCCIÓ
Durant els darrers anys Barcelona ha experimentat un augment molt significatiu en l’afluència de turistes, convertint-se en un dels principals destins del país, i segurament, del continent. Aquest creixement del turisme ha transformat de forma significativa tant la industria com la pròpia ciutat. Si bé alguns dels canvis han estat positius, com per exemple la creació d’ocupació o l’augment d’oportunitats econòmiques, també ha tingut un impacte negatiu en la vida dels habitants de la ciutat, que han vist com el seus barris han experimentat un augment en el nombre de visitants, convertint-se en barris gentrificats on l’alta demanda d’allotjament ha donat lloc a l’aparició d’allotjaments turístics de curta estada.

Una de les principals plataformes de reserves d’allotjaments d’aquestes característiques és Airbnb, una plataforma de lloguers temporals que permet als turistes allotjar-se en pisos, apartaments o habitacions durant la seva estada a la ciutat. Aquesta plataforma, per tant, pot considerar-se una font d’informació sobre el perfil de turisme que visita la ciutat, i per tant, permet entendre millor la nova realitat turística de Barcelona i poder gestionar-la de forma més eficient i efectiva per millorar l’experiència de totes les parts implicades.

Tractant-se d’una plataforma molt estesa i coneguda, i tenint en compte les mesures de verificació i procediments de la plataforma, pot considerar-se que les dades que es puguin extreure d’aquesta seran d’elevada fiabilitat.

Així, hem considerat que l’anàlisi de la informació continguda en aquesta pàgina a través del web scraping pot ser de gran utilitat a autoritats, empreses i professionals del turisme.  Si bé es detalla més extensament a l’apartat 7, l’anàlisi del contingut d’Airbnb pot permetre, per exemple, avaluar la distribució geogràfica de les reserves d'allotjament, les temporades de major afluència, la identificació de zones amb una major pressió turística… Amb aquesta informació es pot plantejar la limitació de l'expansió d'ofertes de pisos turístics o la definició de polítiques que promoguin una distribució equitativa d'allotjament a la ciutat.

No obstant, les dades també poden contribuir en la definició d’estratègies de gestió turística: a través de l’anàlisi de les temporades de major afluència es pot planificar de forma més eficient els recursos, reforçant infraestructures com els sistemes de transport públic o incrementant la presència policial en certes zones.


## DESCRIPCIÓ I CONTINGUT DEL DATASET
TBD


## PROPIETARI
El conjunt de dades recollit i analitzat en aquest projecte pertany a la plataforma Airbnb. Són dades obtingudes públicament a través de *** disponibles a la pàgina web utilitzant tècniques de web scraping, respectant els termes i condicions del portal web. La propietat intel·lectual dels dades originals pertany a l'empresa Airbnb, Inc. i no s'han infringit els drets de propietat de l'entitat ni la privacitat dels usuaris implicats en les dades recollides.


Per garantir una pràctica ètica i legal s'ha fet una revisió dels termes i condicions d'Airbnb i del seu arxiu robots.txt. A més, durant el procés de recopilació de dades, no s'han recopilat dades personals ni informació que pugui ser utilitzada per identificar directament als usuaris del portal web.

*FALTA LA PART DE PROJECTES ANTERIORS*
https://www.nerdwallet.com/article/travel/airbnb-pricing-statistics
https://www.sciencedirect.com/science/article/pii/S0261517721000388


## INSPIRACIÓ
Tal i com s’ha indicat en un dels apartats anteriors, el conjunt de dades inclou, entre d’altres, el nombre d’habitacions i de llits dels quals disposen els diferents allotjaments, així com el preu, la valoració mitjana, el nombre de valoracions i el temps que porta publicat l’anunci. A partir d’aquest conjunt relativament reduït de variables, es pot extreure un gran nombre d’informació referent tant a la distribució de preus dels allotjaments com a l’afluència de visitants o les preferències d’aquests.
En primer lloc, cal destacar que les dades s’han extret per tres dates diferents. A part, també s’indica si l’allotjament està reservat o disponible per les dates corresponents. Les dates escollides intenten reflectir el que considerem com temporada baixa (en aquest cas, de dilluns a dimecres una setmana qualsevol de novembre), temporada mitja (un cap de setmana de novembre) i temporada alta (el cap de setmana de la Puríssima).  Alhora, s’ha dividit Barcelona, una de les ciutats més turístiques del país, en sis zones diferents. Així, és possible estudiar l’evolució de l’ocupació dels allotjaments turístics, i per tant l’afluència de turisme a la ciutat, en funció de les dates i de la ubicació dels allotjaments. A part, també es pot realitzar un estudi de l’evolutiu dels preus en funció d’aquestes variables, així com una comparació dels preus en funció d’altres variables com la seva  valoració mitjana.

En segon lloc, també es pot estudiar la relació entre la popularitat d’un allotjament i la seva valoració mitjana, la seva ubicació, el seu preu o els serveis que ofereix. Si suposem que el nombre total de valoracions reflecteix en certa mesura el nombre de reserves que ha tingut un allotjament, i tenim en compte el temps que aquest porta publicat a la pàgina, podem determinar la popularitat d’aquest, i buscar una relació amb les variables esmentades. A part, també es pot cercar una explicació per a la valoració mitjana de l’allotjament en funció de les diferents variables de les quals es disposa.
Considerem, que tota aquesta informació pot ser molt útil per tenir una idea del perfil de turista que visita la ciutat, sobretot tenint en compte que el turisme és un dels motors principals de l’economia d’aquesta i en general, del país. A més, el conjunt de dades podria utilitzar-se tant per part d’organismes públics, amb les finalitats introduïdes al primer apartat de la memòria, com pel sector privat: les dades extretes permeten desenvolupar estratègies de màrqueting més efectives, adaptant l’oferta en funció de les necessitats i interessos del turisme. Alhora, també es poden utilitzar per segmentar els preus de forma més precisa, adaptant les tarifes en funció de les preferències i característiques del turista així com a l’època de l’any i la ubicació. Fins i tot es podria optar per ajustar els preus de forma dinàmica segons l’anticipació de la reserva o la demanda actual. 

Finalment, també es podria utilitzar aquesta informació per comparar els preus amb altres allotjaments similars, avaluant així la competitivitat de l’allotjament i ajustant els preus en cas que sigui necessari.
Si bé s’han realitzat estudis similars, com en l’anàlisi XXX, considerem que el fet de distribuir els allotjaments per zones delimitades i escollir un conjunt de dates diferents pot aportar informació addicional als informes publicats.

## LLICÈNCIA
Aquest projecte està disponible sota la Llicència Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0). 

La utilització d'aquesta llicència té l'objectiu de fomentar un ús lliure, obert i transparent de les dades, així com promoure la compartició de coneixement.

Aquesta llicència permet a tercers:

- Copiar i redistribuir el material en qualsevol mitjà o format
- Adaptar, modificar i transformar el material

Per a qualsevol propòsit, inclòs comercial, sempre que es compleixin amb els següents termes:

- S'ha de reconèixer l'autoria de manera apropiada, proporcionar un enllaç a la llicència i indicant si s'han realitzat canvis al material original.
- En el cas de modificar o crear a partir del material original, s'han de distribuir sota la mateixa llicència que l'original.