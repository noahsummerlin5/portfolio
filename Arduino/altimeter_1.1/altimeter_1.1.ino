// establish pins
const int echoPin = 2;
const int trigPin = 3;

// variable creation
long duration;  // duration measured in microseconds (us)
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

  // set signal on for 10 us (8 bursts), then set off
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // time from initial pulse to detection with limited timeout to avoid null readings
  duration = pulseIn(echoPin, HIGH, 38000); 

  // check if a valid reading was received
  if (duration > 0) {
    // distance calculation
    distance = (duration * 0.0343) / 2; // 0.0343 cm/us is approx. speed of sound

    // printing results on the serial
    Serial.print("Distance: ");
    Serial.println(distance, 1); // print with 1 decimal place
  }
}