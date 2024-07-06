import json
import openai
import argparse
import os
from datetime import datetime

def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

def load_chat_history(file_path):
    with open(file_path, 'r') as file:  # Ensure this line is correct
        return json.load(file)

def analyze_chat_history(conversation, question, model):
    conversation.append({"role": "user", "content": question})
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=conversation
    )
    
    answer = response['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": answer})
    
    return answer

def create_new_history_export(history_folder):
    os.makedirs(history_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    history_file_path = os.path.join(history_folder, f"chat_history_{timestamp}.json")
    with open(history_file_path, 'w') as file:
        json.dump([], file, indent=4)
    return history_file_path

def get_unique_session_file_name(session_folder, history_file_path):
    os.makedirs(session_folder, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(history_file_path))[0]
    iterator = 1
    while True:
        session_file_path = os.path.join(session_folder, f"{base_name}_session_{iterator}.json")
        if not os.path.exists(session_file_path):
            return session_file_path
        iterator += 1

def main():
    parser = argparse.ArgumentParser(description="Analyze chat history with OpenAI's GPT models.")
    parser.add_argument('--config', default='config.json', help="Path to the configuration file (default: config.json).")
    parser.add_argument('--session', help="Path to the session file to maintain conversation context.")
    parser.add_argument('--new-convo', action='store_true', help="Flag to start a new conversation.")
    parser.add_argument('--create-history', action='store_true', help="Create a new history export.")
    parser.add_argument('question', nargs='?', help="The question you want to ask about the chat history.")
    args = parser.parse_args()

    config = load_config(args.config)
    openai.api_key = config['api_key']
    model = config.get("model", "gpt-4")
    
    if args.create_history:
        history_file_path = create_new_history_export(config['chat_history_folder'])
        print(f"New history export created at {history_file_path}")
        return

    if not args.question:
        parser.error("the following arguments are required: question")

    history_folder = config.get('chat_history_folder', 'histories')
    session_folder = config.get('session_folder', 'sessions')
    default_session_file = config.get('default_session_file', 'session_default.json')

    if not args.session:
        chat_history_files = sorted(
            [f for f in os.listdir(history_folder) if os.path.isfile(os.path.join(history_folder, f))],
            reverse=True
        )
        if chat_history_files:
            latest_history_file = chat_history_files[0]
            history_file_path = os.path.join(history_folder, latest_history_file)
            args.session = get_unique_session_file_name(session_folder, history_file_path)
        else:
            args.session = os.path.join(session_folder, default_session_file)
    
    if args.new_convo or not os.path.exists(args.session):
        conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    else:
        with open(args.session, 'r') as session_file:
            conversation = json.load(session_file)

    answer = analyze_chat_history(conversation, args.question, model)
    print(answer)
    
    with open(args.session, 'w') as session_file:
        json.dump(conversation, session_file, indent=4)

if __name__ == "__main__":
    main()
