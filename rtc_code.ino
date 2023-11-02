#include <Wire.h>
#include <ds3231.h>

struct ts t;
int onHour = 18;   // User-defined turn-on hour
int onMinute = 14; // User-defined turn-on minute
int offHour = 18; // User-defined turn-off hour
int offMinute = 16; // User-defined turn-off minute

void setup() {
  Serial.begin(9600);
  Wire.begin();
  DS3231_init(DS3231_CONTROL_INTCN);
pinMode(D7,OUTPUT);
digitalWrite(D7,HIGH);
  // Set the initial time
  t.hour = 18;
  t.min = 12;
  t.sec = 0;
  t.mday = 30;
  t.mon = 10;
  t.year = 2023;
  DS3231_set(t);
}

void loop() {

  // Read the current time from the RTC
  DS3231_get(&t);

  // Check if it's time to turn on the RTC
  if (t.hour == onHour && t.min == onMinute) {
    Serial.println("RTC turned ON");
    
digitalWrite(D7,LOW);
  }

  // Check if it's time to turn off the RTC
  if (t.hour == offHour && t.min == offMinute) {
    Serial.println("RTC turned OFF");
    
digitalWrite(D7,HIGH);
  }

  // Display the current time
  Serial.print("Date : ");
  Serial.print(t.mday);
  Serial.print("/");
  Serial.print(t.mon);
  Serial.print("/");
  Serial.print(t.year);
  Serial.print("\t Hour : ");
  Serial.print(t.hour);
  Serial.print(":");
  Serial.print(t.min);
  Serial.print(".");
  Serial.println(t.sec);

  delay(1000);
}
