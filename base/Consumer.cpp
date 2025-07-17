#include "Consumer.h"
#include <iostream>

Consumer::Consumer(Queue<std::string> &queue) : queue_(queue) {}

void Consumer::initCallback() {
    std::cout << "Consumer initialized.\n";
}

void Consumer::loopCallback() {
    std::string item;
    for (int i = 0; i < retry_count_; ++i) {
        if (queue_.dequeue(item)) {
            std::cout << "Consumed: " << item << std::endl;
            return;
        } else {
            std::cerr << "Dequeue failed, retrying...\n";
        }
    }
}

void Consumer::cleanCallback() {
    std::cout << "Consumer cleanup done.\n";
}
