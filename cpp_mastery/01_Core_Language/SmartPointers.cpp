/**
 * Topic: Smart Pointers (std::unique_ptr, std::shared_ptr)
 */
#include <iostream>
#include <memory>
#include <vector>

class Order {
public:
    uint64_t id;
    double price;
    Order(uint64_t i, double p) : id(i), price(p) {
        std::cout << "Order " << id << " created\n";
    }
    ~Order() { std::cout << "Order " << id << " destroyed\n"; }
};

void process_order(const std::unique_ptr<Order>& order) {
    std::cout << "Processing order " << order->id << " at price " << order->price << "\n";
}

int main() {
    // 1. unique_ptr - Sole ownership
    auto my_order = std::make_unique<Order>(1, 150.25);
    process_order(my_order);

    // 2. shared_ptr - Shared ownership
    auto shared_order = std::make_shared<Order>(2, 200.50);
    {
        auto another_ref = shared_order;
        std::cout << "Reference count: " << shared_order.use_count() << "\n";
    }
    std::cout << "Reference count after scope: " << shared_order.use_count() << "\n";

    return 0;
}






















































































































































