#pragma once
#include "greenAlert.h"
#include "yellowAlert.h"
#include "redAlert.h"
#include "alertState.h"

class FirstAlert {
public: FirstAlert();
public: void checkWaterLevel();
public: void setAlertState(alertState state);
public: virtual alertState getAlertState() const;
public: ~FirstAlert();
protected: alertState alertstate;
private: greenAlert *green;
private: yellowAlert *yellow;
private: redAlert *red;
};
