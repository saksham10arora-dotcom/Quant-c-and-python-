/**
 * Topic: Simple Single-Producer Single-Consumer (SPSC) Ring Buffer
 */
#include <iostream>
#include <atomic>
#include <vector>
#include <optional>

template<typename T, size_t Size>
class SPSCQueue {
    static_assert((Size & (Size - 1)) == 0, "Size must be power of 2");
    std::vector<T> buffer_;
    alignas(64) std::atomic<size_t> head_{0};
    alignas(64) std::atomic<size_t> tail_{0};

public:
    SPSCQueue() : buffer_(Size) {}

    bool enqueue(T val) {
        size_t h = head_.load(std::memory_order_relaxed);
        if (h - tail_.load(std::memory_order_acquire) == Size) return false;
        buffer_[h & (Size - 1)] = std::move(val);
        head_.store(h + 1, std::memory_order_release);
        return true;
    }

    std::optional<T> dequeue() {
        size_t t = tail_.load(std::memory_order_relaxed);
        if (t == head_.load(std::memory_order_acquire)) return std::nullopt;
        T val = std::move(buffer_[t & (Size - 1)]);
        tail_.store(t + 1, std::memory_order_release);
        return val;
    }
};

int main() {
    SPSCQueue<int, 1024> q;
    q.enqueue(100);
    auto val = q.dequeue();
    if (val) std::cout << "Dequeued: " << *val << "\n";
    return 0;
}






























































































































































