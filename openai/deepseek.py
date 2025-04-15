
#Se reemplaza por openrouter que es gratuito
from openai import OpenAI

client = OpenAI(api_key="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", base_url="https://openrouter.ai/api/v1")

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