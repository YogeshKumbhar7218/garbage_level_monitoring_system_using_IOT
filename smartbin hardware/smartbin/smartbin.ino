#include <SoftwareSerial.h>
#define RX 6                    //pin 6 as receiver
#define TX 7                    //pin 7 as transmitter

String AP ="root";              //wifi Router name
String PASS ="pppppppp";        //wifi router password
String HOST = "192.168.155.6";  //Server IP address or Domain name
String PORT = "80";             //server port number


int countTrueCommand;           //for debugging purpose
int countTimeCommand;           //for debugging purpose
boolean found = false; 
SoftwareSerial esp8266(RX,TX); 
  
String bin_no="1";              //Dustbin number


int dry_trigPin=5;              //trigger pin for dry dustbin
int dry_echoPin=4;              //echo pin for dry dustbin

int wet_trigPin=3;              //trigger pin for wet dustbin
int wet_echoPin=2;              //echo pin for wet dustbin

int pingTravelTime;             //for storing wave travel time
float distance;                 //for storing calculated distance
float dry;                      //for storing dry dustbin's distance
float wet;                      //for stiring wet distbin's distnace

String uri;                     //to store url
String sendData;                //to store HTTP GET method (data to be sent)

void setup() {
  //set IO pins for ultrasonc sensor
  pinMode(dry_trigPin,OUTPUT);      
  pinMode(dry_echoPin,INPUT);

  pinMode(wet_trigPin,OUTPUT);
  pinMode(wet_echoPin,INPUT);
  
  //begin serial communication with esp on 9600 baudrate
  Serial.begin(9600);
  esp8266.begin(9600);
//  Serial.begin(115200);
//  esp8266.begin(115200);
  sendCommand("AT",5,"OK",false);
  delay(500);
  ConnectToWifi();                  //connect to wifi router
}


void loop() {

  //Get distance between Garbage and ultrasonic sensor for dry and wet bin
  dry = getDistance(dry_trigPin, dry_echoPin);
  wet = 100.0;//getDistance(wet_trigPin, wet_echoPin);


  //URL for sending data
  uri="/get_smartbin_data/?bin_no="+bin_no+"&dry_filled="+String(dry)+"&wet_filled="+String(wet);


  //For HTTP GET method
  sendData=
  "GET " + uri + " HTTP/1.0\n" +
  "Host: " + HOST + "\n" +
  "\n";


  //For HTTP POST method        //Django does'nt support due to csrf_token verification
//  sendData=
//  "PUT "+ uri +" HTTP/1.1\n"+
//  "Host: " + HOST + "\n" +
//  "Content-Type: application/json\n"+
//  "Content-Length: 80\n"+
//  "{\n"+
//    "\"Id\": 12345,\n"+
//    "\"Customer\": \"John Smith\",\n"+
//    "\"Quantity\": 1,\n"+
//    "\"Price\": 10.00\n"+
//  "}\n";


 sendCommand("AT+CIPMUX=1",2,"OK",false); //
 sendCommand("AT+CIPSTART=4,\"TCP\",\""+ HOST +"\","+ PORT,10,"OK",false);    //Establish tcp connection with server wih HOST and PORT
 sendCommand("AT+CIPSEND=4," +String(sendData.length()+4),3,">",false);       //Register Size of data to be sent
 sendCommand(sendData,5,"OK",false);                                          //Send data
 delay(1000);
 countTrueCommand++;
 sendCommand("AT+CIPCLOSE=0",2,"OK",false);                                   //Close connection
}




//Function for connecting to the wifi router
bool ConnectToWifi(){
  for (int a=0; a<15; a++)
  {
    sendCommand("AT",5,"OK",false);
    sendCommand("AT+CWMODE=1",5,"OK",false);                                                  //Set esp to station mode(Client mode)
    boolean isConnected = sendCommand("AT+CWJAP=\""+ AP +"\",\""+ PASS +"\"",20,"OK",false);  //Connect to wifi with AP and PASS
    if(isConnected)
    {
      return true;
    }
  }
}


//For executing the commands and checking for success and failures
bool sendCommand(String command, int maxTime, char readReplay[],boolean isGetData) {
  boolean result=false;

  //Test Purpose
  Serial.print(countTrueCommand);
  Serial.print(". at command => ");
  Serial.print(command);
  Serial.print(" ");
  while(countTimeCommand < (maxTime*1))
  {
    esp8266.println(command);
    if(esp8266.find(readReplay))//ok
    {   
      result = true;
      break;
    }
    countTimeCommand++;
  }
  
  if(result == true)
  {
    Serial.println("Ture");
    countTrueCommand++;
    countTimeCommand = 0;
  }
  
  if(result == false)
  {
    Serial.println("False");
    countTrueCommand = 0;
    countTimeCommand = 0;
  }
  
  found = false;
  return result;
 }



//for getting distance through ultrasonic sensor
float getDistance(int trigPin, int echoPin){

  int i;
  int noMeas=100;   //Number of measures to be taken
  float avg=0;      //For storing the result of average

  //calculate distance noMeas times 
  for(i=0;i<noMeas;i++){
    digitalWrite(trigPin,LOW);
    delayMicroseconds(10);
    digitalWrite(trigPin,HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin,LOW);
    pingTravelTime=pulseIn(echoPin,HIGH);                 //Get wave travel time
//    distance=(123436685./3600000000.)*pingTravelTime;   //calculate distance from wave travel time
    distance=(0.034287968)*pingTravelTime;
    distance=distance/2.;
    avg=avg+distance;
    delay(10);
    
    }
    avg=avg/noMeas;        //calculate average distnace

  return avg;             //return distance
  
}
