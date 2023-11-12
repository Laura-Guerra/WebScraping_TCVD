# TÍTOL

## INTRODUCCIÓ
Durant els últims anys el mercat immobiliari andorrà ha observat un augment notable en la demanda d’habitatges, tant de compra com de lloguer, degut al creixent interès de residents estrangers pel país. A part dels avantatges fiscals, altres incentius com la baixa taxa d’atur, l’entorn o la qualitat de vida han convertit a Andorra en un dels països amb un nombre més elevat de nous residents. Aquesta increment de residents ha fet augmentar la demanda d’habitatges, fins al punt en què aquesta supera l’oferta disponible. 

Degut a la geografia del país, envoltat per muntanyes, el desenvolupament immobiliari està restringit físicament. Aquesta limitació territorial i l’augment en la demanda esmentada ha donat lloc a un mercat molt competitiu amb preus constantment a l’alça; convertint l’accés a l’habitatge en un problema de dimensions cada vegada majors. Moltes persones, tant de nacionalitat andorrana com potencials nous residents, s’han vist obligats a buscar alternatives que sovint impliquen buscar un habitatge a localitats properes però fora del país, com per exemple La Seu d’Urgell. 

Per aquests motius hem considerat que disposar de dades detallades del mercat immobiliari andorrà, tant de venta com de lloguer, pot resultar molt útil. En aquest aspecte, obtenir dades d’una pàgina web immobiliària permet obtenir dades per zona geogràfica, tipus d'habitatge i altres característiques específiques a partir de les quals es pot estudiar la distribució de preus, determinant, per exemple, els factors que influeixen en la diferència d’aquest. També es pot estudiar quines parròquies estan experimentant un major creixement, i determinar si cal dur a terme alguna acció en conseqüència. 

Així, la plataforma escollida ha estat www.pisos.ad , un dels portals immobiliaris andorrans amb una major oferta de propietats. Tal com anuncien al seu portal, disposen de més de 3.000 propietats, publicades bé per particulars bé per una de les 34 immobiliàries que utilitzen la plataforma.  A part, la plataforma permet cercar immobles per parròquia, facilitant així la classificació d’aquests en funció de la seva ubicació. L’elevada oferta, així com la popularitat de la pàgina entre els residents del país, ens ha conduit a considerar aquest portal com el més indicat per dur a terme l’estudi proposat en aquesta introducció i que es detalla en més profunditat als apartats posteriors. 


## DESCRIPCIÓ DEL DATASET

Per tal de dur a terme l’estudi proposat a l’apartat anterior, s’ha recopilat informació de totes les propietats publicades al portal immobiliari a data del 9 de novembre de 2023, classificant-les en funció de la tipologia de transacció (venda o lloguer) i per parròquia. Si bé no es pot garantir que les dades actuals són estrictament d’habitatges, durant el procés de neteja del conjunt de dades es pot garantir el filtratge d’aquelles que no es corresponen amb aquesta categoria a través de la variable referent al nombre d’habitacions. 

## REPRESENTACIÓ GRÀFICA
<image src="./images/diagram.png" alt="Diagram">

## CONTINGUT

Cada registre del conjunt de dades correspon a un anunci publicat al portal. No obstant, no necessàriament ha de tractar-se d’una propietat en particular, ja que diferents agències poden publicar anuncis de la mateixa propietat. Així doncs, per cada registre, es recullen les dades següents:

*	Price: preu establert a l’anunci. En cas de tractar-se d’una propietat de lloguer, el preu correspon al preu mensual d’aquesta. El format actual de la variable és el valor en format text, amb punts als milers i en €. 
*	Area: superfície de la propietat, em m2. De nou, actualment es tracta d’una variable textual composta pel valor de la superfície de la propietat i les unitats corresponents. 
*	Bedrooms: nombre d’habitacions de la propietat. En cas de no tractar-se d’un immoble, aquesta variable té com a valor “0 Habitacions”. 
*	Parking: variable categòrica binària que indica si la propietat disposa de garatge. Els seus valors són “Inclòs” i “No Inclòs”. 
*	Features: llista de característiques de la propietat.
*	Agency: nom de l’agència immobiliària que ha publicat l’anunci. 
*	Id: identificador numèric únic de l’anunci, que es correspon amb la referència del portal. 
*	Type: tipologia de la transacció anunciada. Els possibles valors de la variable són “venda” i “lloguer”. 
*	Zone: parròquia on es troba ubicada la propietat. Els possibles valors són "ordino",  "canillo", "encamp", "andorra-la-vella", "sant-julia-de-loria", "escaldes-engordany" i  "la-massana". 
*	URL: enllaç de l’anunci.
*	Timestamp: data i hora de l’extracció. Degut a l’elevada demanda, és possible que part dels anuncis (sobretot els de lloguer) deixin d’estar publicats al portal al cap d’uns dies i per tant no es pugui accedir de nou a la informació. Per aquest motiu s’ha considerat rellevant indicar el període al qual pertanyen les dades. 

El conjunt de dades pot trobar-se a https://doi.org/10.5281/zenodo.10112197. 

## PROPIETARI

Avís Legal s'informa que www.pisos.ad és un domini de l'empresa ANTONI CAPELLA FERNANDEZ (en endavant "PISOS.AD") amb domicili social al Av de les Escoles, 31 – 5º5ª -AD700- ESCALDES-ENGORDANY (PRINCIPAT D’ANDORRA), i correu
electrònic: info@pisos.ad

