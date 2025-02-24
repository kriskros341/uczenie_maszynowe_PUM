# Kasyfikacja II
## KNN, SVM, RF, MLP (ANN)

Klasyfikatory - Porównanie, problem ekstrakcji cech
sklearn pipeline

PCA ustala kierunki największej wariancji i standaryzuje dane. Nie powinno być łączone z standaryzacją.

Standaryzacja przeważnie redundantna z pca, chyba że pomiędzy nimi wystepują jakieś kroki. ex. outlier analysis i czasem do wizualizacji jest lepszy efekt.

celem klasyfikacji jest określenie granic cech

## KNN <3

## SVC - Support vector machines
Poszukuje optymalnej (hiper)płaszczyzny rozdzielającej zbiór. Minimalizacja marginesu

miękki margines - Szerszy margines za tolerowane błędy (Dla zachodzących zbiorów)

kernel trick - Czasem nie da się sklasyfikować liniowo w liniowej przestrzeni, wtedy warto rozważyć coś w stylu x->x^2

RBF - kernel trick który dostosowuje się do danych (bardzo wrażliwe na próbkowanie, outliery)

## Drzewa decyzyjne
### Podstawa wielu lepszych klasyfikatorów

łatwe do zastosowania

Heurystyczne - Wrażliwe na przetrenowanie
Nie są aplikowalne do wszystkich problemów

Random forest 

- Wiele drzew uczonych na podzbiorze danych i podzbiorze atrybutów, ich konsensus określa przynależność do klasy


## Sieci neurownowe

Wartość neuronu to iloczyn skalarny wejść i wag, włożone w funkcję nieliniową

parametr: funkcja_nieliniowa funkcja do przeliczania wag

parametr: n_warstw

parametr: learning_rate - Jak wrażliwa będzie na zmiany

parametr: liczba_epok - Jak długo ta sieć będzie się uczyć

optimizer
    - parametr: batch size



Test statystyczny jest narzędziem weryfikacji.
Jaka jest szansa że wynik jaki mamy jest przypadkowym układem a jaka że jest konsekwentnym rezultatem

3 testy statystyczne które można wykorzystać. (dobry start do dalszego zgłębiania tematu)

### powiedzmy że mamy

C1 o skutecznościach s1: float[]

C2 o skutecznościach s2: float[]

Hipoteza_0: Klasyfikatory mają identyczną skuteczność
Hipoteza_alternatywna: Klasyfikatory mają różną skuteczność

avg(s1) === avg(s2) ?

Dobór testów:
- Czy różnice mają rozkład normalny? -> Shapiro-Wilk

(H0: Czy zestaw danych został wygenerowany z rozkładu normalnego?) -> p_value: jaka jest szansa że jednak przypadek? 00.1 - 1% szans że się pomyliliśmy

Testy normalności są wrażliwe na ilość danych (No mają pewne ograniczenia które należy rozważyć)

w zależności od rezultatu, dalej sprawdzamy albo

H0 przyjęta -> test wilcoxon

albo

H0 odrzucona -> t-test dla par

Te testy istnieją w wariantach jedno (przewaga jednego nad drugim) i dwu stronnych (równość)


## Przekształcanie sygnału:

### transformaty
- fouriera
- falkowa

### fouriera

goto mechanizmy do ekstrakcji cech

Reprezentacja sygnału

przenoszenie do innych domen (Kernel trick?)

xn -> cos(xn a), sin(xn a) -> e^(i n a)

gdzie a jest próbkowane po okręgu

jakiś sposób na określenie najważniejszych cech

REDUKCJA SZUMU

Niewrażliwa na przesunięcia

## falkowa

np. Harra

### dekompozycja sygnału
- PCA
- LDA




