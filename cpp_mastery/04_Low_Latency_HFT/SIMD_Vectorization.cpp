/**
 * Topic: SIMD Vectorization (AVX Intrinsics)
 */
#include <iostream>
#include <immintrin.h>
#include <vector>

void add_vectors_avx(const float* a, const float* b, float* res, size_t n) {
    for (size_t i = 0; i < n; i += 8) {
        __m256 va = _mm256_loadu_ps(a + i);
        __m256 vb = _mm256_loadu_ps(b + i);
        __m256 vr = _mm256_add_ps(va, vb);
        _mm256_storeu_ps(res + i, vr);
    }
}

int main() {
    const int n = 16;
    alignas(32) float a[n], b[n], res[n];
    for (int i = 0; i < n; ++i) {
        a[i] = i;
        b[i] = i * 2;
    }

    add_vectors_avx(a, b, res, n);

    for (int i = 0; i < n; ++i) {
        std::cout << res[i] << " ";
    }
    std::cout << "\n";
    return 0;
}


























































































































