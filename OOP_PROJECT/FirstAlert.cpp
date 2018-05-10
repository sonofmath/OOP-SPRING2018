#include <iostream>
#include <fstream>
#include <unistd.h>
#include <string>
#include "FirstAlert.h"

using namespace std;

FirstAlert::FirstAlert() {
  green = new greenAlert();
  yellow = new yellowAlert();
  red = new redAlert();
}

void FirstAlert::checkWaterLevel()
{
  int waterLevel = 0;
  ifstream input;
	input.open("/dev/ttyACM0");
	if(input.fail())
	{
		cout << "Could not open serial port! \n";
	}
	input>>waterLevel;
  if(waterLevel <= 0)
  {
    // Since we're at Green mode, we set water level and send an update email.
    green->setWaterLevel(waterLevel);
    green->sendEmail();
    cout << "Alert type GREEN sent!\n";
  }
  else if(waterLevel < 100)
  {
    yellow->setWaterLevel(waterLevel);
    yellow->sendEmail();
    cout << "Alert type YELLOW sent!\n";
  }
  else {
    red->setWaterLevel(waterLevel);
    red->sendEmail();
    cout << "Alert type RED sent!\n";
  }
	input.close();
}



FirstAlert::~FirstAlert() {
  delete green;
  delete yellow;
  delete red;
}
