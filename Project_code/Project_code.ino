//libraries used
#include <Wire.h> 
#include <LiquidCrystal_I2C.h> /*LCD*/
#include <Servo.h>
//variables
char userInput;
Servo myservo; //servo object
LiquidCrystal_I2C lcd(0x27,16,2);

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>0){
  userInput = Serial.read();

  if(userInput == "a"){
    //what happens when open gate 1 is pressed
  }
  if(userInput == "b"){
    //what happens when close gate 1 is pressed
  }
  if(userInput == "c"){
    //what happens when open gate 2 is pressed
  }
  if(userInput == "d"){
    //what happens when close gate 2 is pressed
  }
  if(userInput == "e"){
    //what happens when user asks for parking spot available
  }
}
}

//functions
//get ultrasonic reading
float gate_reading(int trigPin, int echoPin){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  // Trigger the sensor by setting the trigPin high for 10 microseconds:
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Read the echoPin, pulseIn() returns the duration (length of the pulse) in microseconds:
  float duration = pulseIn(echoPin, HIGH);
  // Calculate the distance:
  float distance = duration * 0.034 / 2;
  return distance;
}

////////////servo function/////////
//BoomGate Open
void Gate_Open(){
  myservo.write(90);
}

//BooGate Close
void Gate_Close(){
  myservo.write(0);
}

///////////led functions/////////////
//LED ALL OFF
void LED_ALL_OFF(){
  digitalWrite(green_led,HIGH);
  digitalWrite(red_led,HIGH);
  digitalWrite(red_led,HIGH);
}

//LED ON
void LED_ON(int LED){
  digitalWrite(LED,LOW);
}
