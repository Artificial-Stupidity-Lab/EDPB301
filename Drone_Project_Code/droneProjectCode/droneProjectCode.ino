//libraries used
#include <Wire.h> 
#include <LiquidCrystal_I2C.h> /*LCD*/
#include <Servo.h>
//variables used
float dronePosition = 0.00;
String userInput;
char arduinoData[15];
//joystick1
int Ypin1=A0;
int Xpin1=A1;
int Bpin1=52;
int Yval1;
int Xval1;
int Bval1;
//joystick1
int Ypin2=A8;
int Xpin2=A9;
int Bpin2=50;
int Yval2;
int Xval2;
int Bval2;
//pb variables
const int pb_take_Pic_pin = 3;
int TakePicture;
int escape;
const int pb_exit_pin = 2;
//led variables
const int indicator_led = 4;

void setup(){

}

void loop(){
    surveillanceMoves();
}

//functions
//comm functions
int talk(char data[15]){
  Serial.println(data);
  delay(500);
}

void listen(){
  while(Serial.available()==0){
    //do nothing while there is no data
  }
  userInput = Serial.readStringUntil("\r");
}

//init arduino
void initArduino(){
    Serial.begin(115200);
    pinMode(indicator_led, OUTPUT);
    pinMode(pb_take_Pic_pin,INPUT);
    pinMode(pb_exit_pin,INPUT);
}

void notify(){
    digitalWrite(indicator_led, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(500);                       // wait for a second
    digitalWrite(indicator_led, LOW);    // turn the LED off by making the voltage LOW
    delay(500);  
}

void surveillanceMoves(){
    Xval1=analogRead(Xpin1);
    Xval2=analogRead(Xpin2);
    Yval1=analogRead(Ypin1);
    Yval2=analogRead(Ypin2);
    Bval1=digitalRead(Bpin1);
    Bval2=digitalRead(Bpin2);
    TakePicture=digitalRead(pb_take_Pic_pin);
    escape=digitalRead(pb_exit_pin);
    if(Xval1==0){
        //tell python to go left
        talk("left");
        notify();
    }
    if(Xval1==1023){
        //tell python to go right
        talk("right");
        notify();
    }
    if(Xval2==0){
        //tell pyton to rotate left
        talk("antiClockwise");
        notify();
    }
    if(Xval2==1023){
        //tell python to rotate right
        talk("clockwise");
        notify();
    }
    if(Bval1==0 && Bval2==1){
        //tell py to speed up
        talk("speedUp");
        notify();
    }
    if(Bval2==0 && Bval1==1){
        //tell py to slow down
        talk("speedDown");
        notify();
    }
    if(Yval1==0){
        //tell python to go back
        talk("back");
        notify();
    }
    if(Yval1==1023){
        //tell python to go forward
        talk("forward");
        notify();
    }
    if(Yval2==0){
        //tell pyton to move down
        talk("down");
        notify();
    }
    if(Xval2==1023){
        //tell python to move up
        talk("up");
        notify();
    }
    if(Bval1==0 && Bval2==0){
        //tell drone to land or go up
        talk("landTakeoff");
        notify();
        delay(3000);
    }
    if(TakePicture==0){
        //big PB
        talk("takePic");
        notify();

    if(escape==0){
        //samll pb
        talk("escape");
        notify();
    }
    }
    /*if(Bval1==1 & Bval2==1){
        radar();
        notify();
    }*/
    else{
        talk("none");
    }
    
}
/*void radar(){
    //radar control the stepper motor
    //may have to remove
    listen();
    radar_var = userInput;

}*/
void getWeather(){
    //reading the barometer reading
    //may have to remove

}
