#include "Queue.h"

template<typename T>
void Queue<T>::enqueue(T item) {
    std::lock_guard<std::mutex> lock(mutex_);
    queue_.push(item);
    cond_.notify_one();
}

template<typename T>
bool Queue<T>::dequeue(T &item) {
    std::unique_lock<std::mutex> lock(mutex_);
    cond_.wait(lock, [this] { return !queue_.empty(); });
    item = queue_.front();
    queue_.pop();
    return true;
}

template<typename T>
size_t Queue<T>::size() {
    std::lock_guard<std::mutex> lock(mutex_);
    return queue_.size();
}

// Explicit template instantiation
template class Queue<std::string>;
