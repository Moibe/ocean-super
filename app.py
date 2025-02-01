import inputs
import globales
import funciones
import sulkuFront
import autorizador
import gradio as gr

def iniciar():    
    app_path = globales.app_path
    main.queue(max_size=globales.max_size)
    main.launch(auth=autorizador.authenticate, root_path=app_path, server_port=globales.server_port)

#Credit Related Elements
print("Imprimiendo credit related items...")
lbl_usos = gr.Label(value="1", visible=True)
html_credits = gr.HTML(visible=True)
lbl_console = gr.Label(label="AI Terminal " + globales.version +  " messages", value="", container=True)
btn_buy = gr.Button("Get Credits", visible=False, size='lg')


#Customizable Inputs and Outputs
input1, gender, result = inputs.inputs_selector(globales.seto)  
#Otros Controles y Personalizaciones

nombre_posicion = gr.Label(label="Posicion") #Ponle visible false para producción para no mover todo lo demás.

js = """
    function ejecuta() {
    alert("Hola");
    console.log("Hola consola");
    
    // Verificar si la clave 'usos' ya existe y obtener su valor
    let usos = localStorage.getItem('usos');

    // Si no existe, creamos la clave con el valor inicial
    if (!usos) {
    usos = 10;
    localStorage.setItem('usos', usos);
    }

    // En este punto, la variable 'usos' siempre tendrá un valor,
    // ya sea el valor inicial de 10 o el valor que estaba almacenado
    
    console.log("Número de usos vigentes:", usos);
    
    impresion = document.querySelector('.output-class');
    impresion.innerText = usos;
    console.log("Usos guardados en gradio.");
    
    }   
"""

js_adios2 = """
function ejecuta2() {
    alert("Adiós");
    console.log("Adiós consola");
    
    }   
"""
def welcome():
    #raise gr.Error("Entré a Welcome!")
    return f"Welcome to Gradio!"

with gr.Blocks(theme=globales.tema, js=js, css="footer {visibility: hidden}") as main:   
    #Cargado en Load: Función, input, output
    main.load(sulkuFront.precarga, None, html_credits) 
    #js = '(x, y, z) => { console.log(88); return [x, y, z]; }'
    #js_adios = 'function ejecuta2() { console.log(88); }'
       
    with gr.Row():
        demo = gr.Interface(
            fn=funciones.perform,
            inputs=[lbl_usos, input1, gender], 
            outputs=[result, lbl_console, html_credits, btn_buy, nombre_posicion], 
            flagging_mode=globales.flag
            )
    
    result.change(welcome, None, None, js=js_adios2) 

iniciar()