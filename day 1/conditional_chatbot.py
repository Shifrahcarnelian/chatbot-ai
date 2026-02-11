user=input("you:").lower()
bot="" #Response variable
if user == "hi":
    bot="hello!"
elif user == "hello":
    bot = "how may i assist you?"
elif user == "name":
    bot = "I am a simple chatbot"
elif user == "bye":
    bot = "good bye have a good day!"
else:
    bot-"I don't understand"
print("Bot:",bot)