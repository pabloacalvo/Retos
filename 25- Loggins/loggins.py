import logging
import traceback
from pathlib import Path

print(f"##{logging.DEBUG = }")
print(f"##{logging.INFO = }")
print(f"##{logging.WARNING = }")
print(f"##{logging.ERROR = }")
print(f"##{logging.CRITICAL = }")

DEBUG = False
level = logging.DEBUG if DEBUG else logging.ERROR
root = Path(__file__).parent

logging.basicConfig(level=level, filename=f"{root}/error.log", format="%(asctime)s %(message)s")

def func_a():
    hello_world()

def hello_world():
    logging.debug("Se esta llamando a la funcion hello_world")
    dictionary = {
        "Hello":"World",
        "hello":""
    }
    1/0
    return dictionary["Hello"]

# result = func_a()

try:
    result = func_a()

except Exception as err:
    trace = traceback.format_exc()
    #logging.debug(f"{trace}")
    logging.error(f"Error: {err}")