def send_messages(messages,sent_messages):

    while messages:
        message = messages.pop()
        print(f'message: {message}')
        sent_messages.append(message)

messages = ['hey', 'hello', 'how are you']
sent_messages = []

send_messages( messages,sent_messages)

print(f'\nmessages: {messages}')
print(f'\nsent_messages: {sent_messages}')
