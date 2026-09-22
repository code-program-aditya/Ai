# Program: Rule-Based Chatbot for Customer Queries

def get_response(user_input):
    # Normalize user input
    user_input = user_input.lower().strip()

    # Greeting
    if ("hello" in user_input or
            "hi" in user_input or
            "hey" in user_input):
        return "Hello! How can I help you today?"

    # Order status
    elif ("order status" in user_input or
          "where is my order" in user_input or
          "track my order" in user_input):
        return "Please provide your order ID to check the order status."

    # Return
    elif ("return" in user_input or
          "replace" in user_input):
        return ("Our return policy allows eligible products to be "
                "returned within the specified return period.")

    # Refund
    elif ("refund" in user_input or
          "money back" in user_input):
        return ("Refunds are processed after the returned product "
                "is received and verified.")

    # Payment
    elif ("payment" in user_input or
          "pay" in user_input or
          "payment method" in user_input):
        return ("We accept commonly supported payment methods such "
                "as cards, UPI, and online payment options.")

    # Delivery
    elif ("delivery" in user_input or
          "shipping" in user_input):
        return ("Please share your order ID so that I can guide "
                "you regarding delivery information.")

    # Complaint / support
    elif ("complaint" in user_input or
          "problem" in user_input or
          "issue" in user_input or
          "help" in user_input):
        return ("I'm sorry for the inconvenience. Please describe "
                "your issue so that we can assist you.")

    # Contact
    elif ("contact" in user_input or
          "customer care" in user_input or
          "support number" in user_input):
        return ("Please contact customer support through the official "
                "customer-service channel.")

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        return "Thank you for contacting us. Goodbye!"

    # Unknown query
    else:
        return ("I'm sorry, I couldn't understand your query. "
                "Please rephrase it or contact customer support.")


# Start chatbot
print("==============================================")
print("      CUSTOMER SUPPORT RULE-BASED CHATBOT")
print("==============================================")
print("Ask about orders, returns, refunds, payment, delivery, or support.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("Customer: ")

    response = get_response(user_input)
    print("Chatbot:", response)

    if user_input.lower().strip() in ["bye", "exit", "quit"]:
        break
