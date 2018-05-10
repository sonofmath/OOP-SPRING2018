#include <iostream>
#include <fstream>
#include <unistd.h>
#include <ctime>
#include <string>
#include "alertState.h"
#include "FirstAlert.h"

using namespace std;

FirstAlert::FirstAlert():alertstate(alertState::GREEN) {
  green = new greenAlert();
  yellow = new yellowAlert();
  red = new redAlert();
}

void FirstAlert::setAlertState(alertState state) {
  alertstate = state;
}

alertState FirstAlert::getAlertState() const {
  return alertstate;
}

void FirstAlert::checkWaterLevel()
{
  time_t now = time(0);
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
    tm *ltm = localtime(&now);
    //Checks if the time is between 7:44 and 7:59 AM to send Green Message status
    getAlertState();
    if((ltm->tm_hour > 7 && ltm->tm_hour < 8 && ltm->tm_min < 59 && ltm->tm_min > 44) || (alertstate==alertState::YELLOW) || (alertstate == alertState::RED))
    {
      // Since we're at Green mode, we set water level and send an update email.
      green->setWaterLevel(waterLevel);
      green->sendEmail();
      setAlertState(GREEN);
      cout << "Alert type GREEN sent!\n";
    }
  }
  else if(waterLevel < 100)
  {
    yellow->setWaterLevel(waterLevel);
    yellow->sendEmail();
    setAlertState(YELLOW);
    cout << "Alert type YELLOW sent!\n";
  }
  else {
    red->setWaterLevel(waterLevel);
    red->sendEmail();
    setAlertState(RED);
    cout << "Alert type RED sent!\n";
  }
	input.close();
}



FirstAlert::~FirstAlert() {
  delete green;
  delete yellow;
  delete red;
}
