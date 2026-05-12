#include <stdio.h>
#include <float.h> // Para usar FLT_MIN

int main() {
    printf("\n--- Demonstração de Underflow de Expoente com float ---\n");

    // FLT_MIN é o menor valor positivo normalizado que um float pode representar
    float min_float = FLT_MIN;
    printf("Menor float (FLT_MIN): %e\n\n", min_float);

    printf("Dividindo sucessivamente por 2...\n");
    for (int i = 0; i < 50; ++i) {
        min_float = min_float / 2.0f;
        printf("Passo %2d: %.50f\n", i + 1, min_float);
        if (min_float == 0.0f) {
            printf("O resultado virou zero (underflow de expoente)!\n");
            break;
        }
    }

    return 0;
}