import os
import cloudinary
import cloudinary.api
from dotenv import load_dotenv

load_dotenv()

# عرض القيم التي يقرأها البرنامج
print("CLOUDINARY_NAME:", os.getenv("CLOUDINARY_NAME"))
print("CLOUDINARY_API_KEY:", os.getenv("CLOUDINARY_API_KEY"))
print("CLOUDINARY_API_SECRET:", os.getenv("CLOUDINARY_API_SECRET"))

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

try:
    result = cloudinary.api.ping()
    print("✅ الاتصال ناجح مع Cloudinary!")
    print(result)
except Exception as e:
    print("❌ فشل الاتصال:")
    print(e)
