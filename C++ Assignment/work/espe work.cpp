#include <iostream>
using namespace std;

int main()
{
   cout << "Hello, World!";
   int age = 20;
   double price = 19.99;
   char grade = 'A';
   string name = "Alice";

   cout << "Name: " << name << endl;
   cout << "Age: " << age << endl;
   cout << "Price: $" << price << endl;
   cout << "Grade: " << grade << endl;

   string name;
   int age;

   cout << "Enter your name: ";
   cin >> name;

   cout << "Enter your age: ";
   cin >> age;

   cout << "Hello, " << name << "! You are " << age << " years old." << endl;

   int a = 10, b = 3;
   cout << "Sum: " << a + b << endl;
   cout << "Difference: " << a - b << endl;
   cout << "Product: " << a * b << endl;
   cout << "Quotient: " << a / b << endl;
   cout << "Remainder: " << a % b << endl;
}