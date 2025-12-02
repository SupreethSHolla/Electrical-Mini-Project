const int sensorPin = 2;
int lastState = HIGH;
int count = 0;
const int debounceMs = 100;
unsigned long lastTime = 0;

void setup()
{
    Serial.begin(115200);
    pinMode(sensorPin, INPUT);
}

void loop()
{
    int current = digitalRead(sensorPin);
    unsigned long now = millis();

    if (current == LOW && lastState == HIGH && (now - lastTime) > debounceMs)
    {
        count++;
        Serial.print("Object Detected! Total Count: ");
        Serial.println(count);

        lastTime = now;
    }

    lastState = current;
}