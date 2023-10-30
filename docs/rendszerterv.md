# Rendszerterv

## A Rendszer célja

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
