import logging

# Configurar el nivel de registro deseado (por ejemplo, INFO)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Obtener el logger de la aplicación
logger = logging.getLogger(__name__)

# Crear un manejador para imprimir en la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Agregar el manejador a nuestro logger
logger.addHandler(console_handler)