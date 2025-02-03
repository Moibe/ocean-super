import gradio as gr

def carga_preferencias(browser_state):
  print("loading from local storage", browser_state)
  
  return browser_state["theme"], browser_state["font_size"]

def save_preferences(theme, font_size): 
        return {
            "theme": theme,
            "font_size": font_size,
            }

with gr.Blocks() as main:
  nota_tema = gr.Textbox(label="Tema")
  nota_font = gr.Textbox(label="Font")
  resultado_tema = gr.Textbox(label="Resultado Tema")
  resultado_font = gr.Textbox(label="Resultado Font")
  
  browser_state = gr.BrowserState({ 
        "theme": "",
        "font_size": "",})
  
  main.load(carga_preferencias, inputs=[browser_state], outputs=[resultado_tema, resultado_font])

  demo = gr.Interface(
            fn=save_preferences,
            inputs=[nota_tema, nota_font],
            outputs=browser_state, 
            flagging_mode='never'
            )

main.launch()