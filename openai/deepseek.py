
#Se reemplaza por openrouter que es gratuito
from openai import OpenAI

client = OpenAI(api_key= ${{ secrets.openrouter_key }}, base_url="https://openrouter.ai/api/v1")

print ("Bienvenido a DeepSeek cli")
print("Por favor ingrese su busqueda")
palabra = str(input())

chat = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
        {
        "role":"user",
        "content":palabra
        }
    ]
)

print(chat.choices[0].message.content)
