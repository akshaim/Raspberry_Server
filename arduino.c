int i=0;
void setup(){  
  Serial.begin(9600);    // Open serial connection at a baud rate of 9600
  pinMode(13, OUTPUT);   //set pin13 in o/p mode
}

void loop(){ 
while(1)
{
Serial.write('\n'); 
Serial.write("10.028371,76.328873"); 
delay(1000);
  }
}
