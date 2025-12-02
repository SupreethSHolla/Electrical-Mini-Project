const int sensorPin = 2;

void setup()
{
  Serial.begin(115200);
  pinMode(sensorPin, INPUT);
}

void loop()
{
  int sensorValue = digitalRead(sensorPin);

  if (sensorValue == LOW)
  {
    Serial.println("Object Detected!");
  }

  delay(200); // small delay for stability
}