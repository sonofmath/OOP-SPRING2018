#include <iostream>
#include <string>
#include <fstream>
#include "FirstAlert.h"

using namespace std;

int main()
{
	FirstAlert MyAlert = FirstAlert();
	MyAlert.checkWaterLevel();

	return 0;
}
