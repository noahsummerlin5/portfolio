// establish pins
const int echoPin = 3;
const int trigPin = 2;
const int fanPin = 10;
const int unarmedPin = 11;
const int armedPin = 12;
const int doingPin = 13;

// define states
// enum State {UNARMED, ARMED, DOING};
// State currentState = UNARMED;
enum State {UNARMED, ARMED, DOING};
enum Range {LOWER, NEAR, FULL};
State currentState = UNARMED;
Range currentRange = LOWER;

// variable creation
long duration;  // duration measured in microseconds (us)
float altitude; // altitude measured in cm

void setup() {
  // establish input and output pin
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(fanPin, OUTPUT);
  pinMode(unarmedPin, OUTPUT);
  pinMode(armedPin, OUTPUT);
  pinMode(doingPin, OUTPUT);
  Serial.begin(9600);
}

// altitude function
void readAltitude() {
  // set sensor off
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // set signal on for 10 us (8 bursts), then set off
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // time from initial pulse to detection with 38ms timeout (about 6.5m max range)
  duration = pulseIn(echoPin, HIGH, 38000); 

  // check if a valid reading was received
  if (duration > 0) {
    // altitude calculation
    altitude = (duration * 0.0343) / 2; // 0.0343 cm/us is approx. speed of sound
  }
}

void setUnarmed() {
    // set and print state
  currentState = UNARMED;
  Serial.println(currentState);
  digitalWrite(fanPin, LOW);

  // set LEDs
  digitalWrite(unarmedPin, HIGH);
  digitalWrite(armedPin, LOW);
  digitalWrite(doingPin, LOW);
}

void setArmed() {
    // set and print state
  currentState = ARMED;
  Serial.println(currentState);
  digitalWrite(fanPin, LOW);

  // set LEDs
  digitalWrite(unarmedPin, LOW);
  digitalWrite(armedPin, HIGH);
  digitalWrite(doingPin, LOW);
}

void setDoing() {
    // set and print state
  currentState = DOING;
  Serial.println(currentState);

  // set LEDs
  digitalWrite(unarmedPin, LOW);
  digitalWrite(armedPin, LOW);
  digitalWrite(doingPin, HIGH);
  delay(2000);

  int counter = 0; // dummy variable
  int increment = 100; // can be fine-tuned
  while (counter <= 500000) {
    doAltimeter();
    delay(increment);
    counter += increment;
  }
}

void setLower() {
  // set and print range
  currentRange = LOWER;
  Serial.println(currentRange);

  // *APPROXIMATION* to control propeller speed
  digitalWrite(fanPin, HIGH);
  delayMicroseconds(10000);
  digitalWrite(fanPin, LOW);
  delayMicroseconds(5);
}

void setNear() {
  // set and print range
  currentRange = NEAR;
  Serial.println(currentRange);

  // *APPROXIMATION* to control propeller speed
  digitalWrite(fanPin, HIGH);
  delayMicroseconds(80000);
  digitalWrite(fanPin, LOW);
  delayMicroseconds(5);
}

void setFull() {
  // set and print range
  currentRange = FULL;
  Serial.println(currentRange);

  // *APPROXIMATION* to control propeller speed
  digitalWrite(fanPin, HIGH);
  delayMicroseconds(5);
}

// check to change rotor speed
void checkAltitude() {
  if (altitude > 91.4) {
    setLower();
  }
  else if (altitude < 91.4 and altitude > 15.2) {
    setNear();
  }
  else {
    setFull();
  }
}

// altimeter function
void doAltimeter() {
  readAltitude();
  checkAltitude();
    
  // printing results on the serial
  Serial.print("Altitude: ");
  Serial.println(altitude, 1); // print with 1 decimal place
  }

// loop to demonstrate working order of each mode
void loop() {
  setUnarmed();
  delay(3000);

  setArmed();
  delay(3000);

  setDoing();
}