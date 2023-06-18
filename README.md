# Local-LLM Chat

This is a lightweight chatbot designed to allow users to run an open-source Large Language Model (LLM) with [GPT4All](https://github.com/nomic-ai/gpt4all), locally via a Python API. This makes it possible to chat with the LLM directly from the command line without an internet connection or external bias.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.6 or later.

## Installing Local-LLM Chat

To install Local-LLM, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the directory containing the cloned repository.
3. Install the required Python package by running the following command in your terminal:

```bash
pip install gpt4all
```

## Usage

To start the chat program, navigate to the directory containing the Python script (`chat.py`) and run the following command:

```bash
python LocalLLM.py
```

In the command line interface, you can type in your chat messages. The GPT4All model will respond to each message. To end the chat and quit the program, type 'quit' or press Ctrl+C.

## LLM Models

By default this program runs the ggml-gpt4all-j-v1.3-groovy LLM model. To use a different model, replace "ggml-gpt4all-j-v1.3-groovy" in the script with the name of your desired model. 


Alternative models can be  found [here](https://gpt4all.io/models/models.json).
