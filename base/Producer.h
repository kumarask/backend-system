#pragma once
#include "BaseBackend.h"
#include "Queue.h"
#include <string>

class Producer : public BaseBackend {
public:
    Producer(Queue<std::string> &queue);
    void initCallback() override;
    void loopCallback() override;
    void cleanCallback() override;

private:
    Queue<std::string> &queue_;
};
