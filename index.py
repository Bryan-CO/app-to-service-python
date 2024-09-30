import os
import shutil
import subprocess
import platform


# Nombre de la carpeta a crear
FOLDER_NAME = "pumpDemon"

FOLDER_ORIGIN = os.path.dirname(__file__)

# Ruta del archivo origen
FILE_ORIGIN = os.path.join(FOLDER_ORIGIN, 'pump-demon.exe')

# Ruta del Program Files
PF_FOLDER = os.environ["ProgramFiles"]

# Ruta destino con la nueva carpeta
NEW_FOLDER = os.path.join(PF_FOLDER, FOLDER_NAME)

# Ruta destino con el nombre del archivo
NEW_FILE = os.path.join(NEW_FOLDER, 'pump-demon.exe')

# Mi arquitectura
ARCHITECTURE = platform.architecture()[0][0:2]

def createFolder():
    os.makedirs(NEW_FOLDER, exist_ok=True)
    print(f"Carpeta creada en {NEW_FOLDER}")


def copyFile():
    shutil.copy(FILE_ORIGIN, NEW_FOLDER)
    print(f"Archivo copiado con éxito!")


def createService():
    print('Creando el servicio...')
    os.chdir(os.path.join(FOLDER_ORIGIN, 'nssm'))
    os.chdir('win64' if ARCHITECTURE == '64' else 'win32') # Watefok con la operacion ternaria de python
    print(NEW_FILE)
    subprocess.run(f'nssm install pumpDemon "{NEW_FILE}"', shell=True)
    subprocess.run('nssm set pumpDemon Start SERVICE_AUTO_START', shell=True)


def initializeService():
    print("Iniciando servicio....")
    subprocess.run('nssm start pumpDemon', shell=True)

try:
    createFolder()
    copyFile()
    createService()
    initializeService()
except Exception as e:
    print(f"Ocurrió un error :( = {e}")
    input()