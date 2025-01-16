import random
import json
import datetime

# Load configuration from JSON file
def load_data():
    with open('project.2.json', 'r') as file:
        data = json.load(file)
    return data

def get_name(data):
    return random.choice(data['agent_names'])

def get_response(input_from_user, user_name, data):
    responses = []
    input_from_user = input_from_user.lower()
    for keyword in data['keyword_responses']:
        if keyword in input_from_user:
            responses.append(data['keyword_responses'][keyword])
    if responses:
        response = " ,".join(responses)
    else:
        response = random.choice(data['random_responses'])

    if random.choice([1, 2, 3]) == 1:
        return f"{response} {user_name}"
    else:
        return response

# Log the conversation
def conversation_list(user_name, input_from_user, response):
    with open('conversation_list.txt', 'a') as log_file:
        log_file.write(f"{user_name}: {input_from_user}\n")
        log_file.write(f"Agent: {response}\n")

def log_session_start():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('conversation_list.txt', 'a') as log_file:
        log_file.write(f"\n--- New Conversation Session Started at {timestamp} ---\n")

def main():
    data = load_data()
    name_of_user = input("Welcome to the University of Poppleton! Please enter your name: ")
    agent_name = get_name(data)
    print(f"Hello {name_of_user}! My name is {agent_name}😊, how can I assist you today?")

    # Log the start of a new conversation session
    log_session_start()

    interaction_count = 0
    max_interactions = random.randint(5, 15)  # Randomly choose a number of interactions before disconnecting

    while True:
        input_from_user = input(f"{name_of_user}: ")
        if input_from_user.lower() in data["goodbye_responses"]:
            print("Thank you for chatting with us. Have a great day!")
            break

        response = get_response(input_from_user, name_of_user, data)
        print(f"{agent_name}: {response}")

        # Log the conversation
        conversation_list(name_of_user, input_from_user, response)

        interaction_count += 1
        if interaction_count >= max_interactions:
            print("Oops, it seems like the connection was lost. Please try again later.")
            break

if __name__ == "__main__":
    main()
