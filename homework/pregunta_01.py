# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import glob
import pandas as pd # type: ignore


def cargar_y_procesar_archivos(ruta_base, tipo_sentimiento):
    datos = []
    patron_ruta = os.path.join(ruta_base, tipo_sentimiento, "*.txt")
    archivos = glob.glob(patron_ruta)

    for ruta_archivo in archivos:
        with open(ruta_archivo, "r") as f:
            frase = f.read()
            frase_limpia = frase.strip().replace('\n', ' ').replace('\r', ' ')
            frase_limpia = " ".join(frase_limpia.split())
            datos.append((frase_limpia, tipo_sentimiento))
    return datos

def crear_dataset_desde_directorio(ruta_directorio_base):
    todos_los_datos_frases = []
    sentimientos = ["positive", "negative", "neutral"]

    for sentimiento in sentimientos:
        frases_para_sentimiento = cargar_y_procesar_archivos(ruta_directorio_base, sentimiento)
        todos_los_datos_frases.extend(frases_para_sentimiento)

    dataframe = pd.DataFrame(todos_los_datos_frases, columns=["phrase", "target"])
    return dataframe

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```
    """
    ruta_base_entrenamiento = os.path.join("files", "input", "input", "train")
    ruta_base_prueba = os.path.join("files", "input", "input", "test")

    df_entrenamiento = crear_dataset_desde_directorio(ruta_base_entrenamiento)

    df_prueba = crear_dataset_desde_directorio(ruta_base_prueba)
    directorio_salida = os.path.join("files", "output")

    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    ruta_salida_entrenamiento = os.path.join(directorio_salida, "train_dataset.csv")
    ruta_salida_prueba = os.path.join(directorio_salida, "test_dataset.csv")

    df_entrenamiento.to_csv(ruta_salida_entrenamiento, index=False, sep=",")

    df_prueba.to_csv(ruta_salida_prueba, index=False, sep=",")
    