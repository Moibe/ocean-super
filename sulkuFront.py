import globales
import sulkuPypi
import gradio as gr
import threading
import tools
import time

#import modulo_correspondiente
mensajes, sulkuMessages = tools.get_mensajes(globales.mensajes_lang)

result_from_displayTokens = None 
result_from_initAPI = None    

def displayTokens(request: gr.Request):
    
    global result_from_displayTokens
    
    novelty = sulkuPypi.getNovelty(sulkuPypi.encripta(request.username).decode("utf-8"), globales.aplicacion)    
    if novelty == "new_user": 
        display = gr.Textbox(visible=False)
    else: 
        tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"), globales.env)
        display = visualizar_creditos(tokens, request.username) 
    
    result_from_displayTokens = display

def displayUsos(browser_state):

    global result_from_displayTokens 

    print("Ésto es browserstate en la primera revisión: ", browser_state)
    time.sleep(1)

    if browser_state["usos"] == '': 
        #Si está vacio es que és el primer uso, y por lo tanto crearemos su carga con 10 usos.
        print("No existía, cargué 10...")
        display = {"usos": 10}
    else: 
        #Si ya existía, dejalo intacto.
        print("Si existía, lo dejé tal")
        display = browser_state

    print("Hice el IF correspondiente, ahora este es el browserstate que quedó: ")
    print(display)      

    result_from_displayTokens = display

def precarga(browser_state, request: gr.Request):

    # global result_from_initAPI
    # global result_from_displayTokens

    #thread1 = threading.Thread(target=initAPI)
    #thread2 = threading.Thread(target=displayTokens, args=(request,)) #Ésta es la precarga cuando se usa Sulku.
    thread2 = threading.Thread(target=displayUsos, args=(browser_state,))

    #thread1.start()
    thread2.start()

    #thread1.join()  # Espera a que el hilo 1 termine
    thread2.join()  # Espera a que el hilo 2 termine

    #return result_from_initAPI, result_from_displayTokens  
    return result_from_displayTokens 

def visualizar_creditos(nuevos_creditos, usuario):

    html_credits = f"""
    <div>
    <div style="text-align: left;">👤<b>{mensajes.lbl_username}: </b> {usuario}</div><div style="text-align: right;">💶<b>{mensajes.lbl_credits}: </b> {nuevos_creditos}</div>
    </div>
                    """    
     
    return html_credits

#Controla lo que se depliega en el frontend y que tiene que ver con llamados a Sulku.
def noCredit(usuario=None):
    info_window = sulkuMessages.out_of_credits
    path = 'images/no-credits.png'
    #tokens = 0
    #html_credits = visualizar_creditos(tokens, usuario) #Impotante no se usa si no hay auth.
    return info_window, path

def aError(excepcion, usuario=None, tokens=None):
    #aError se usa para llenar todos los elementos visuales en el front.
    info_window = manejadorExcepciones(excepcion)
    path = 'images/error.png'
    #html_credits = visualizar_creditos(tokens, usuario)  #Ya no se trabajará con html_credits cuando no hay auth. 
    return info_window, path

def manejadorExcepciones(excepcion):
    #El parámetro que recibe es el texto despliega ante determinada excepción:
    if excepcion == "PAUSED": 
        info_window = sulkuMessages.PAUSED
    elif excepcion == "RUNTIME_ERROR":
        info_window = sulkuMessages.RUNTIME_ERROR
    elif excepcion == "STARTING":
        info_window = sulkuMessages.STARTING
    elif excepcion == "HANDSHAKE_ERROR":
        info_window = sulkuMessages.HANDSHAKE_ERROR
    elif excepcion == "GENERAL":
        info_window = sulkuMessages.GENERAL
    elif excepcion == "NO_FACE":
        info_window = sulkuMessages.NO_FACE
    elif excepcion == "NO_FILE":
        info_window = sulkuMessages.NO_FILE
    elif excepcion == "NO_POSITION": #Solo aplíca para Splashmix.
        info_window = sulkuMessages.NO_POSITION
    elif "quota" in excepcion: #Caso especial porque el texto cambiará citando la cuota.
        info_window = excepcion
    else:
        info_window = sulkuMessages.ELSE

    return info_window

def presentacionFinal(usuario, accion):
        
    capsule = sulkuPypi.encripta(usuario).decode("utf-8") #decode es para quitarle el 'b
    
    if accion == "debita":        
        tokens = sulkuPypi.debitTokens(capsule, globales.work, globales.env)
        info_window = sulkuMessages.result_ok        
    else: 
        info_window = "No face in source path detected."
        tokens = sulkuPypi.getTokens(capsule, globales.env)
    
    html_credits = visualizar_creditos(tokens, usuario)       
    
    return html_credits, info_window

def presentacionFinalUsos(browser_state, accion):        
    
    if accion == "debita":        
        usos_actuales = browser_state["usos"]
        usos_updated = usos_actuales - 1
        browser_state["usos"] = usos_updated
        info_window = sulkuMessages.result_ok        
    else: 
        info_window = "No face in source path detected."  
    
    return browser_state, info_window