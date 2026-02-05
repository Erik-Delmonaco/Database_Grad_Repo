import gradio as gr

def f(x,y):
    return x+y

with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            xbox = gr.Number(label = "Type in a number")
            sumbox = gr.Number(label = "This is the sum of these numbers")
        with gr.Column():
            ybox = gr.Number(label = "Type in another number")

    xbox.change(fn = f, inputs = [xbox, ybox], outputs = [sumbox])
    ybox.change(fn = f, inputs = [xbox, ybox], outputs = [sumbox])

iface.launch()