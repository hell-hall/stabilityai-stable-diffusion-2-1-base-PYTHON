# -- PACKAGES --
import requests
import io
from PIL import Image
# -- TOKEN SET -- If you do not have one already go to huggingface.com and get a token --
# -- Place your token within the quotes EXAMPLE: TOKEN = "MY TOKEN HERE" --

TOKEN = ""

# -- SET API INFO --
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1-base"
headers = {"Authorization": f"Bearer {TOKEN}"}

# -- ASK USER WHAT THEY WANT DRAWN --
def promt():
    try:
        prompt = input("Enter your prompt or type help:")
        return prompt
    except Exception as error:
        print(error)

def save():
    try:
        image_name = input("What would you like your image to be named (requires name):") + ".jpg"
        return image_name
    except Exception as error:
        print(error)

# -- CHECK IF THE USER ENTERS INPUT FOR BOTH PROMPT AND image_name --
def check_input():
    if user_prompt == '':
        print("!!Please enter an input!!")

# -- RUN REQUEST AND RETURN IMAGE --
def run(prompt, save_path):
    try:
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content

        image_bytes = query({
            "inputs": prompt,
        })

        # -- DOWNLOAD THE IMAGE --
        image = Image.open(io.BytesIO(image_bytes))
        image.save(save_path)  # -- SAVE THE IMAGE --
        print(f"Image generated and saved to {save_path}")
    except Exception as error:
        print(error)
while True:
    try:
        # -- CALL THE PROMPT FUNCTION --
        user_prompt = promt()

        # -- CALL THE IMAGE SAVE FUNCTION --
        save_image = save()

        # -- CREATE SAVE PATH TO IMAGE --
        save_path = f'YOUR IMAGES/{save_image}'

        run(user_prompt, save_path)
    except Exception as error:
        print(error)
