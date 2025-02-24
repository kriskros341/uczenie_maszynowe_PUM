# Konkurs

Klasyfikatory:
- VMC
- random forest 
- naive bayes

Zadanie z klasyfikacji

    Zostaliśmy rozniesieni i ja nie wiem nawet o czym mówią jak tłumaczą zadania ; . ; 

    Am i really the problem or is it that my peers have preexisting knowledge. Guess I will need to redo this one.

    Pod koniec zajęć okazało się, że trenowałem na danych normalizowanych a oceniałem na nienormalizowanych
    Realny wynik to nie 38% tylko 80%. Czuję się z tym lepiej.

# Ocena klasyfikatorów

1. accuracy (mało ciekawe) nie wiemy jakie błędy popełniamy | koszty błędów mogą być różne
False positive (typ I) i False negative (typ II) są różnie ważne


2. (Precision, recall) - easy, wywodzi się z baz danych
https://en.wikipedia.org/wiki/Precision_and_recall
3. (Sensitivity, specificity) - wywodzi się z medycyny
https://en.wikipedia.org/wiki/Sensitivity_and_specificity 
    
    F1: 2 * P * R / (P + R) -> Pesymistyczne uśrednienie do jednej wartości


4. R. O. C. - receiver operator characteristic
- Co jeśli mamy porównać metody ale one mają parametr
When True positive overlaps with true negative for some parameter values
(for value 20, 80% is +, 20% is -)

Wykres parametryczny
y: TP + FN
x: TN / (TN + FP)
krzywa charakterystyki operatora
miarą sprawności jest pole pod krzywą

# OVERTRAINING

Gdy model uczy się pod dane nie pod pattern

- Nie ucz na tym samym zbiorze danych!
- Podziel na część treningową i testową?
- - spoko, tracimy potencjalnie dużą część zbioru treningowego. Dobre dla sieci głębokiego uczenia tho!
- test on 1 sample at time? Leave one out cross validation LOOCV
- - zajmie długo
- - Zwiększona wariancja wyniku
- GOLD STANDARD: K-fold CV
- - dzieli na N części
- - LOOCV na częściach.

i to wszystko działa super jeśli klasyfikator nie ma hiperparametrów

# HIPER PARAMETRY
- Hiper parametrem sieci neuronowej jest ilość warstw (My ustawiamy)
- Parametry sieci neuronowej to wagi (Rezultat optymalizacji)

Jak dobrać hiper parametry (przykład KNN(K))?

KFOLD
pierwszy podział jako referencyjny, sprawdzamy na 2-5

Drugi podział dla następnych K, sprawdzamy na 3-5

grid_search_cv
cross_val_score

najlepszy sposób sprawdzania efektywności klasyfikatorów, ale wymaga dużo kalkulacji i się nie sprawdzi dla Neural network

# Standaryzacja i stratyfikacja

stratified to taki podział na foldy, który stara się utrzymać równy podział klas w każdym foldzie 
( W absolutnej większości sytuacji korzystamy z stratified CV )

Standaryzacja sprowadza wszystkie zakresy do 0..1 (NIEMAL ZAWSZE WSKAZANE)