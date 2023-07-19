# GPT-4 Chatbot README

## Overview

This script uses OpenAI's GPT-4 model to generate a response based on a text prompt inputted from a file. It includes a loading animation while waiting for the API to return the response. After the response is generated, the conversation is saved to a markdown file on the user's desktop.

## Requirements

- Python 3.6 or later
- openai-python package

## Setup

1. Install the necessary Python package with pip:
   ```
   pip3 install openai
   ```
2. Clone or download this repository to your local machine.

3. Replace the `<API key>` string with your OpenAI API key in the line `openai.api_key = "<API key>"`.

4. Replace the `<path_to_your_prompt_file>` string with the path to your .txt file containing the prompt for the chatbot in the line `prompt_file_path = "<path_to_your_prompt_file>"`.

## How to Run

Run the script using Python from the command line:

```
python3 chattytxt.py
```

The chatbot will generate a response to the prompt in your .txt file, display the response in the console, and save the conversation to a markdown file on your desktop.

The name of the output file will be in the format `chat_output_<current_time>.md`, where `<current_time>` is the current date and time in the format `YYYY-MM-DD_HH-MM-SS`.

## Functions

- `generate_response(prompt, messages, max_tokens=1500, temperature=1)`: Generates a response to a prompt using GPT-4.

- `spinning_cursor(stop_flag)`: Displays a spinning loading animation.

- `call_gpt_with_spinner(prompt, messages)`: Calls the GPT-4 API with a loading animation.

- `get_desktop_path()`: Returns the path to the user's desktop.

- `chatbot()`: The main function that starts the chatbot.

## Customizations

You can customize various parameters for the GPT-4 model, such as `max_tokens` and `temperature`, in the `generate_response` function.

## Disclaimer

Please note that the usage of the OpenAI GPT-4 model requires an API key which is typically a paid feature. You are responsible for any costs associated with your usage.
