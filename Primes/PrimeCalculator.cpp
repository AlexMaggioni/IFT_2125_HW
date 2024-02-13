#include "PrimeCalculator.h"
#include <iostream>
#include <vector>
#include <cmath> // Use <cmath> instead of <math.h> for C++

// This file contains the definitions of the methods of the PrimeCalculator class

PrimeCalculator::PrimeCalculator() {
    // Constructor implementation (if needed)
}

int PrimeCalculator::CalculateNthPrime(int N) {
    if (N < 1) return -1;
    if (N == 1) return 2; 

    // For small N, use a predefined limit to ensure accuracy and efficiency.
    int limit;
    if (N < 6) {
        limit = 15;
    } else {
        limit = static_cast<int>(N * std::log(N) + N * std::log(std::log(N)));
    }

    std::vector<bool> prime(limit + 1, true);
    prime[0] = prime[1] = false; 

    for (int p = 2; p * p <= limit; ++p) {
        if (prime[p]) {
            for (int i = p * p; i <= limit; i += p) {
                prime[i] = false;
            }
        }
    }

    int primeCount = 0;
    for (int p = 2; p <= limit; p++) {
        if (prime[p]) {
            ++primeCount;
            if (primeCount == N) {
                return p; 
            }
        }
    }

    return -1;
}