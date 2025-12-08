int ir1 = 2;
int ir2 = 3;

void setup()
{
    Serial.begin(9600);
    pinMode(ir1, INPUT);
    pinMode(ir2, INPUT);
}

void loop()
{
    int s1 = digitalRead(ir1);
    int s2 = digitalRead(ir2);

    // Your sensor outputs HIGH when object detected
    Serial.print("A:");
    Serial.print(s1 == HIGH ? 1 : 0);

    Serial.print(" B:");
    Serial.println(s2 == HIGH ? 1 : 0);

    delay(200);
}
