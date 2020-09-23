#include <iostream>
using namespace std;
int main()
{
	int num1, num2, result;
	string opt;
	cout << "Enter first number: ";
	cin >> num1;
	cout << "Enter second number: ";
	cin >> num2;
	cout << "Enter operator(+, - , * , /): ";
	cin >> opt;
	
	if (opt == "+")
	{
		result = num1 + num2;
		cout << "The sum of " << num1 << " and " << num2 << " is: " << result << endl; 
	}
	else if (opt == "-")
	{
		result = num1 - num2;
		cout << "The subtraction of " << num1 << " and " << num2 << " is: " << result << endl; 
	}
	else if (opt == "*")
	{
		result = num1 * num2;
		cout << "The multiplication of " << num1 << " and " << num2 << " is: " << result << endl; 
	}
	else if (opt == "/")
	{
		if (num2 == 0)
		{
			cout << "Error...! division with zero is not possible." << endl;
		}
		else 
		{
			result = num1 / num2;
			cout << "The division of " << num1 << " and " << num2 << " is: " << result << endl; 
		}
	}
	else 
	{
		cout << "Error...! Invalid operator." << endl;
	}
	return 0;
}
