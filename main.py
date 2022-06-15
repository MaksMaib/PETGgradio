
import gradio as gr
import model
def inference(content, style):
    result = model.main(style.name, content.name)

    return result


title = " Part of my PET project"
description = "One of my attempts to combine machine learning models and a web interface. Gredio as black magic prototype for visualization of the model is ready in a couple of hours."
git = "<a href='https://github.com/PaddlePaddle/PaddleHub' target='_blank'>Github Repo</a></p>"
examples = [
    ['style_example/picasso-old.jpg', 'style_example/picasso.jpg'],
    ['style_example/Lesya.jpg', 'style_example/forest.jpg'],
    ['style_example/picasso-old.jpg', 'style_example/Picasso_Painting.jpg'],
    ]


inputs = [gr.inputs.Image(type="file", label='content'), gr.inputs.Image(type="file", label='style')]
output = gr.outputs.Image(type="pil")
iface = gr.Interface(inference, inputs, outputs=output, title=title, article=git,
                     description=description, examples=examples)
iface.launch()
