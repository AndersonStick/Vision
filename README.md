
# Vision

Ejercicios introductorios de visión artificial con Python, OpenCV, NumPy y
MediaPipe. El repositorio presenta una progresión práctica desde la captura de
video hasta la detección de puntos clave de las manos.

## Contenido

- Captura de video desde la cámara web.
- Dibujo de un cuadrado rojo sobre cada fotograma.
- Volteo horizontal y conversión a escala de grises con OpenCV.
- Conversión manual a escala de grises usando los canales BGR de la imagen.
- Detección de hasta dos manos mediante MediaPipe Hands.
- Visualización de las puntas de los cinco dedos detectadas por MediaPipe.

## Requisitos

- Windows con una cámara web disponible.
- Python 3.12 recomendado.
- PowerShell o una terminal compatible.

Las versiones de las dependencias están fijadas en
[`requirements.txt`](requirements.txt):

- `opencv-python==4.10.0.84`
- `numpy==1.26.4`
- `mediapipe==0.10.21`

## Instalación

Desde la raíz del repositorio, crea y activa un entorno virtual:

```powershell
python -m venv env
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\env\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

En cada nueva sesión de PowerShell, activa de nuevo el entorno:

```powershell
.\env\Scripts\Activate.ps1
```

## Ejecución

Los ejemplos se ejecutan individualmente desde la raíz del proyecto:

```powershell
python .\VisionProyectos\hello_world.py
python .\VisionProyectos\1_red_square.py
python .\VisionProyectos\2_first_filters.py
python .\VisionProyectos\3_black_and_white_filter.py
python .\VisionProyectos\4_hand_detection.py
```

Para cerrar cualquiera de las ventanas de video, pulsa la tecla `q`.

## Ejemplos

| Archivo | Descripción |
| --- | --- |
| `hello_world.py` | Abre la cámara y muestra el video sin modificaciones. |
| `1_red_square.py` | Coloca un cuadrado rojo de 100 x 100 píxeles en la esquina superior izquierda y muestra las dimensiones del fotograma. |
| `2_first_filters.py` | Aplica efecto espejo y convierte el fotograma a escala de grises con `cv2.cvtColor`. |
| `3_black_and_white_filter.py` | Calcula manualmente la escala de grises a partir de los canales BGR mediante una combinación ponderada. |
| `4_hand_detection.py` | Detecta manos con MediaPipe, marca las puntas de los dedos y las conecta con una polilínea. |

## Cómo funciona la detección de manos

`4_hand_detection.py` utiliza el modelo **MediaPipe Hands**. El modelo analiza
cada fotograma convertido de BGR a RGB y devuelve hasta 21 landmarks por mano.
El script usa los landmarks `4`, `8`, `12`, `16` y `20`, correspondientes a las
puntas del pulgar, índice, medio, anular y meñique.

Las coordenadas que devuelve MediaPipe están normalizadas. El programa las
transforma a píxeles usando el ancho y el alto del fotograma antes de dibujar
los círculos y la polilínea.

Este ejemplo **no utiliza detección de contornos** mediante
`cv2.findContours()`. La polilínea que aparece en pantalla únicamente conecta
los puntos detectados.

## Estructura

```text
Vision/
├── README.md
├── requirements.txt
└── VisionProyectos/
	├── hello_world.py
	├── 1_red_square.py
	├── 2_first_filters.py
	├── 3_black_and_white_filter.py
	└── 4_hand_detection.py
```

## Solución de problemas

### La cámara no se abre

- Comprueba que ninguna otra aplicación esté utilizando la cámara.
- Verifica los permisos de cámara de Windows para Python o tu terminal.
- Prueba otro índice en `cv2.VideoCapture(0)` si hay varias cámaras conectadas.

### MediaPipe no se puede instalar

Comprueba que el entorno virtual esté activo y que estés usando una versión de
Python compatible con la versión fijada en `requirements.txt`:

```powershell
python --version
python -m pip --version
```

### La ventana se cierra inmediatamente

Ejecuta el script desde PowerShell para poder leer el mensaje de error y
confirma que la cámara esté conectada antes de iniciarlo.

## Estado del proyecto

Repositorio educativo en desarrollo. Los scripts están pensados para estudiar
conceptos básicos y se ejecutan como programas independientes.
