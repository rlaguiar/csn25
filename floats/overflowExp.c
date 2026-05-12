#include <stdio.h>
#include <float.h> // Para usar FLT_MAX
#include <math.h>  // Para usar isinf()

int main() {
    printf("\n--- Demonstração de Overflow de Expoente com float ---\n");

    // FLT_MAX é o maior valor que um float pode armazenar
    float max_float = FLT_MAX;

    printf("Maior float (FLT_MAX): %e\n", max_float);

    // Vamos multiplicar por 2 para exceder o limite
    float overflow = max_float * 2.0f;

    printf("FLT_MAX * 2.0 = %f\n", overflow);

    // Verificando se o resultado é infinito
    if (isinf(overflow)) {
        printf("O resultado é infinito (overflow de expoente)!\n");
    }

    return 0;
}