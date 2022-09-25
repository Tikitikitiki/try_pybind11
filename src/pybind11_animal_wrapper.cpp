#include <pybind11/pybind11.h>

#include "Animal.hpp"

namespace py = pybind11;

PYBIND11_MODULE(animal, m) {
  py::class_<Animal>(m, "Animal")
      .def(py::init<const std::string &>())
      .def("set_hobby", &Animal::SetHobby, "Set the hobby of the animal")
      .def("get_name", &Animal::GetName, "Set the name of the animal")
      .def("get_hobby", &Animal::GetHobby, "Set the hobby of the animal")
      .def("print_animal", &Animal::PrintAnimal,
           "Print out animal name and hobby");
}