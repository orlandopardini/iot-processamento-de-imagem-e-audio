#  IoT - Processamento de Imagem e Áudio

Este repositório reúne três aplicações que exploram técnicas de IoT utilizando sensores físicos, visão computacional e comandos por voz. Os projetos demonstram como integrar hardware, inteligência artificial e automação.

##  Estrutura do Repositório

###  Sensor_Temperatura_Arduino
Projeto com Arduino que utiliza o sensor TMP36 para medir temperatura ambiente. A temperatura é representada por LEDs coloridos de acordo com a faixa térmica (azul, verde, vermelho).

###  YoloV3
Detecção de objetos com o modelo YOLOv3 em imagens e webcam. Implementado com OpenCV e suporte a múltiplas classes com bounding boxes coloridas e probabilidades.

###  automacao_por_audio
Automação de tarefas no Windows por comandos de voz usando `speech_recognition` com microfone. Reconhece comandos como “abrir navegador”, “Excel”, “YouTube” e outros.

##  Requisitos

- Python 3.8+
- OpenCV
- SpeechRecognition
- PyAudio
- imutils
- Arduino IDE (para o sensor de temperatura)
