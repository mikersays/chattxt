import openai
import sys
import time
import threading
import os
from datetime import datetime

# Set up your API key. Replace the entire <API key> string with your OpenAI API key.
openai.api_key = "<API key>"

# Function to generate a response using GPT-4
def generate_response(prompt, messages, max_tokens=5000, temperature=1):
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        n=1,
        top_p=1,
    )
    messages.append({"role": "assistant", "content": response.choices[0].message['content']})
    return response.choices[0].message['content']

# Function to display a spinning loading animation
def spinning_cursor(stop_flag):
    while not stop_flag.is_set():
        for cursor in "|/-\\":
            sys.stdout.write(cursor)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")

# Function to call GPT-4 API with a loading animation
def call_gpt_with_spinner(prompt, messages):
    stop_flag = threading.Event()
    spinner = threading.Thread(target=spinning_cursor, args=(stop_flag,))
    spinner.daemon = True
    spinner.start()

    response = generate_response(prompt, messages)

    stop_flag.set()
    spinner.join()
    sys.stdout.write("\b")
    sys.stdout.flush()

    return response

# Function to get the user's desktop path
def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

# Main function to start the chatbot
def chatbot():
    # Prepare the prompt file path
    prompt_file_path = "<path_to_your_prompt_file>"
    
    # Read the content of the prompt file
    with open(prompt_file_path, "r") as prompt_file:
        prompt = prompt_file.read().strip()

    print(f"Generating response for the prompt from {prompt_file_path}")
    print("----------------------------------")

    # Prepare the output file
    desktop_path = get_desktop_path()
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"chat_output_{current_time}.md"
    output_file_path = os.path.join(desktop_path, output_filename)

    # Define Chatty's role or persona
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    with open(output_file_path, "w") as output_file:
        output_file.write(f"Prompt: {prompt}\n\n")  # Added an extra line

        print("AI: ", end="", flush=True)
        response = call_gpt_with_spinner(prompt, messages)
        print(response)

        output_file.write(f"AI: {response}\n\n")  # Added an extra line

    print(f"Chatbot conversation saved to: {output_file_path}")

if __name__ == "__main__":
    chatbot()
