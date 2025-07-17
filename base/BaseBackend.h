#pragma once

class BaseBackend {
public:
    virtual void initCallback() = 0;
    virtual void loopCallback() = 0;
    virtual void cleanCallback() = 0;
    virtual void start();
    virtual void stop();
    virtual ~BaseBackend() = default;

protected:
    bool running_ = false;
};
