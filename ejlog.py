import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if len(sys.argv) == 2:
    if sys.argv[1] == '-v':
        logger.setLevel(logging.DEBUG)
    elif sys.argv[1] == '-q':
        logger.setLevel(logging.ERROR)

logger_complicado = logging.getLogger("paq1.zaraza")
logger_complicado.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(levelname)-5s %(message)s")

handler = logging.FileHandler("ejemplo.log")
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("Linea de debug")
aa = 123.8712638716584
bb = "cadena"
logger.info("Sucedio que recibi %r y tuve valor %.2f%%", bb, aa)
logger.error("Linea de error")
try:
    1 / 0
except:
    # algo para arreglar
    logger.exception("Mensaje")
    print("(sigue andando)")

