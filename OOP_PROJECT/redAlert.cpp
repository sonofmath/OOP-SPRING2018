#include <iostream>
#include <stdlib.h>
#include "redAlert.h"

using namespace std;

redAlert::redAlert():yellowAlert() {
}

string redAlert::getMessage() {
	string message;
	getTime();
	message = "The current time is " + currenttime + ", the water level is " + to_string(waterLevel) + "\n";
	return message;
}

void redAlert::sendEmail() {
	system("python sendRed.py \"sonofmath3.14@gmail.com\" \"Red Alert\" \"The water level has risen.\"");
}

redAlert::~redAlert() {}
