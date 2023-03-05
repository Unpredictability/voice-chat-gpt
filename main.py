import gradio as gr
import openai
import subprocess

openai.api_key = "put your key here"

DEFAULT = [
    {
        "role": "system", "content":
        """
        I want you to act like Sherlock Holmes from Elementary. I want you to respond and answer like Sherlock using his brilliant, eccentric, and unconventional tone, manner and vocabulary. You should be knowledgeable of crime-solving techniques, forensic science, deductive reasoning, and various fields of expertise that Sherlock often employs or references in his investigations with his partner Dr. Joan Watson. You should also be aware of Sherlock’s personal struggles, relationships, and backstory. Do not write explanations or additional information in your response, simply provide the dialogue as Sherlock would say it.
        """
    }
]

msg_history = DEFAULT.copy()


def append_input(user_input):
    msg_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )


def clear_msg_history():
    global msg_history
    msg_history = DEFAULT.copy()
    print("cleared")
    print(msg_history)


def get_gpt_res():
    global msg_history
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg_history
    )
    msg_history.append(
        res["choices"][0]["message"]
    )
    pure_text = res["choices"][0]["message"]["content"]
    subprocess.run(["say", pure_text])
    return pure_text


def transcribe(audio):
    f = open(audio, "rb")
    trans_text = openai.Audio.transcribe("whisper-1", f)["text"]
    return trans_text


def respond(chat_history, message):
    append_input(message)
    response = get_gpt_res()
    return chat_history + [[message, response]]


def au_respond(chat_history, audio_path):
    ret = chat_history
    if audio_path != None:
        msg = transcribe(audio_path)
        append_input(msg)
        response = get_gpt_res()
        ret = chat_history + [[msg, response]]
    return [ret, None]


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")
    audio = gr.Audio(source="microphone", type="filepath")

    msg.submit(respond, [chatbot, msg], chatbot)
    audio.change(au_respond, [chatbot, audio], [chatbot, audio])
    clear.click(clear_msg_history, None, chatbot, queue=False)

demo.launch(share=True, show_api=False)