const int sensorPin = 2;
int lastState = HIGH;
int count = 0;

void setup() {
  Serial.begin(9600);
  pinMode(sensorPin, INPUT);
}

void loop() {
  int current = digitalRead(sensorPin);

  if (current == LOW && lastState == HIGH) {
    count++;
    Serial.print("DETECTED:");
    Serial.println(count);
  }

  lastState = current;
  delay(50);
}