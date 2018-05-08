#pragma once
#include "generalAlert.h"

class greenAlert: public generalAlert {
  public: greenAlert();
  public: virtual void sendEmail();
  public: virtual ~greenAlert();
};
