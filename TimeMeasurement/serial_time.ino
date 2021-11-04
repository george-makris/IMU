void setup(){
    Serial.begin(115200); // Starting the serial port
}

void loop(){
    Serial.println(millis()); // Print to the serial point the time in ms that has passed since the beginning
}

