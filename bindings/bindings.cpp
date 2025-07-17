#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "Producer.h"
#include "Consumer.h"
#include "Queue.h"

namespace py = pybind11;

PYBIND11_MODULE(backend_cpp, m) {
    py::class_<Queue<std::string>>(m, "Queue")
        .def(py::init<>())
        .def("enqueue", &Queue<std::string>::enqueue)
        .def("dequeue", [](Queue<std::string> &q) {
            std::string item;
            bool success = q.dequeue(item);
            return py::make_tuple(success, item);
        });

    py::class_<BaseBackend>(m, "BaseBackend");

    py::class_<Producer, BaseBackend>(m, "Producer")
        .def(py::init<Queue<std::string> &>())
        .def("start", &Producer::start)
        .def("stop", &Producer::stop);

    py::class_<Consumer, BaseBackend>(m, "Consumer")
        .def(py::init<Queue<std::string> &>())
        .def("start", &Consumer::start)
        .def("stop", &Consumer::stop);
}