Inscrita al Registre de Comerç del Principat d’Andorra amb número 920418-Z i amb número de Registre Tributari F-033235-T

Després de verificar els termes i condicions, així com el fitxer robots.txt de PISOS.AD, s'ha pogut determinar que la recopilació de dades específiques com llistats d'immobles, preus, ubicacions i característiques generals està permès sempre que no s'infringeixin els drets de propietat intel·lectual de la plataforma, no es recopilin dades personals dels usuaris ni s'impedeixi el funcionament normal del lloc web. 

Degut a l'absència d'anàlisis anteriors específics sobre el web scraping de dades de PISOS.AD, s'ha realitzat una recerca de casos similars en altres plataformes immobiliàries per identificar quines són les dades d'interés i garantir que el nostre procés s'ajusta a les normatives legals vigents. Exemples d'anàlisis en webs similars:
* Evolució del preu de la vivenda a Andorra: [Indomio](https://www.indomio.es/mercado-inmobiliario/andorra/)
* Preu de la vivenda a Andorra per m2: [RealAdvisor](https://realadvisor.es/es/precios-viviendas/44500-andorra)
* Evolució del preu de la vivenda a Barcelona: [Idealista](https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/venta/cataluna/barcelona-provincia/barcelona/)

## INSPIRACIÓ

Tal i com s’ha introduït en el primer apartat d’aquesta memòria, l’objectiu de l’anàlisi de les dades extretes del portal pisos.ad és obtenir una visió més detallada del mercat immobiliari andorrà. 

Un dels primers objectius de l’anàlisi de les dades obtingudes és determinar la situació actual de la oferta i la demanda, i per tant, de la disponibilitat d’immobles. A part d’un primer estudi generalitzat, també es pot determinar la distribució d’oferta per parròquies, per tal d’observar si la situació és similar a totes les parròquies o hi ha més oferta i/o demanda en funció de la localització dels immobles. L’estudi de la distribució de la oferta també es pot realitzar en funció de la tipologia de la transacció, és a dir, si la propietat és de lloguer o està en venta. Degut al context actual de pujades dels tipus d’interès, i conseqüentment les comissions de les hipoteques, seria interessant contrastar si s’ha observat una disminució en la demanda d’habitatges de compra i en conseqüència un augment en la demanda de lloguers.  Finalment, seguint amb aquesta línia d’estudi, en un futur es podria repetir l’extracció i compara com ha evolucionat l’oferta immobiliària, tant per observar-ne la tendència com per determinar si aquesta es veu subjecta a estacionalitat (en el cas dels lloguers), fet molt probable degut a l’increment d’ocupació laboral i del turisme en temporada. 

Una altra dimensió rellevant que volem explorar és la distribució de preus en funció de la ubicació de l’immoble, així com de les característiques d’aquest (nombre d’habitacions, superfície, garatge...), determinant quin pes pot arribar a tenir cada característica a l’hora d’establir els preus. En cas de poder assolir aquest objectiu, es podria determinar quins immobles estan per sobre del preu que els correspondria, i quins per sota. En cas que aquest conjunt de dades i el seu estudi estigués disponible al públic general, els inversors el podrien utilitzar per cercar oportunitats de negoci, si bé aquest fet agreujaria la situació descrita a la introducció de la memòria. Per contra, aquestes dades també podrien utilitzar-se per determinar quines zones estan més tensionades i intentar buscar solucions a través de la implementació de noves legislacions addicionals a la legislació actual de congelació dels preus de lloguer o de taxació de les inversions estrangeres. 

Finalment, es pretén estudiar el nombre d’immobles publicats per cada immobiliària amb la intenció d’establir si hi ha lliure competència al sector o pel contrari aquest es troba monopolitzat. En cas que el conjunt de dades permetés determinar dos registres duplicats a través de les característiques del conjunt, però publicats per immobiliàries diferents, també es podria determinar si els preus per un mateix immoble publicat per dues immobiliàries diferents és el mateix, o si per contra, una d’elles té un preu més elevat. 

Si bé s’han realitzat estudis similars, com en l’anàlisi de RealAdvisor, considerem que l’estudi proposat aporta informació addicional, com podria ser el fet de que la propietat disposi de pàrquing, algunes de les característiques que es recullen al portal immobiliari, o tot l’estudi relacionat amb les immobiliàries que gestionen els anuncis de les propietats. 

## LLICÈNCIA
Aquest projecte està disponible sota la Llicència Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0). 

La utilització d'aquesta llicència té l'objectiu de fomentar un ús lliure, obert i transparent de les dades, així com promoure la compartició de coneixement.

Aquesta llicència permet a tercers:

* Copiar i redistribuir el material en qualsevol mitjà o format
* Adaptar, modificar i transformar el material

Per a qualsevol propòsit, inclòs comercial, sempre que es compleixin amb els següents termes:

* S'ha de reconèixer l'autoria de manera apropiada, proporcionar un enllaç a la llicència i indicant si s'han realitzat canvis al material original.
* En el cas de modificar o crear a partir del material original, s'han de distribuir sota la mateixa llicència que l'original.

Per més informació sobre la llicència visitar [Creative Commons](https://creativecommons.org/licenses/by-sa/4.0/deed.es)

