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

## Projektterv

### Projekt szerepkörök

| Név           |     Szerepkör      |                        Feladat |
| :------------ | :----------------: | -----------------------------: |
| Baráth Simon  | Software Engineer  |                            N/A |
| Brázda Martin | Software Engineer  |                            N/A |
| Deák Erik     | Software Engineer  |                            N/A |
| Gyenes Balázs | Frontend developer | Frontend logika implementálása |

## Ütemterv

- Projekt kezdet: **2023. október**
- HTML és hozzá tartozó stíluslap elkészítése: TBA
- Frontend vezérlő elkészítése: TBA
- TensorFlow modell elkészítése: TBA
- Endpointok létrehozása: TBA
- Backend - Frontend kommunikáció implementálása: TBA

| Funkció      | Feladat            | Prioritás | Becslés (h:mm) | Eltelt idő (h:mm) | Hátralévő idő (h:mm) |
| :----------- | :----------------- | :-------: | :------------: | :---------------: | :------------------: |
| KövSpec      |                    |     6     |      2:00      |       2:00        |         0:00         |
| FunkSpec     |                    |     6     |      2:00      |       2:00        |         0:00         |
| Rendszerterv |                    |     6     |      2:00      |       1:00        |         1:00         |
| WebApp       | Frontend stílus    |     5     |      2:00      |       0:00        |         2:00         |
|              | Frontend vezérlés  |     5     |     10:00      |       0:00        |        10:00         |
|              | Frontend tesztelés |     5     |      2:00      |       0:00        |         2:00         |
| API          | Adatok beolvasása  |     3     |      4:00      |       0:00        |         4:00         |
| Backend      | TensorFlow modell  |     0     |     20:00      |       0:00        |        20:00         |
|              | Adatok lementése   |     2     |      3:00      |       0:00        |         3:00         |
|              | Backend tesztelés  |     2     |      5:00      |       0:00        |         5:00         |
