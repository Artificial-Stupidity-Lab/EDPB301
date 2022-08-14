//libraries used
#include <Wire.h> 
#include <LiquidCrystal_I2C.h> /*LCD*/
#include <Servo.h>
//variables
char userInput;
int control_type; //manual control, 1 is auto
int pre_control_type = 1; //previous control type
int gate_one_state = 0; //closed at 0
int gate_two_state = 0; //closed at 0
int obstacle_one_state; //obtacle at gate 1
int obstacle_two_state; //obtacle at gate 1
int bay_1_state; //empty parking slot
int bay_2_state;
int bay_3_state;
Servo myservo_1; //servo objects
Servo myservo_2;
LiquidCrystal_I2C lcd(0x27,16,2);
//gate ultrasonic variables
const int trig_1 = 4; //trigger pin of sensor 1(entrance)
const int echo_1 = 5; //echo pin of sensor 1
const int trig_2 = 6; //trigger pin of sensor 1
const int echo_2 = 7; //echo pin of sensor 1
//parking bay ultrasonic sensors
const int trig_3 = 22; //trigger pin of sensor 1
const int echo_3 = 23; //echo pin of sensor 1
const int trig_4 = 24; //trigger pin of sensor 1
const int echo_4 = 25; //echo pin of sensor 1
const int trig_5 = 26; //trigger pin of sensor 1
const int echo_5 = 27; //echo pin of sensor 1
const int trig_6 = 28; //trigger pin of sensor 1
const int echo_6 = 29; //echo pin of sensor 1

const int critical_height; //critical height of parking bays
const int critical_dis_1; //distance to entrance
const int critical_dis_2; //distnace to exit

//led_1 variables
const int green_led_1 = 8;
const int red_led_1 = 9;
//led_2 variables
const int green_led_2 = 10;
const int red_led_2 = 11;
//leds at the parking bays
//3
const int green_led_3 = 30;
const int red_led_3 = 31;
//4
const int green_led_4 = 32;
const int red_led_4 = 33;
//5
const int green_led_5 = 34;
const int red_led_5 = 35;
//6
const int green_led_6 = 36;
const int red_led_6 = 37;


void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  //reads for data, this will be the control type
if(Serial.available()>0){
  control_type = Serial.read();

  //manual control
  while(control_type == 0){ 
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
      if(userInput == "f"){
        //what happens when automatic control is selected
        //lines of code
        pre_control_type = 0;
        control_type = 2; //exit manual control
      }
      else{
        //do nothing if there is no new user input
      }
    }
  }

  //automatic control
  while(control_type == 1){ 
   if(Serial.available()>0){
    userInput = Serial.read();
    if(userInput == "g"){
    pre_control_type = 1;
    control_type = 2; //exit automatic
    }
    else{
      /*nothing happens if any other control is pressed during
      auto control*/
    }
   }
   else{
    //normal automatic control
   }
  }


  //change over
  while(control_type == 2){
    /*exiting one contro type and entering another
    turn off led's tell drivers to wait, do a countdown
    but first check i there are any vehicles blocking the exit or entry point*/
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
void Gate_Open_1(){
  myservo_1.write(90);
}

//BooGate Close
void Gate_Close_1(){
  myservo_1.write(0);
}

void Gate_Open_2(){
  myservo_2.write(90);
}

//BooGate Close
void Gate_Close_2(){
  myservo_2.write(0);
}

//close both gates
void Close_Gates(){
  Gate_close_1();
  Gate_Close_2():
}

///////////led functions/////////////
//LED ALL OFF
void LED_ALL_OFF_0(){
  //truns off all leds at the gates 
  digitalWrite(green_led_1,LOW);
  digitalWrite(red_led_1,LOW);
  digitalWrite(green_led_2,LOW);
  digitalWrite(red_led_2,LOW);
}
void LED_ALL_OFF_00(){
  //truning off all parking bay leds
   char* green_leds[] = {"green_led_3", "green_led_4","green_led_5","green_led_6"};
   char* red_led[] = {"red_led_3","red_led_4","red_led_5","red_led_6"};
   for(int i=0; i<4; i++){
    digitalWrite(green_leds[i],LOW);
    digitalWrite(red_leds[i],LOW);
   }
}

void LED_ALL_OFF_1(){
  //turns off leds at gate 1
  digitalWrite(green_led_1,LOW);
  digitalWrite(red_led_1,LOW);
}

void LED_ALL_OFF_2(){
  //turns off leds at gate 2
  digitalWrite(green_led_2,LOW);
  digitalWrite(red_led_2,LOW);
}

void LED_REDS_ON(){
  //turn on both red leds
  digitalWrite(red_led_1,HIGH);
  digitalWrite(red_led_2,HIGH):
  
}

//LED ON
void LED_ON(int LED){
  digitalWrite(LED,HIGH);
}

void init_arduino(){
  Serial.begin(115200);
  myservo_1.attach(2); //servo pin
  myservo_2.attach(3);
  lcd.begin();
  lcd.backlight();
  pinMode(trig_1,OUTPUT);
  pinMode(echo_1,INPUT);
  pinMode(trig_2,OUTPUT);
  pinMode(echo_2,INPUT);
  pinMode(trig_3,OUTPUT);
  pinMode(echo_3,INPUT);
  pinMode(trig_4,OUTPUT);
  pinMode(echo_4,INPUT);
  pinMode(trig_5,OUTPUT);
  pinMode(echo_5,INPUT);
  pinMode(trig_6,OUTPUT);
  pinMode(echo_6,INPUT);
  pinMode(red_led_1, OUTPUT);
  pinMode(red_led_2, OUTPUT);
  pinMode(green_led_1, OUTPUT);
  pinMode(green_led_1, OUTPUT);
  LED_ALL_OFF_0();
  LED_REDS_ON();
  Close_Gates();
  
  
}

//check parking spots
int parking_slots_check(){
  LED_ALL_OFF_00();
  int parking_slots;
  float slot_3, slot_4, slot_5, slot_6;
  int sum; //number of parking slots available
  slot_3 = float gate_reading(int trig_3, int echo_3);
  slot_4 = float gate_reading(int trig_4, int echo_4);
  slot_5 = float gate_reading(int trig_5, int echo_5);
  slot_6 = float gate_reading(int trig_6, int echo_6);
   char* slots[] = {"slot_3", "slot_4", "slot_5", "slot_6"};
   char* green_leds[] = {"green_led_3", "green_led_4","green_led_5","green_led_6"};
   char* red_led[] = {"red_led_3","red_led_4","red_led_5","red_led_6"};
  for(int i=0; i<4; i++){
    if(slots[i] > critical_height){
      sum+=1;
      LED_ON(green_leds[i]);
    }
    else{
      LED_ON(red_leds[i]);
    }

  }
  return sum;
}

//checking for obstruction at gates
//gate 1
void gate_one_check(){
  if(gate_reading(int trig_1, int echo_1)>critical_dis_1){
    obstacle_one_state = 0; //no obstacle
  }
  else{
    obstacle_one_state = 1;
  }
}
//gate 2
void gate_two_check(){
  if(gate_reading(int trig_2, int echo_2)>critical_dis_2){
    obstacle_two_state = 0; //no obstacle
  }
  else{
    obstacle_two_state = 1;
  }
}