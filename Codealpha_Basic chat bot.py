def chatbot():

    print("=================================")
    print("        BASIC CHATBOT")
    print("=================================")
    print("Type 'bye' to exit the chatbot.\n")

    while True:

        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! Welcome.")

        elif user == "how are you":
            print("Bot: I am fine. Thank you!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
