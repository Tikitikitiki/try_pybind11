#include <iostream>

#include "Animal.hpp"

using namespace std;

int main() {
  string simba_hobby = "Programming";
  string simba_name = "Simba";
  auto ptr_simba = make_unique<Animal>(simba_name);
  ptr_simba->SetHobby(simba_hobby);
  ptr_simba->PrintAnimal();
}
