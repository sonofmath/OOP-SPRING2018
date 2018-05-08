#include <iostream>
#include "generalAlert.h"

using namespace std;

generalAlert::generalAlert() {
	waterLevel = 0;
	message = "";
}

void generalAlert::setWaterLevel(int input) {
	waterLevel = input;
}

int generalAlert::getWaterLevel() const {
	return waterLevel;
}

string generalAlert::getMessage() {
	return message;
}

void generalAlert::setMessage(string str) {
	message = str;
}

generalAlert::~generalAlert() {}
