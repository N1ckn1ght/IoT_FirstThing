constexpr auto pinSensor = A0;
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  int valueSensor = analogRead(pinSensor);
  Serial.println(valueSensor);
  delay(1000);
}
