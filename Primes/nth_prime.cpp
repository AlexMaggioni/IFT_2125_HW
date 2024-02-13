// CE FICHIER NE SERT QU'A APPELER ET TESTER VOTRE CODE. 
// VOUS NE DEVRIEZ PAS AVOIR BESOIN DE LE MODIFIER, SAUF POUR 
// AJOUTER VOUS-MÊME D'AUTRES TESTS SI VOUS LE VOULEZ.
// NE PAS REMETTRE SUR STUDIUM. REMETTEZ SEULEMENT PrimeCalculator.cpp/.h

// THIS FILE IS ONLY USED TO CALL AND TEST YOUR CODE.
// YOU SHOULD NOT HAVE TO MODIFY IT, EXCEPT FOR ADDING 
// NEW CUSTOM TESTS IF YOU WISH TO DO SO.
// DO NOT SUBMIT ON STUDIUM. ONLY SUBMIT PrimeCalculator.cpp/.h


#include <iostream> // pour l'affichage dans la console // for display in console
#include "PrimeCalculator.h" // pour la classe principale de l'exercice // for the main class of the exercise
#include <vector> // pour utiliser les vecteurs de la librairie standard // to use vectors from the standard library
#include <cstdlib> // pour convertir le input en int // to convert input to int

// commandes / command (PowerShell) :
// g++ -o nth_prime.exe nth_prime.cpp PrimeCalculator.cpp
// .\nth_prime.exe 100

// for VS Code, make sure to compile all the files of the project
// you might want to change "${file}", by "${fileDirname}\\**.cpp" in the tasks.json of .vscode -> taks -> args
// pour VS Code, veillez à compiler tous les fichiers du projet
// vous souhaiterez peut-être remplacer "${file}", par "${fileDirname}\\**.cpp" dans le fichier task.json de .vscode -> taks -> args

// Calculateur de nombres premiers / Prime Calculator
// Le / The 100e nombre premier est / th prime nomber is : 541
// Tests reussis / Tests passed !

bool TestPrimeCalculator();

int main(int argc, char *argv[])
{
    std::cout << "Calculateur de nombres premiers / Prime Calculator" << std::endl;

    int N = 10000;
    if (argc >= 2){
        N = atoi(argv[1]);
        if (N == 0){
            std::cout << "Erreur d'entree / input error" << std::endl;
            N = 10000;
        }
        
    }

    PrimeCalculator Calculator = PrimeCalculator();
    int NthPrime = Calculator.CalculateNthPrime(N);

    std::cout << "Le / The " << N << "e nombre premier est / th prime nomber is : ";
    std::cout << NthPrime << std::endl;

    // tests
    if (TestPrimeCalculator()){
        std::cout << "Tests reussis / Tests passed !" << std::endl;
    } else {
        std::cout << "Tests echoues / Failed tests :(" << std::endl;
    }

}

bool TestPrimeCalculator(){
    std::vector<int> PrimesPositions = {1,3,260,1000,10000};
    std::vector<int> PrimesNumbers = {2,5,1657,7919,104729};
    PrimeCalculator Calculator = PrimeCalculator();

    for (int Idx = 0; Idx < PrimesPositions.size(); Idx++){
        if (Calculator.CalculateNthPrime(PrimesPositions[Idx]) != PrimesNumbers[Idx]){
             std::cout << "Test echoue / Failed test : " << PrimesPositions[Idx] << " devrait donner / should give " << PrimesNumbers[Idx] << std::endl;
            return false;
        }
    }

    return true;
}
// Note :
// Le 1000000e nombre premier est : 15485863
// Cela devrait prendre un temps max de 5-10 secondes environ (dépendamment de votre machine), si l'algorithme est efficace.

// The 1000000th prime number is : 15485863
// This should take a maximum time of around 5-10 seconds (depending on your machine), if the algorithm is efficient.