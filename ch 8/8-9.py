messages = ['hey', 'hello', 'how are you']
sent_messages = []

while messages[:]:
    message = messages.pop()
    print(f'Message: {message}')
    sent_messages.append(message)

print('\nThe following messages have been sent:')
for sent_message in sent_messages:
    print(sent_message)
