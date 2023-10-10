# Tensorflow alapú időjárás alkalmazás követelmény specifikáció

### Jelenlegi státusz:
Rohanó információéhes világunk óhatatlanul vágyik arra, hogy a környező történésekről mindent - és ezalatt értsd:
MINDENT - tudnia kell a benne élő embereknek. A mi alkalmazásunk ebben segít és szükséges információkat közöl az
egyénnek, melyek nélkülözhetetlenek ahhoz, hogy ki tudja tenni a lábát a házból úgy, hogy soha nem érik meglepetések, ha
időjárásról van szó. Megannyi baleset történik a világban az időjárás miatt, hiszen az anyatermészetet nem tudjuk
becsapni, de tudunk hozzá alkalmazkodni. Évente többezren halnak meg egy egyszerű megfázásban, ezt pedig nem
megengedhető. Ha egy vastagabb kabát választ el az életünk megszűnésétől, akkor inkább válasszuk a kabátot, mintsem a
halált. Tehát az alkalmazásunk nem más mint egy időjárás monitoring alkalmazás. Különböző városok időjárásának
megfigyelésére alkalmas. Jelen és jövőbeli időjárás megfigyelése. Az időjárásmegjelenítés tartalmazza a hőmérséklet,
szél és egyéb időjárással kapcsolatos státusz megosztását / megjelenítését. Csak meg kell nyitnia alkalmazásunkat,
beírni az Ön városát és máris öltözködhet az igényei szerint!

> „Ahogyan a kód mindig fejlődik, úgy fejlődik benned is a tudás és a szakértelmesség. Legyél az innováció
> mestere, és hagyd, hogy a fejlődés szárnyakat adjon álmaidnak a programozás végtelen univerzumában!”
> -- <cite>ChatGPT 3.5</cite>

Előző alkalmazásunkban a felhasználók egy különböző elemekből felépített felületet láthattak, melyen
dinamikusan jelenítettük meg az időjárást. A felhasználó egy keresősáv segítségével kereshetett a különböző
települések között. A keresés gomb lenyomásával az alkalmazás kiírta a felületre a hőmérsékletet, a település
nevét, a százalékos páratartalmat és a szél sebességét. Az alkalmazás tartalmazta az időjárásolvasáshoz
szükséges összes adatot. Ez egy szép és jó elképzelés volt, azonban mi többet akartunk. Elhatároztuk, hogy
megalkotjuk a világ legjobb időjárás alkalmazását. Az új alkalmazásunkban a felhasználók egy szép, igényes
felületen, továbbra is megkapják az időjárás adatait. Azonban az új alkalmazásunkban a felhasználók egy
általunk készített háttéralkalmazással képesek az adatok megszerzésére, mely nem igényel külön
alkalmazást, pusztán meglévő történelmi adatokkal dolgozva jelenítjük meg az előrelátható időjárást. Tény,
hogy az időjárás előrejelzés nem mindig pontos, azonban mi ezt megoldottuk. Az alkalmazásunkban a
„TensorFlow” nevű Python alapú nyílt forráskódú szoftverkönyvtárat használjuk, melyet a Google Brain
csapata fejlesztett ki. A TensorFlow egy gépi tanulási keretrendszer, amelyet a Google a neurális hálózatok és
a mély tanulás kifejlesztésére használ. A megoldásunkkal fölöslegessé válnak különböző időjárásmérő
eszközök, hiszen alkalmazásunk anélkül is már többtíz évvel ezelőtti adatokból dolgozik.


### Vágyálom rendszer:
Célunk ügyfeleink naprakész, percre pontos információk szerzése a jelenlegi időjárásról annak céljából, hogy ne érhessék
meglepetések utazás, kirándulás esetében, hogy tudják, mikor hogyan kell öltözködniük és mit kell magukkal vinniük az
utazásokra. Az alkalmazásnak könnyen üzemeltethetőnek kell lennie. Az online megjelenítésnek lehetőleg reszponzívnak
kell lennie, hogy mobil / tablet illetve számítógép eszközökön is szépen, jól láthatóan megjelenített legyen. Elvárt a
platformfüggetlenség, nem elfogadható, ha csak egy operációs rendszeren futtatható az alkalmazás. Elvárt, hogy az alkalmazás a felhasználók által megadott
településre vonatkozóan megjelenítse az aktuális időjárási adatokat, valamint az előrejelzést. Az
alkalmazásnak folyamatosan tudnia kell kommunikálni a meglévő adatbázissal, hogy a felhasználók a lehető
legpontosabb adatokat kapják meg. Nem elfogadható, ha az alkalmazás nem pontos adatot közöl a
felhasználókkal.

