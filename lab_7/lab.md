# Krzywa strat

- pca bardzo utrudnia pracę mlp

# Kluczowe parametry
### 0: iteracje i epoki

iteracja to iteracja

Epoka to przejście przez cały zbiór treningowy

they are not the same

# 1: learning rate

Learning rate może zostać dobrany na podstawie loss-curve.
Większy learning rate na start i w dół?

# 2: batch size

batch size, większy wymaga więcej zasobów. Zbyt mały batch size zwiększa oscylacje
jego wartość trzeba dopasować do zbioru danych


# 3: Optimizer

sterowanie procesem uczenia
SGD (gradient descent), ADAM (szybszy mniej precyzyjny SGD)

# Funkcja nieliniowa

- Sigmoid/logistic

- Tanh

Mało reagują na outliery

- ReLu

Prosta szybka

Może powodować martwe neurony

### Generalnie zaczynamy od relu

tensor to dnarray pytorcha

STANDARYZACJA JEST JEDYNĄ RZECZĄ JAKĄ ROBIMY PRZED WŁOŻENIEM ICH DO NN

# uczenie

# douczanie - do istniejącego robimy dodatkowe iteracje

dataset opakowuje zbiór danych

lossy regresyjne:

l1loss - mean abosulte error
MSELoss - mean square error

do klasyfikacji potrzebujemy loss functon który kara nie tylko za złe predykcje ale też za niezdecydowanie:

softmax - normalizacja do 0/1 i do sumy 1 (taki jakby rozkład prawdopodobnieństwa)

nll - negative log likelyhood dobrze współgra z softmax (patrz wzór logarytmu). - Gdy chcemy by tylko jedna z klas miała wysoką wartość



