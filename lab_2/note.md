# data mining laboratory
dimmentional reduction - np PCA - zmniejszenie wymiarów danych
clustering, example KMeans

TSNE to alt dla PCA, w którym pozycja nie ma żadnego znaczenia, liczą się tylko odległości punktów danych
TSNE takes a long time to parse, so it is a good idea to reduce dimmention count with pca before doing tsne
It is a good idea to cache TSNE results. Należy jednak pamiętać że 

### zbyt pochopna optymalizacja jest źródłem każdego zła

## różnice tsne pca
PCA - liniowy - możemy nowy zestaw danych i przemielić przez pca - wytrenować
TSNe - nieliniowy/nieodwracalny - nie możemy wytrenować. Nowe dane mają się się ni jak do poprzednich danych (bardziej wykorzystywany pod wizualizacje)

---

try except > if (). mechanisms like caching are best encapsulated behind a class

---

datamining combo:

PCA -> KMEANS

PCA -> TSNE -> hierarchiczne

---

## grupowanie hierarchiczne

rodzaje grupowania hierarchicznego.
- Single - closest
- Complete - fuhrest
- Other -  average, etc.

trochę inaczej grupuje (nie jest ograniczone sferowością kmeans)

izolowane punkty mogą łatwo zaburzyć grupowanie. Hierarchiczne radzi sobie z tym dobrze

---

## Klasteryzacja:

- Kmeans
- AgglomerativeClustering
- DBSCAN

te trzy sprawdzają się w 90% przypadków