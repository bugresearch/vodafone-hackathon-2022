#include <VirtualWire.h>
char *message;

void setup(){
    Serial.begin(9600);
    pinMode(buton, INPUT);
    vw_set_ptt_inverted(true);
    vw_set_tx_pin(12);
    vw_setup(4000); 
}

String hashtable(veri){
    String[] charmap = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001", ,"1010", ,"1011"];
    String[] chars = ["0","1","2","3","4","5","6","7","8","9",".","@"]
    int veri_len = veri.length() + 1
    char char_array[veri_len];
    String send = "";
    for(int i = 0; i < char_array.sizeOf(); i++){
        for(int j = 0; j < char_array.sizeOf(); j++){
            if(chars[j] == char_array[i]){
                send = send+charmap[j];
                break;
            }
        }
    }
    return send;
}

void loop(){ 

    if (Serial.available() > 0){
        incomingByte = Serial.read();
        String send = hashtable(incomingByte);
        vw_send((uint8_t *)message, strlen(message));
        vw_wait_tx();
    }
    delay(100);
}