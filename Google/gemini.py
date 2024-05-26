from google.colab import userdata
userdata.get('GOOGLE_API_KEY')
import google.generativeai as genai
import PIL.Image
# para gestionar las imagenes usamos Pillow. Si estás replicando este cuaderno en tu propio ambiente deberás instalar esta librería. Usa pip install Pillow

img = PIL.Image.open('corgi-en-patineta.jpg')
img
## Cambiamos el modelo a Gemini Pro Vision
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)
to_markdown(response.text)
response = model.generate_content([
    "¿Por qué se conoce el animal de esta foto? ¿Se asocia a algún país en particular?"
    , img], stream=True)
response.resolve()

to_markdown(response.text)