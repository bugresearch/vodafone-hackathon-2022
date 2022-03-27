#include <VirtualWire.h> 
#define led 3 
char message[] = " ";
void setup() 
{
pinMode(led, OUTPUT);
Serial.begin(9600);
vw_set_ptt_inverted(true);
vw_set_rx_pin(11); 
vw_setup(4000);
vw_rx_start();
} 
void loop() 
{ 
uint8_t buf[VW_MAX_MESSAGE_LEN];
uint8_t buflen = VW_MAX_MESSAGE_LEN; 
if (vw_get_message(buf, &buflen)) 
{
message[0] = (char) buf[0]; 
if (message[0] == '0') 
{ 
Serial.println(message[0]);
digitalWrite(led, LOW);
} 
else if (message[0] == '1')
{
Serial.println(message[0]);
digitalWrite(led, HIGH);
}
}
}