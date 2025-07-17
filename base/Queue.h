#pragma once
#include <queue>
#include <mutex>
#include <condition_variable>

template<typename T>
class Queue {
public:
    void enqueue(T item);
    bool dequeue(T &item);
    size_t size();

private:
    std::queue<T> queue_;
    std::mutex mutex_;
    std::condition_variable cond_;
};
