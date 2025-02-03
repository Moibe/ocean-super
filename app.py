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

# js_open = """
# //Se ejecuta cuando carga la página.
# function ejecuta() {
#     //alert("Hola");
#     console.log("Hola consola");
    
#     // Verificar si la clave 'usos' ya existe y obtener su valor
#     let usos = localStorage.getItem('usos');

#     // Si no existe, creamos la clave con el valor inicial
#     if (!usos) {
#     usos = 10;
#     localStorage.setItem('usos', usos);
#     }

#     // En este punto, la variable 'usos' siempre tendrá un valor,
#     // ya sea el valor inicial de 10 o el valor que estaba almacenado.    
#     console.log("Número de usos vigentes:", usos);
    
#     //Obtenemos el lugar de donde pondrémos esa info. 
#     impresion = document.querySelector('.prose');
#     //Y guardaremos ahí el valor e cuantos usos le quedan.
#     impresion.innerText = usos;
#     console.log("Usos guardados en gradio.");

#     return "Retorna esto"
    
#     }      
# """

# js_close = """
# //Se ejecuta cuando cambia la ventana de result.

# function ejecuta2() {
#     console.log("Adiós consola");

#     //Toma el valor que reside en lbl_usos:
#     impresion = document.querySelector('.prose');
#     //Restale un uso
#     usos = impresion.innerText
#     usos = usos - 1 
#     impresion.innerText = usos 
    
#     }   
# """

def actualizaBrowserState(browser_state): 

    print("Entré a actualiza browser state...", browser_state)    
         
    usos_actuales = browser_state["usos"]
    usos_updated = usos_actuales - 1
    browser_state["usos"] = usos_updated        
    
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