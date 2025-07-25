def chatbot():
    print("Chatbot: Hello! How can I help you?")
    while True:
        user_input = input("You:").lower()
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing fine!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")
chatbot()