# AudioShift

**AudioShift** es una herramienta de procesamiento de audio diseñada para desplazar frecuencias inaudibles a un rango audible. Esto permite a los usuarios escuchar sonidos que normalmente no podrían percibir, como frecuencias ultrasónicas o infrasónicas.

## Características

- **Desplazamiento de Frecuencias**: Mueve frecuencias específicas a un rango audible.
- **Modos de Procesamiento**: Permite sumar las frecuencias desplazadas a las existentes o sobrescribirlas.
- **Compatibilidad con Diversos Formatos**: Soporta múltiples formatos de archivos de audio, como `.flac`, `.wav`, `.mp3`, entre otros.

## Requisitos

- Python 3.x
- Bibliotecas de Python: `numpy`, `soundfile`

## Instalación

### Usando el Ejecutable (Recomendado)

1. **Descarga el Ejecutable**:
   - Descarga el archivo ejecutable desde la sección de [releases](#) del repositorio.

2. **Ejecuta el Programa**:
   - En Linux, asegúrate de que el archivo tenga permisos de ejecución:
     ```bash
     chmod +x AudioShift
     ```
   - Ejecuta el programa:
     ```bash
     ./AudioShift --ext flac --mode sum
     ```

### Usando el Código Fuente

1. **Clona el Repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/AudioShift.git
   cd AudioShift

Crea un Entorno Virtual (Opcional):

python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate  # En Windows


### Uso

    Argumentos:
        --ext: Especifica la extensión del archivo de audio a procesar (por ejemplo, flac, wav, mp3).
        --mode: Especifica el modo de procesamiento:
            sum: Suma las frecuencias desplazadas a las existentes.
            overwrite: Sobrescribe las frecuencias existentes con las desplazadas.

    Ejemplo:
    
    python AudioShift.py --ext flac --mode sum
