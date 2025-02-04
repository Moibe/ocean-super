js_open = """
//Se ejecuta cuando carga la página.
function ejecuta() {
    //alert("Hola");
    console.log("Hola consola");
    
    // Verificar si la clave 'usos' ya existe y obtener su valor
    let usos = localStorage.getItem('usos');

    // Si no existe, creamos la clave con el valor inicial
    if (!usos) {
    usos = 10;
    localStorage.setItem('usos', usos);
    }

    // En este punto, la variable 'usos' siempre tendrá un valor,
    // ya sea el valor inicial de 10 o el valor que estaba almacenado.    
    console.log("Número de usos vigentes:", usos);
    
    //Obtenemos el lugar de donde pondrémos esa info. 
    impresion = document.querySelector('.prose');
    //Y guardaremos ahí el valor e cuantos usos le quedan.
    impresion.innerText = usos;
    console.log("Usos guardados en gradio.");

    return "Retorna esto"
    
    }      
"""

js_close = """
//Se ejecuta cuando cambia la ventana de result.

function ejecuta2() {
    console.log("Adiós consola");

    //Toma el valor que reside en lbl_usos:
    impresion = document.querySelector('.prose');
    //Restale un uso
    usos = impresion.innerText
    usos = usos - 1 
    impresion.innerText = usos 
    
    }   
"""