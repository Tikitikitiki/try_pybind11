#include "Animal.hpp"

// constructor
Animal::Animal(const std::string &name) : name_{name} {}

// member function
void Animal::SetHobby(const std::string &hobby) { hobby_ = hobby; }

std::string Animal::GetName() { return name_; }

std::string Animal::GetHobby() { return hobby_; }

void Animal::PrintAnimal() {
  std::cout << "from cpp file: " << name_ << " has hobby " << hobby_
            << std::endl;
}