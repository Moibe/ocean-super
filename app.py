import inputs
import globales
import funciones
import sulkuFront
#import autorizador
import gradio as gr
import time

def iniciar():    
    app_path = globales.app_path
    main.queue(max_size=globales.max_size)
    main.launch(root_path=app_path, server_port=globales.server_port)

#Credit Related Elements
html_credits = gr.HTML(visible=True)
lbl_console = gr.Label(label="AI Terminal " + globales.version +  " messages", value="", container=True)
btn_buy = gr.Button("Get Credits", visible=False, size='lg')

#Customizable Inputs and Outputs
input1, gender, result = inputs.inputs_selector(globales.seto)  
#Otros Controles y Personalizaciones

nombre_posicion = gr.Label(label="Posicion") #Ponle visible false para producción para no mover todo lo demás.

def actualizaBrowserState(browser_state):      
         
    usos_actuales = browser_state["usos"]
    usos_updated = usos_actuales - 1
    browser_state["usos"] = usos_updated  

    print(f"Tenía {usos_actuales} usos, ahora tiene: {usos_updated}")      
    
    return browser_state

#Declaramos BrowserState: 
browser_state = gr.BrowserState({ 
    "usos": "",
    }) 

with gr.Blocks(theme=globales.tema, css="footer {visibility: hidden}") as main:      
    
    #Cargado en Load: Función, input, output
    main.load(sulkuFront.precarga, browser_state, browser_state) #Importante: Cuando no usa auth, carga los usos no los credits.
    
    with gr.Row():
        demo = gr.Interface(
            fn=funciones.perform,
            inputs=[browser_state, input1, gender], 
            outputs=[result, lbl_console, btn_buy, nombre_posicion], 
            flagging_mode=globales.flag
            )
    
    result.change(actualizaBrowserState, browser_state, browser_state) 

iniciar()