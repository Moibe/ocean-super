import splashmix.configuracion
#POR EL MOMENTO SOLO SE ESTÁ USANDO promteador, los demás vienen de splashmix-batcher.

def prompteador(objeto, nombre_diccionario):
    datos = getattr(splashmix.configuracion, nombre_diccionario)
    creacion_seleccionada = datos["creacion"]
 
    if creacion_seleccionada == "Superhero": 
        #PROMPT PARA HEROE
        prompt = f"A {objeto.style} of a superhero like {objeto.subject} " #agregar otros atributos random aquí posteriormente.
        print(prompt)
    
    elif creacion_seleccionada == "Superheroine": 
        #PROMPT PARA HEROE
        prompt = f"A {objeto.style} of a superheroine like {objeto.subject} " #agregar otros atributos random aquí posteriormente.
        print(prompt)
    
    else:        
        prompt = f"""A {objeto.style} of a {objeto.adjective} {objeto.type_girl} {objeto.subject} with {objeto.boobs} and {objeto.hair_style} wearing {objeto.wardrobe_top}, 
                {objeto.wardrobe_accesories}, {objeto.wardrobe_bottom}, {objeto.wardrobe_shoes}, {objeto.situacion} at {objeto.place} {objeto.complemento}"""   
        print(prompt)      
    return prompt