/**
 * Topic: Limit Order Book (Simplified)
 */
#include <iostream>
#include <map>
#include <list>
#include <unordered_map>

enum class Side { BUY, SELL };

struct Order {
    uint64_t id;
    double price;
    uint32_t qty;
    Side side;
};

class OrderBook {
    std::map<double, uint32_t, std::greater<double>> bids_;
    std::map<double, uint32_t> asks_;

public:
    void add_order(const Order& o) {
        if (o.side == Side::BUY) bids_[o.price] += o.qty;
        else asks_[o.price] += o.qty;
    }

    void print() {
        std::cout << "--- ASK ---\n";
        for (auto it = asks_.rbegin(); it != asks_.rend(); ++it)
            std::cout << it->first << " | " << it->second << "\n";
        std::cout << "--- BID ---\n";
        for (auto const& [p, q] : bids_)
            std::cout << p << " | " << q << "\n";
    }
};

int main() {
    OrderBook ob;
    ob.add_order({1, 100.5, 10, Side::BUY});
    ob.add_order({2, 100.6, 5, Side::SELL});
    ob.print();
    return 0;
}































































































































































