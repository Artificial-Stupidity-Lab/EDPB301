//libraries used
#include <Wire.h> 
#include <LiquidCrystal_I2C.h> /*LCD*/
#include <Servo.h>
//variables used
float dronePosition = 0.00;
char userInput[15];
char arduinoData[15];
//joystick1
int Ypin1=A0;
int Xpin1=A1;
int Bpin1=20;
int Yval1;
int Xval1;
int Bval1;
//joystick1
int Ypin2=A2;
int Xpin2=A3;
int Bpin2=21;
int Yval2;
int Xval2;
int Bval2;


void setup(){

}

void loop(){
    surveillanceMoves();
}

//functions
//comm functions
void talk(data){
  Serial.println(data);
  delay(500);
}

listen(){
  while(Serial.available()==0){
    //do nothing while there is no data
  }
  userInput = Serial.readStringUntil("\r");
}

//init arduino
void initArduino(){
    Serial.begin(115200);
}

void surveillanceMoves(){
    Xval1=analogRead(Xpin1);
    Xval2=analogRead(Xpin2);
    Yval1=analogRead(Ypin1);
    Yval2=analogRead(Ypin2);
    Bval1=digitalRead(Bpin1);
    Bval2=digitalRead(Bpin2);
    if(Xval1==0){
        //tell python to go left
        talk(left);
    }
    if(Xval1==1023){
        //tell python to go right
        talk(right);
    }
    if(Xval2==0){
        //tell pyton to rotate left
        talk(antiClockwise);
    }
    if(Xval2==1023){
        //tell python to rotate right
        talk(clockwise);
    }
    if(Bval1==0){
        //tell py to speed up
        talk(speedUp);
    }
    if(Bval2==0){
        //tell py to slow down
        talk(speedDown);
    }
    if(Yval1==0){
        //tell python to go back
        talk(back);
    }
    if(Yval1==1023){
        //tell python to go forward
        talk(forward);
    }
    if(Yval2==0){
        //tell pyton to move down
        talk(down);
    }
    if(Xval2==1023){
        //tell python to move down
        talk(up);
    }
    if(Bval1==0 && Bval2==0){
        //tell drone to land or go up
        talk(landTakeoff);
        delay(3000);
    }
    if(TakePicture==1){
        talk(takePic);
    }
    if(Bval1==1 & Bval2==1){
        radar();
    }
    else(){
        talk(none);
    }
    
}
void radar(){
    //radar control the stepper motor
    //may have to remove
    listen();
    radar = userInput;

}
void getWeather(){
    //reading the barometer reading
    //may have to remove

}