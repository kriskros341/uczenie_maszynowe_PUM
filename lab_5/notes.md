Szeregi czasowe (x [t]) są specyficznym rodzajem danych

inne metody i modele myślenia

szereg kumulatywny (integrative) -> różnicujemy

cykliczność/sezonowość

trędy i cykle to najważniejsze źródło informacji w takich danych

- Dane (np. xml)
- informacja (t = 13C*)
- Wiedza (na zewnątrz itd.)

WERYFIKACJA
- poprawność i spójność
- Weryfikacja merytoryczna -> sens danych, znaczenie/kontekst
- - anomalizacja
- - detekcja/klasyfikacja znanych problemów

## Weryfikacja statystyczna metodą MAD (outliery)


Żeby wiedzieć co jest nietypowe trzeba wiedzieć co jest typowe

do tego użyteczny jest histogram
-> logarytm uwidacznia anomalie

opis:
- średnia
- std
- "skewness" skośność - w którą i jak bardzo odchylone od średniej
- momenty statystyczne
- kurtoza (0 == rozkład normalny, odchylenia od niego) - uniformity?

- Kwartet Anscombe. dla par punktór (x, y)
- avg x
- avg y
- regresja
... dokończ


- mediana
- kwartyle
- precentyle
// wąsy box plot - top/bottom n%


Median Absolute Deviation
di = |xi - m|
Tm = mediana(d)
N - tolerancja (zwykle 3 ponieważ 95% wartości w rozkładzie normalnych jest pod odchyleniem 3)

di > Tm * N --> znaczy błąd

Tm -> średnia happy case, 3 -> 95% normalnej od happy case

outliery != anomalie
outliery są z poza danych które nas interesują - np. błąd rejestracji
anomalnie są wewnątrz zbioru "Żadkie" - np. wyciek

## Weryfikacja statystyczna metodą RX Reed-Xiaoli (anomalie)

maciej kowariancji

średnia ma pewne zalety nad medianą:
- szybka w liczeniu
- building block of more complex proporties
- przewidywalna

RX wychodzi poza pojedynczy punkt danych, badamy cykliczność

anomaliczne == nietypowe, nietypowe == oddalone od średniej 

timeseries -> 2d array (cykl = float[])[]
Sama odległość od średniej jest usls (ukrywa np. skierowanie)

Macierz kowariancji dla rozkładu normalnego to [[1, 0], [0, 1]]
main axis -> przesunięcie, skalowanie
other axis -> obrót

Odległość Mahalanobisa (uogólnienie odległości euklidesowej uwzględniająca macieja kowariancji) (rozkład N -> rozkład phi2)
dla większej ilości stopni swobody (wymiarów d) rozkład phi2 zaczyna przypominać normalny


Punkt jest anomalią, jeśli jego odległość Mahalanobisa > tolerancja
skąd tolerancja?? -> określamy procent szansy na anomaliczność od którego ucinamy

algorytm działa tym lepiej im lepiej dane przypominają rozkład jakiś normalny. Kontrolujemy to dostosowując tolerancję

dane wciąż muszą być jakoś jednorodne, (np. podobna powierzchnia z anomaliami)

pochodne algoryt,y
- Mixture of Gaussians (MoG)
- PCA
- Hidden Markov Models (HMM)
