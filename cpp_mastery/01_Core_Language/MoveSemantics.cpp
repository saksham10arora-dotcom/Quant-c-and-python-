/**
 * Topic: Move Semantics & Rvalue References
 */
#include <iostream>
#include <vector>
#include <string>

class MemoryBuffer {
    double* data_;
    size_t size_;
public:
    MemoryBuffer(size_t n) : size_(n), data_(new double[n]) {
        std::cout << "Allocated " << n << " doubles\n";
    }
    ~MemoryBuffer() { delete[] data_; }

    // Move Constructor
    MemoryBuffer(MemoryBuffer&& other) noexcept 
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
        std::cout << "Moved buffer\n";
    }

    // Move Assignment
    MemoryBuffer& operator=(MemoryBuffer&& other) noexcept {
        if (this != &other) {
            delete[] data_;
            data_ = other.data_;
            size_ = other.size_;
            other.data_ = nullptr;
            other.size_ = 0;
        }
        return *this;
    }

    // Disable Copy for demonstration
    MemoryBuffer(const MemoryBuffer&) = delete;
    MemoryBuffer& operator=(const MemoryBuffer&) = delete;
};

MemoryBuffer create_large_buffer() {
    return MemoryBuffer(1000000); // RVO or Move
}

int main() {
    MemoryBuffer b1 = create_large_buffer();
    MemoryBuffer b2 = std::move(b1); // Explicit move
    return 0;
}












































































































































