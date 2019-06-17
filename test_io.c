
#include <stdio.h>
//building this file ,must use -lwiringPi 
#include<wiringPi.h>

int main()
{
	wiringPiSetup();
	pinMode(15, OUTPUT);
//	pinMode(1, PWM_OUTPUT);
//
////	pwmWrite(1, 1024);
//
//	pwmSetMode(PWM_MODE_BAL);
//	pwmSetRange(2000);
//	//
//	pwmSetClock(192);
//
//	for(int i = 2; i>0; i--){
////		pwmWrite(1, 5);
////	delay(5000);
//	pwmWrite(1, 150);
//	delay(5000);
//	pwmWrite(1, 200);
//	delay(5000);
//	}
//	digitalWrite(15, HIGH);
//	delayMicroseconds(1500);
//	digitalWrite(15, LOW);
//	delayMicroseconds(1500);
//
	pinMode(1, OUTPUT);
	digitalWrite(1, HIGH);
	delay(5000);
	digitalWrite(1, LOW);
	delay(5000);


	return 0;
}
