import gradio


def inference(foo, bar):
    print(f"Esto es foo: {foo}, y ésto es bar: {bar} ")
    return foo + bar


with gradio.Blocks() as main:
    input1 = gradio.Textbox()
    input2 = gradio.Textbox()
    output = gradio.Text()
    btn = gradio.Button("submit")
    js = '(x, y) => { console.log(8); return [y+1, y]; }'
    btn.click(inference, inputs=[input1, input2], outputs=output, js=js)

main.launch()