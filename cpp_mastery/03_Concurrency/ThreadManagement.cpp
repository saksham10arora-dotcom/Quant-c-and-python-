/**
 * Topic: Concurrency (Threads and Mutexes)
 */
#include <iostream>
#include <thread>
#include <mutex>
#include <vector>

std::mutex mtx;
int shared_counter = 0;

void increment(int n) {
    for (int i = 0; i < n; ++i) {
        std::lock_guard<std::mutex> lock(mtx);
        shared_counter++;
    }
}

int main() {
    std::vector<std::thread> threads;
    for (int i = 0; i < 5; ++i) {
        threads.emplace_back(increment, 10000);
    }

    for (auto& t : threads) {
        t.join();
    }

    std::cout << "Final counter: " << shared_counter << "\n";
    return 0;
}














































































































































