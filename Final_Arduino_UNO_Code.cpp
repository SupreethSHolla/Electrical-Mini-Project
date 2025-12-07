int ir = 2;

void setup()
{
    Serial.begin(9600);
    pinMode(ir, INPUT);
}

void loop()
{
    int value = digitalRead(ir);

    if (value == LOW)
    {
        Serial.println("NO Object Detected!");
    }
    else
    {
        Serial.println("Object Detected!");
    }

    delay(300);
}