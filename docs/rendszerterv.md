# Rendszerterv

## A Rendszer célja

A rendszer célja aktuális regionális időjárási adatok hozzáférésének biztosítása.
A felhasználónak lehetőséget ad bizonyos települések időjárási adatainak elmentésére.
A Weather webapplikáció célja az, hogy a felhasználók számára könnyen és gyorsan hozzáférhetővé tegye az időjárási információkat.

A webalkalmazás lehetővé teszi a felhasználók számára, hogy egyszerűen megkeressék a kívánt helyszínt a kereső funkció használatával, és biztosítja az időjárási adatok megjelenítését kártyák formájában.
Az első kártya kiemelt módon mutatja be az aktuális hőmérsékletet, míg a további kártya grafikusan ábrázolja a többi nap előrejelzését, segítve a felhasználókat a jövőbeli időjárás megértésében.

A webalkalmazás fókuszában a felhasználói élmény és az egyszerűség áll, így mindenki könnyedén
használhatja bármely platformon, legyen az számítógép, tablet vagy telefon.
Az ingyenes elérhetőség lehetővé teszi bárki számára, hogy naprakész időjárási adatokhoz jusson.
A webalkalmazás kártya alapú megjelenítésével a felhasználók gyorsan és könnyen áttekinthetik az időjárási információkat.

Előző alkalmazásunkkal összehasonlítva ez az alkalmazás egy TensorFlow megtanított modellt használ,
amely a jövőbeli időjárást is képes előre jelezni anélkül, hogy szükség lenne felállított időjáráselőrejlző
rendszerekre. A modell 120 évvel ezelőtti mindennapos időjárásadatokat tanult meg, és ezek alapján jelzi
előre a jövőbeli időjárást.

A rendszer célja aktuális regionális időjárási adatok hozzáférésének biztosítása
TensorFlow-ban implementált AI modell segítségével.
A felhasználónak lehetőséget ad bizonyos települések időjárási adatainak elmentésére.
A Weather webapplikáció célja az, hogy a felhasználók számára könnyen és gyorsan
hozzáférhetővé tegye az időjárási információkat.

A webalkalmazás lehetővé teszi a felhasználók számára, hogy egyszerűen megkeressék
a kívánt helyszínt a kereső funkció használatával, és biztosítja az időjárási adatok
megjelenítését kártyák formájában. Az első kártya a választható városokat tartalmazza.
Ezekre kattintva megnyílit az adott városnak specifikus oldal, ahol a következő kártyák jelennek meg:

- Holnapra jósolt adatok
- Jelenlegi naptól 7 napra eső napra jósolt adatok
- Jelenlegi naptól 30 napra eső napra jósolt adatok
- Jelenlegi naptól 365 napra eső napra jósolt adatok
- Részletes szűrés

A részletes szűrés kártyán a felhasználó rászűrhet a neki szükséges dátumra jósolt időjárási
adatokra egy külön oldalon.

A webalkalmazás fókuszában a felhasználói élmény és az egyszerűség áll, így mindenki
könnyedén használhatja bármely platformon, legyen az számítógép, tablet vagy telefon.
Az ingyenes elérhetőség lehetővé teszi bárki számára, hogy naprakész időjárási adatokhoz jusson.
A webalkalmazás kártya alapú megjelenítésével a felhasználók gyorsan és könnyen
áttekinthetik az időjárási információkat.

## Projektterv

### Projekt szerepkörök

| Név           |     Szerepkör      |                        Feladat |
|:--------------|:------------------:|-------------------------------:|
| Baráth Simon  | Software Engineer  |                     AI/Backend |
| Brázda Martin | Software Engineer  |                Backend/Teszter |
| Deák Erik     | Software Engineer  |                Frontend Stílus |
| Gyenes Balázs | Frontend developer | Frontend logika implementálása |

## Ütemterv

- Projekt kezdet: **2023. október**
- Követelményspecifikáció megfogalmazása: **2023. október**
- Funkcionális specifikáció megfogalmazása: **2023. október**
- Rendszerterv megfogalmazása: **2023. október**
- HTML és hozzá tartozó stíluslap elkészítése: TBA
- Frontend vezérlő elkészítése: TBA
- TensorFlow modell elkészítése: **2023. opktóber 26.**
- Endpointok létrehozása: TBA
- Backend - Frontend kommunikáció implementálása: TBA

