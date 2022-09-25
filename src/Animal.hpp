#ifndef ANIMAL_HPP
#define ANIMAL_HPP
#include <iostream>
#include <string>

class Animal {
 private:
  std::string name_;
  std::string hobby_;

 public:
  Animal(const std::string &name);

  void SetHobby(const std::string &hobby);

  std::string GetName();
  std::string GetHobby();

  void PrintAnimal();
};

#endif