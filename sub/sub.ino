int led_pin = 13;
int state = -1;

int get_state(int state)
{
  if (Serial.available() > 0)
  {
    char c = Serial.read();
    if (c == 'z')
    {
      state = 0;
    }
    else if (c == 'c')
    {
      state = 1;
    }
    else if (c == 'x')
    {
      state = 2;
    }
  }
  return state;
}

void switch_led_state(int state)
{
  if (state == 0)
  {
    digitalWrite(led_pin, state); 
  }
  else if (state == 1)
  {
    digitalWrite(led_pin, state);
  }
  else if (state == 2)
  {
    digitalWrite(led_pin, HIGH);
    delay(500);
    digitalWrite(led_pin, LOW);
  }
  return;
}

void setup() {
  Serial.begin(9600);
  pinMode(led_pin, OUTPUT);
}

void loop() {
  state = get_state(state);
  switch_led_state(state);
  delay(100);
}
