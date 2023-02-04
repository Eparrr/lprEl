#include <iostream>

int main() {
    int a, b, b1;
    a = 100; b = 28 ;
    if (a<b) {
      while(b){
      b1 = b;
      b = a % b; 
      a = b1 ;
      std::cout << a << std::endl;
    }
    } else {
      while(a){
      b1 = a;
      b = b % a; 
      b = b1 ;
    }
std::cout << b << std::endl;
    }
return 0;

}