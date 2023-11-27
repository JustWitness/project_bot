from pymongo import MongoClient
from PIL import Image
import io
import matplotlib.pyplot as plt

host = "localhost"
port = 27017
client = MongoClient(host=host, port=port)
db = client["some_database"]
collection = db["some_collection"]

image = collection.find_one()

pil_img = Image.open(io.BytesIO(image['photo_bytes']))
pil_img.save("C:\\All mine\\University\\7 семестр\\ТСПП\\python_bot\\saved_image.jpg")
