import gradio as gr

import cv2


def inference(image):

   img = cv2.imread(image.name)
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   return gray


# if __name__ == "__main__":
title = " Part of my PET project"
description = "One of my attempts to combine machine learning models and a web interface. Gredio as black magic prototype for visualization of the model is ready in a couple of hours."
git = "<p style='text-align: center'> <a href='https://github.com/MaksMaib/PETGgradio' target='_blank'>Github Repo</a></p>"


inputs = [gr.inputs.Image(type="file", label='image')]
output = gr.outputs.Image(type="pil")
iface = gr.Interface(inference, inputs, outputs=output, title=title, article=git,
                     description=description)
iface.launch()
