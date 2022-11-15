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
initArduino();
}

void loop(){
    surveillanceMoves();
}

//functions
//comm functions
int talk(char data[15]){
  Serial.println(data);
  delay(250);
}

void listen(){
  while(Serial.available()==0){
    //do nothing while there is no data
  }
  userInput = Serial.readStringUntil("\r");
}

//init arduino
void initArduino(){
    Serial.begin(9600);
    pinMode(indicator_led, OUTPUT);
    pinMode(pb_take_Pic_pin,INPUT);
    pinMode(pb_exit_pin,INPUT);
    pinMode(Xpin1,INPUT);
    pinMode(Xpin2,INPUT);
    pinMode(Ypin1,INPUT);
    pinMode(Ypin2,INPUT);
    pinMode(Bpin1,INPUT);
    pinMode(Bpin2,INPUT);
}

void notify(){
    digitalWrite(indicator_led, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(50);                       // wait for a second
    digitalWrite(indicator_led, LOW);    // turn the LED off by making the voltage LOW
    delay(50);  
}

void surveillanceMoves(){
    Xval1=analogRead(Xpin1);
    Xval2=analogRead(Xpin2);
    Yval1=analogRead(Ypin1);
    Yval2=analogRead(Ypin2);
    Bval1=digitalRead(Bpin1);
    Bval2=digitalRead(Bpin2);
    standby=digitalRead(pb_take_Pic_pin);
    //escape=digitalRead(pb_exit_pin);
    if(Xval1<50){
        //tell python to go left
        //yellow left
        talk("left");
        notify();
    }
    if(Xval1>900){
        //tell python to go right
        //yellow right
        talk("right");
        notify();
    }
    if(Xval2<50){
        //tell pyton to rotate left
        //red left       
        talk("antiClockwise");
        notify();
    }
    if(Xval2>900){
        //tell python to rotate right
        //red right
        talk("clockwise");
        notify();
    }
    if(Bval1==1 && Bval2==0){
        //tell py to speed up
        //landTake off, yellow press
        talk("landTakeoff");
        notify();
        delay(3000);
    }
    if(Bval2==1 && Bval1==0){
        //tell py to slow down
        //take picture, red press
        talk("takePic");
        notify();       
    }
    if(Yval1<50){
        //tell python to go back
        talk("back");
        notify();
    }
    if(Yval1>900){
        //tell python to go forward
        talk("forward");
        notify();
    }
    if(Yval2<50){
        //tell pyton to move down
        talk("down");
        notify();
    }
    if(Yval2>900){
        //tell python to move up
        talk("up");
        notify();
    }
    if(standby==0){
        //tell drone to land or go up
        talk("standby");
        notify();
        delay(3000);
    }
   /* if(TakePicture==0){
        //big PB
        talk("takePic");
        notify();
    }

    if(escape==0){
        //samll pb
        talk("landTakeoff");
        notify();
        delay(3000);
    }
    
    /*if(Bval1==1 & Bval2==1){
        radar();
        notify();
    }*/
    else{
        digitalWrite(indicator_led, LOW);
    }
    delay(50);
    
    
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
