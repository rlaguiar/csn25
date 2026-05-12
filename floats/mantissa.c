#include <stdio.h>

int main() {
    printf("--- Demonstração de Perda de Precisão (Mantissa) com float ---\n");

    // Um número grande com bastante precisão inicial
    float grande = 16777216.0f;
    // Um número muito pequeno
    float pequeno = 0.5f;

    // A representação em binário de 16777216.0f é 2^24.
    // A mantissa de um float tem 23 bits explícitos (+1 implícito),
    // então este é o limite onde a precisão começa a se degradar.
    float resultado1 = grande + pequeno;

    printf("Número grande:           %.7f\n", grande);
    printf("Número pequeno:          %.7f\n", pequeno);
    printf("grande + pequeno =       %.7f  <-- O valor 'pequeno' foi perdido!\n\n", resultado1);

    // Vamos tentar com um número um pouco menor que o limite
    float quase_no_limite = 16777215.0f;
    float resultado2 = quase_no_limite + pequeno;
    printf("Quase no limite:         %.7f\n", quase_no_limite);
    printf("quase_no_limite + 0.5 =  %.7f  <-- Aqui a soma ainda funciona.\n", resultado2);


    return 0;
}