| Funkció      | Feladat            | Prioritás | Becslés (h:mm) | Eltelt idő (h:mm) | Hátralévő idő (h:mm) |
|:-------------|:-------------------|:---------:|:--------------:|:-----------------:|:--------------------:|
| KövSpec      |                    |     6     |      2:00      |       2:00        |         0:00         |
| FunkSpec     |                    |     6     |      2:00      |       2:00        |         0:00         |
| Rendszerterv |                    |     6     |      2:00      |       1:00        |         1:00         |
| WebApp       | Frontend stílus    |     5     |      2:00      |       0:00        |         2:00         |
|              | Frontend vezérlés  |     5     |     10:00      |       0:00        |        10:00         |
|              | Frontend tesztelés |     5     |      2:00      |       0:00        |         2:00         |
| API          | Adatok beolvasása  |     3     |      4:00      |       0:00        |         4:00         |
| Backend      | TensorFlow modell  |     0     |     20:00      |       10:00       |        10:00         |
|              | Adatok elérése     |     2     |      8:00      |       0:00        |         8:00         |
|              | Backend tesztelés  |     2     |      5:00      |       0:00        |         5:00         |

## Mérfölkövek

1. Projekt kezdete - **_2023. október 9._**
2. Követelményspecifikáció megírása - **_2023. október 10._**
3. Funkcionális specifikiáció megírása - **_2023. október 19._**

## Üzleti folyamatok modellje

### Üzleti szereplők

1. Felhasználó: Az alacsony jogosultágokkal rendelkező felhasználó, aki használja az alkalmazást az időjárás lekérdezéséhez.
2. Adminisztrátor: Adminisztrátorok magasabb jogosultsági szinttel rendelkező felhasználók az alábbi feladatok ellátása végett:

   - Problémák kezelése: Jelenlegi problémák, panaszok, visszajelzések kezelése.
   - Renszerkarbantartás: Biztonsági mentések rendeltetés szerű készítése, a rendszer teljesítményének optimalizálása.
   - Kommunikáció: Rendszeres kommunikálás a felhasználókkal: válasz felhasználók kéréseire, kérdéseire.

### Üzleti folyamatok

0. **Backend API betaníttatása**: A háttéralkalmazás felkészítése a meglévő városok időjárásának
lekérdezésére.
   - _Input_: Adatbázis az elmúlt 120 év időjárásadataiból
   - _Output_: nincs
   - _Szereplők_: TensorFlow API

1. **Város Lekérdezése:** Adott város időjárási adatainak lekérdezése.
Az eseményt az alkalmazás felhasználói felülete indítja.

   - _Input_: Felhasználói input
   - _Output_: Lekérdezni kívánt város időjárási adatai előrejósolva
   - _Szereplők_: Felhasználó

2. **Város input elküldése**: A felhasználó által küldött városnak a backend felé történő elküldése.
Az eseményt az alkalmazás felhasználói felülete indítja.

   - _Input_: Felhasználói input
   - _Output_: Város input elküldve a backend felé
   - _Szereplők_: Felhasználó, frontend

3. **Város input feldolgozása**: A backend TensorFlow API által feldolgozott adatok lekérdezése a kívánt
időszakra vonatkozólag.

    - _Input_: Város input
    - _Output_: Város időjárásának előrejelzése
    - _Szereplők_: Backend

4. **Város időjárásának továbbküldése**: A backend továbbküldi a frontend felé a frontend által lekért
és backend által feldolgozott adatokat.

    - _Input_: Város időjárásának előrejelzése
    - _Output_: Város időjárásának továbbküldése
    - _Szereplők_: Backend, frontend

5. **Megkapott város időjárásának feldolgozása**: A frontend a backendtől kapott adatokat
feldolgozza és felhasználó által feldolgozható formátumban megjelenítik.

    - _Input_: Város időjárásának továbbküldése
    - _Output_: Város időjárásának megjelenítése
    - _Szereplők_: Frontend