#pragma once
#include "generalAlert.h"

class yellowAlert: public generalAlert {
	public: yellowAlert();
	public: virtual string getMessage() override;
	public: virtual void sendEmail();
	public: virtual ~yellowAlert();
	protected: virtual void getTime();
	protected: string currenttime;
};
