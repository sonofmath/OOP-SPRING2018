#pragma once
#include "greenAlert.h"
#include "yellowAlert.h"
#include "redAlert.h"

class FirstAlert {
public: FirstAlert();
public: void checkWaterLevel();
public: ~FirstAlert();
private: greenAlert *green;
private: yellowAlert *yellow;
private: redAlert *red;
};
