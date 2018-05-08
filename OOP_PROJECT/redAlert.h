#pragma once
#include "yellowAlert.h"

class redAlert: public yellowAlert {
	public: redAlert();
	public: virtual string getMessage() override;
	public: virtual void sendEmail() override;
	public: virtual void setHumidity(int input);
	public: virtual ~redAlert();
	protected: int humidity;
};
