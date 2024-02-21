//Alex Maggioni, 20266243
//Canelle Wagner, 20232321

#include "PrimeCalculator.h" 
#include <iostream> 
#include <vector> 
#include <cmath> 

// Définition du constructeur de la classe PrimeCalculator.
PrimeCalculator::PrimeCalculator() {
}

int PrimeCalculator::CalculateNthPrime(int N) {
    
    // Si N est inférieur à 1, cela n'a pas de sens, donc on retourne -1 comme valeur d'erreur.
    if (N < 1) return -1;
    // Le premier nombre premier est 2, donc si N est 1, on retourne directement 2.
    if (N == 1) return 2;

    // Définition de la limite du crible.
    int limit;
    // Si N est inférieur à 6, on utilise une limite fixe de 15 pour éviter les erreurs de sous-estimation.
    if (N < 6) {
        limit = 15;
    } else {
        // Pour N >= 6, on calcule la limite en se basant sur l'approximation du N-ième nombre premier.
        limit = static_cast<int>(N * std::log(N) + N * std::log(std::log(N)));
    }

    // Création d'un vecteur de booléens, initialisé à true, pour marquer les nombres premiers.
    std::vector<bool> prime(limit + 1, true);
    // 0 et 1 ne sont pas des nombres premiers, donc on les marque comme false.
    prime[0] = prime[1] = false;

    // Crible d'Ératosthène: itération sur les nombres pour marquer les multiples comme non-premiers.
    for (int p = 2; p * p <= limit; ++p) {
        if (prime[p]) {
            for (int i = p * p; i <= limit; i += p) {
                prime[i] = false;
            }
        }
    }

    // Comptage et identification du N-ième nombre premier.
    int primeCount = 0;
    for (int p = 2; p <= limit; p++) {
        if (prime[p]) {
            ++primeCount;
            if (primeCount == N) {
                return p; // Retourne le N-ième nombre premier trouvé.
            }
        }
    }

    // Si on n'a pas trouvé le N-ième nombre premier dans la limite calculée, on retourne -1.
    return -1;
}
