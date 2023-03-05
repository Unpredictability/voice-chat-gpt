# Demo of using Whisper and GPT-3.5-Turbo API

This is a minimal demo repository showing how to use the newly released Whisper and GPT-3.5-Turbo API by OpenAI. The code allows users to input text via keyboard or microphone, display the chat in a neat dialogue frame, and clear chat history.

## Getting started

To use this code, you will need to change the API key in the `main.py` file first. You can obtain an API key from OpenAI's website.

Once you have obtained the API key, simply replace the placeholder text in `main.py` with your own API key.

## Usage

To run the code, navigate to the project directory and execute the following command:

```
python main.py
```

The code will launch a web server where you can enter your inputs via keyboard or microphone. The chat history will be displayed in a dialogue frame, and you can clear the chat history at any time. This code also use the `say` command on MacOS to read out the output.

## Dependencies

This code requires the following dependencies:

- gradio
- openai

Make sure you have installed these dependencies before running the code.

## Credits

If you find this code useful, please consider giving it a star on GitHub.