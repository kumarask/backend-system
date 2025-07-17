#include "BaseBackend.h"
#include <thread>
#include <chrono>

void BaseBackend::start() {
    running_ = true;
    initCallback();
    while (running_) {
        loopCallback();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    cleanCallback();
}

void BaseBackend::stop() {
    running_ = false;
}