#### További vágyálmok:

- Engedélyezni a felhasználoknak, hogy beállítsák az időjárási riasztásokat, például eső vagy hó előrejelzés
esetén. Ez segíthet nekik felkészülni az időjárás változásaira.

- A kártyákon kívül engedélyezni a felhasználóknak, hogy kattintsanak a napi időjárási részletekre, és
lássák a részletes időjárási előrejelzést, például a páratartalmat, a napnyugtát és a napkelte idejét.

- Adatokat szolgáltathatunk a légköri viszonyokról, például a légszennyezettségi szintekről vagy a
pollenkoncentrációról, amelyek hasznosak lehetnek az allergiásoknak és az egészségüket figyelő
felhasználóknak.

- Időjárási térképek: térképek feltöltése az alkalmazásba, amelyeken megjelenik a radar és a
hőmérsékleti térkép. Ezen térképek segítségével a felhasználók könnyen áttekinthetik az időjárási
körülményeket.

- Engedélyezés a felhasználóknak, hogy megosszák az időjárási információkat közösségi média
platformokon, így további felhasználókat vonzhatnak  az alkalmazáshoz.

- Felhasználói visszajelzés és értékelések kérése a felhasználóktól, hogy folyamatosan fejlesztő legyen az
alkalmazás és jobb élményt nyújthassunk.

- Offline használat biztosítása, hogy a felhasználók hozzáférhessenek az időjárási információkhoz,
amikor nincs internetkapcsolatuk.

- Élő háttérképek az időjárási körülményeknek megfelelően, így az alkalmazás vizuálisan is érdekes
legyen.

- Widgeteket fejlesztése, amelyek lehetővé teszik az időjárás információinak gyors megtekintését a
felhasználók kezdőképernyőjén.


### Jelenlegi üzleti folyamatok:

#### App indítása:
A felhasználó elé táruljon egy szép, igényes felület, melyen lehetősége van beírni az általa választott várost illetve
települést.

#### Widgetek:
A felhasználó egy különböző elemekből felépített felületet lásson, melyen dinamikusan megjelenik az aktuális település
időjárása.

#### Szükséges időjárásadatok közlése:
Az alkalmazás tartalmazza az időjárásolvasáshoz szükséges összes adatot például: hőmérséklet, település neve, százalékos
páratartalom valamint a szél sebessége

#### Felhasználói interakciók feldolgozásáért felelős információinput
Szükséges az alkalmazásnak tartalmaznia egy keresősávot, valamint a keresősávhoz egy megfelelő "Keresés" gombot.

#### Információbecslés, avagy "Könnyített Mód"
Az információ feldolgozását meg kell próbálni megtippelni, amennyiben a felhasználó félreírja a számára igényelt
település megnevezését!

#### A keresőgomb működése
A keresésgomb lenyomásakor az alkalmazás kiírja a felületre a fent említett adatokat.

### Követelménylista:

| **ID** | **Név** | **Kifejtés** |
|--------|---------|--------------|
| K1 | Felhasználói interfész | Az alkalmazásnak egy felhasználóbarát felülettel kell rendelkeznie. |
| K2 | Helyszínválasztás      | A helyszínválasztásnak lehetővé kell tennie a felhasználók számára, hogy kereső opció segítségével gyorsan megtalálhassák a választott helyszínt/várost. |
| K3 | Időjárásinformációk    | Az időjárásinformációknak pontosnak és naprakésznek kell lenniük, hogy a felhasználók megbízható adatokhoz jussanak. |
| K4 | Aktuális hőmérséklet   | Az aktuális hőmérsékletnek kiemelten kell megjelennie. |
| K5 | Előrejelzés            | Az előrejelzésnek öt napos időtávot kell lefednie és grafikus formában kell bemutatnia az időjárás változásait. |
| K6 | Mobilkompatibilitás    | A reszponzív designnak biztosítania kell, hogy az alkalmazás megfelelően műdjön mobiltelefonokon és tableteken is. |
| K7 | Adatforrás             | Az időjárásinformációk lekérdezését egy külső weather API használatával kell megvalósítani. |