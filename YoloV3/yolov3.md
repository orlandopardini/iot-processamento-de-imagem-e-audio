# YOLOv3: Detecção de Objetos com Webcam e Imagens Locais

Este projeto realiza **detecção de objetos em tempo real** utilizando a rede YOLOv3 e a biblioteca OpenCV, com suporte tanto para **captura de imagem via webcam** quanto para **seleção de arquivos locais** com interface gráfica.

## Requisitos

Instale as dependências com:

```bash
pip install opencv-python matplotlib numpy tk

.
├── arquivos_base/
│   ├── yolov3.cfg
│   ├── yolov3.weights
│   └── coco.names
├── seu_script.py
