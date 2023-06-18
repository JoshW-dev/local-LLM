import gpt4all
gptj = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy")

try:
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        messages = [{"role": "user", "content": user_input}]
        gptj.chat_completion(messages)

except KeyboardInterrupt:
    print("\nExiting...")