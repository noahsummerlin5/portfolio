// establish pins
const int echoPin = 2;
const int trigPin = 3;

// variable creation
long duration; // duration measured in microseconds (us)
float distance; // distance measured in cm

void setup() {
  // establish input and output pin
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // set sensor off
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // set signal on for 10 us (8 bursts), set off
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // time from initial pulse to detection
  duration = pulseIn(echoPin, HIGH); // ERROR - takes longer than expected to reset

  // distance calculation
  distance = (duration * 0.0343) / 2; // 0.0343 cm/us is approximately the speed of sound

  // printing results on the serial
  Serial.print("Distance: ");
  Serial.println(distance, 1); // ERROR - prints additional "0.0" value
}