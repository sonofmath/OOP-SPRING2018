#include <iostream>
#include <ctime>
#include <stdlib.h>
#include "yellowAlert.h"

using namespace std;

yellowAlert::yellowAlert():generalAlert(){
	getTime();
}

string yellowAlert::getMessage() {
	string message;
	getTime();
	message = "The current time is " + currenttime + ", the water level is " + to_string(waterLevel) + "\n";
	return message;
}

void yellowAlert::sendEmail() {
	system("python send.py \"sonofmath3.14@gmail.com\" \"Yellow Alert\" \"There has been water detected.\"");
}

void yellowAlert::getTime() {
	time_t rawtime;
	struct tm * timeinfo;
	char buffer[80];

	time (&rawtime);
	timeinfo = localtime(&rawtime);

	strftime(buffer, sizeof(buffer), "%d-%m-%Y %I:%M:%S", timeinfo);
	string str(buffer);
	currenttime = str;
}

yellowAlert::~yellowAlert() {}
