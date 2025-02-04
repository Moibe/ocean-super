import gradio as gr

nombre_diccionario = "datos_superheroe"

#MAIN
version = "0.0.0"
env = "prod"
aplicacion = "super" #como se llama en tu repo y tu dominio.

seleccion_api = "eligeQuotaOCosto" #eligeQuotaOCosto , eligeAOB o eligeGratisOCosto
max_size = 20
#Quota o Costo
api_zero = ("Moibe/InstantID2", "quota")
api_cost = ("Moibe/InstantID2-B", "costo")

interface_api_name = "/generate_image" #El endpoint al que llamará client.


process_cost = 30

seto = "splashmix"
work = "picswap"
app_path = "/super"
server_port=7889
tema = gr.themes.Default()
flag = "auto"

neural_wait = 6
mensajes_lang = "en"
