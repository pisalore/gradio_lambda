import gradio as gr
from transformers import pipeline

# load transformers pipeline from a local directory (model)
clf = pipeline("sentiment-analysis", model="model/")


# predict function used by gradio
def sentiment(payload):
    prediction = clf(payload, return_all_scores=True)
    # convert list to dict
    result = {}
    for pred in prediction[0]:
        result[pred["label"]] = pred["score"]
    return result


# create gradio interface, with text input and dict output
demo = gr.Interface(
    fn=sentiment,
    inputs=gr.Textbox(placeholder="Enter a positive or negative sentence here..."),
    outputs="label",
    interpretation="default",
    examples=[["I Love Serverless Machine Learning"], ["Running Gradio on AWS Lambda is amazing"]],
    allow_flagging="never",
)

# run the app
demo.launch(server_port=8080, enable_queue=False)
