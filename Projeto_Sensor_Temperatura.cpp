int pinTMP = A0; // pino do sensor TMP36
int pinAzul = 9; // LED azul
int pinVerde = 10; // LED verde
int pinVermelho = 8; // LED vermelho

void setup()
{
  pinMode(pinAzul, OUTPUT); // configura LED azul
  pinMode(pinVerde, OUTPUT); // configura LED verde
  pinMode(pinVermelho, OUTPUT); // configura LED vermelho
  Serial.begin(9600); // habilita monitor serial
}

void loop()
{
  int leitura = analogRead(pinTMP); // leitura bruta do sensor
  float tensao = leitura * 5.0 / 1023.0; // converte para tensão
  float temperatura = (tensao - 0.5) * 100.0; // calcula temperatura em °C

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C");

  if (temperatura <= 20)
  {
    digitalWrite(pinAzul, HIGH);
    digitalWrite(pinVerde, LOW);
    digitalWrite(pinVermelho, LOW);
  }
  else if (temperatura > 20 && temperatura <= 30)
  {
    digitalWrite(pinAzul, LOW);
    digitalWrite(pinVerde, HIGH);
    digitalWrite(pinVermelho, LOW);
  }
  else
  {
    digitalWrite(pinAzul, LOW);
    digitalWrite(pinVerde, LOW);
    digitalWrite(pinVermelho, HIGH);
  }

  delay(1000); // intervalo de leitura
}
