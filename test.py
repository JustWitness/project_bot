from pymongo import MongoClient
from PIL import Image
import io

host = "localhost"
port = 27017
client = MongoClient(host=host, port=port)

db = client["some_database"]
collection = db["some_collection"]

image = Image.open("C:\\All mine\\University\\7 семестр\\ТСПП\\python_bot\\image.jpg")
image_bytes = io.BytesIO()
image.save(image_bytes, format="JPEG")

im = {'data': image_bytes.getvalue()}

x = collection.insert_one(im)

client.close()
