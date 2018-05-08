#include <iostream>
#include <stdlib.h>
#include "greenAlert.h"

using namespace std;

greenAlert::greenAlert():generalAlert() {}

void greenAlert::sendEmail() {
  system("python send.py \"sonofmath3.14@gmail.com\" \"Green Alert\" \"Everything looks good. No water detected.\"");
}

greenAlert::~greenAlert() {}
