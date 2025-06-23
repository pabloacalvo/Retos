from pymongo import MongoClient
import base64
from pathlib import Path
from PIL import Image
import io
from datetime import date
import matplotlib.pyplot as plt

class ImageDAO:
    def __init__(self, host='localhost', port=27017, db_name='ticket_safe', collection_name='project1'):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def close_connection(self):
        self.client.close()

    def encode_image_to_base64(self, image_path: Path) -> str:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def decode_image_from_base64(self, base64_str: str) -> bytes:
        return base64.b64decode(base64_str)

    def insert(self, name: str, image_path: Path,total_amount:float):
        image_base64 = self.encode_image_to_base64(image_path)
        ticket_date = date.today().strftime("%d-%m-%Y")
        document = {
            "store_name": name,
            "date":ticket_date,
            "total_amount":total_amount,
            "imagen_base64": image_base64
        }
        try:
            if not self.is_exist(name,ticket_date,image_base64):
                self.collection.insert_one(document)
                print(f"Documento insertado con exito")
            else:
                print("No se inserto el documento, porque ya existe")
        except Exception as e:
            print("Error al insertar:{e}")

    def is_exist(self,name,ticket_date,image_base64):
        exist = self.collection.find_one({
        "store_name": name,
        "date":ticket_date,
        "imagen_base64": image_base64
        })
        if exist:
            return True
        return False

    def find_by_name(self, name: str):
        return self.collection.find({"store_name": name})

    def show_image_from_bytes(self, image_bytes: bytes):
        try:
            image = Image.open(io.BytesIO(image_bytes))
            plt.imshow(image)
            plt.axis('off')  # Oculta los ejes
            plt.show()
        except Exception as e:
            print(f"Error displaying image: {e}")


# === Main Execution ===

def main():
    image_path = Path(__file__).parent / "imagen1.jpg"
    dao = ImageDAO()

    try:
        # Insert image (descomentar si querés insertar)
        dao.insert(name="Starbucks", image_path=image_path,total_amount=100.50)

        # Find and show image
        results = dao.find_by_name("Starbucks")
        for doc in results:
            image_bytes = dao.decode_image_from_base64(doc['imagen_base64'])
            dao.show_image_from_bytes(image_bytes)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        dao.close_connection()
        print("Connection closed")


if __name__ == "__main__":
    main()

