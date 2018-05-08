#pragma once
#include <string>

using std::string;

class generalAlert {
	public: generalAlert();
	public: int getWaterLevel() const;
  public: void setWaterLevel(int input);
	public: virtual string getMessage();
	public: void setMessage(string input);
	//public: virtual void sendEmail() = 0;
	public: virtual ~generalAlert();

	protected: int waterLevel;
	protected: string message;
};
