import numpy as np
import soundfile as sf
import argparse
import os

def find_audio_file(extension):
    files = [f for f in os.listdir('.') if f.endswith(f'.{extension}') and extension not in ['aiff', 'aif']]
    if len(files) == 0:
        print(f"no se ha encontrado ningun archivo .{extension}")
        return None
    elif len(files) > 1:
        print(f"en este directorio hay mas de un .{extension}, especifica cual usar")
        return None
    return files[0]

#cambiar frecuencias aqui:
def shift_frequencies(input_file, output_file, min_freq=20000, max_freq=30000, target_min_freq=10000, target_max_freq=20000, mode='sum'):
    #cargar el archivo de sonido usando soundfile
    samples, sr = sf.read(input_file)

    #obtener la transformada de fourier
    D = np.fft.rfft(samples)
    freqs = np.fft.rfftfreq(samples.shape[-1], 1/sr)

    #filtrar las frecuencias en el rango especificado
    mask = (freqs >= min_freq) & (freqs <= max_freq)

    #aplicar el cambio de escala solo a las frecuencias filtradas
    if mode == 'sum':
        shifted_D = np.copy(D)  #copiar el espectro original para sumar
    elif mode == 'overwrite':
        shifted_D = np.zeros_like(D, dtype=complex)  #inicializar con ceros para sobrescribir
    else:
        raise ValueError("modo no valido. usa 'sum' o 'overwrite'.")

    for i, freq in enumerate(freqs):
        if mask[i]:
            #calcular el nuevo indice en el rango objetivo
            new_freq = target_min_freq + (target_max_freq - target_min_freq) * (freq - min_freq) / (max_freq - min_freq)
            new_idx = int(new_freq * len(D) / (sr / 2))
            if new_idx < len(D):
                if mode == 'sum':
                    shifted_D[new_idx] += D[i]  #sumar
                elif mode == 'overwrite':
                    shifted_D[new_idx] = D[i]  #sobrescribir

    #transformada inversa para obtener el audio modificado
    shifted_audio = np.fft.irfft(shifted_D)

    #guardar el resultado
    sf.write(output_file, shifted_audio, sr)

    print(f"Archivo guardado en: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="desplaza frecuencias de audio a un rango audible")
    parser.add_argument("--ext", type=str, required=True, help="extension del archivo de audio a procesar (ej: flac, wav, mp3...)")
    parser.add_argument("--mode", type=str, choices=['sum', 'overwrite'], default='sum', help="modo de procesamiento: 'sum' para sumar frecuencias, 'overwrite' para sobrescribir.")
    args = parser.parse_args()

    if args.ext in ['aiff', 'aif']:
        print("formato AIFF no compatible")
    else:
        input_file = find_audio_file(args.ext)
        if input_file:
            output_file = f"output.{args.ext}"
            shift_frequencies(input_file, output_file, mode=args.mode)
