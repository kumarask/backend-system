#include "Producer.h"
#include <iostream>

Producer::Producer(Queue<std::string> &queue) : queue_(queue) {}

void Producer::initCallback() {
    std::cout << "Producer initialized.\n";
}

void Producer::loopCallback() {
    static int count = 0;
    std::string msg = "Message " + std::to_string(count++);
    queue_.enqueue(msg);
    std::cout << "Produced: " << msg << std::endl;
}

void Producer::cleanCallback() {
    std::cout << "Producer cleanup done.\n";
}
