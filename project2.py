while True:
    msg = input("You: ")

    if msg == "hello":
        print("Bot: Hi!")
    elif msg == "bye":
        print("Bot: Goodbye")
        break
    else:
        print("Bot: I don't understand")
        