import gpt4all

model="ggml-gpt4all-j-v1.3-groovy"
gptj = gpt4all.GPT4All(model)

print("\nLocalLLM running " + model + "\n")
print("Hello I am a locally run chatbot, what can I do for you?")

try:
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        messages = [{"role": "user", "content": user_input}]
        gptj.chat_completion(messages)

except KeyboardInterrupt:
    print("\nExiting...")