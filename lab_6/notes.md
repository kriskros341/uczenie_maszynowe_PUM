## sieci neuronowe - podstawy

nieliniowa funkcja ReLU, np. f(x) = max(x, 0)

Dlaczego nieliniowość?

max(0, x) dobrze usunie przesunięcie w danych oraz ich ograniczenie - w jakimś obszarze generuj dane, w jakimś nie [piecewise]

poszczególne neurony mogą wtedy odpowiadać za różne części zbioru danych

### model

schemat połączeń neuronów (warstwy i wagi)

MLP multi layer perceptron

windowing of time series is useful to limit data

Zadanie:

Sygnał -> [trening, test]
3 pliki

6:2:2
train, validate, test
miara błędu RMSE

Przetrenować sieć
