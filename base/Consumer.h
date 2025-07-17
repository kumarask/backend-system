#pragma once
#include "BaseBackend.h"
#include "Queue.h"
#include <string>

class Consumer : public BaseBackend {
public:
    Consumer(Queue<std::string> &queue);
    void initCallback() override;
    void loopCallback() override;
    void cleanCallback() override;

private:
    Queue<std::string> &queue_;
    int retry_count_ = 3;
};
