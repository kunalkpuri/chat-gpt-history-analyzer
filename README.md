# Chat GPT History Analyzer

A command-line tool to analyze chat history using OpenAI's GPT models. This tool allows you to maintain conversation context, create new chat history exports, and continue conversations with session files.

## Features

- Analyze chat history and maintain conversation context.
- Create new chat history exports.
- Continue conversations with session files.

## Requirements

- Python 3.6+
- OpenAI API key

## Installation

1. Clone the repository:
   `git clone https://github.com/yourusername/chat-gpt-history-analyzer.git`
   `cd chat-gpt-history-analyzer`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Copy the example config file and update it with your OpenAI API key:
   `cp config.json.example config.json`

4. Update `config.json` with your OpenAI API key and other settings.

## Usage

### Create a New History Export
`python3 chat_history_analyzer.py --create-history`

### Start a New Conversation
`python3 chat_history_analyzer.py --new-convo "What are the most common topics discussed?"`

### Continue a Conversation
`python3 chat_history_analyzer.py "Can you give me more details about the top topic?"`

## Use Cases

### Personal Use

For individuals, **Chat GPT History Analyzer** helps keep track of long-term interactions with AI, making personal projects or learning experiences more cohesive and productive:

1. **Memory**:
   - The tool remembers your conversations with the AI, so you don’t have to start over each time. This is useful for ongoing projects or learning sessions.

2. **Insight**:
   - It can highlight important parts of past conversations, helping you recall significant details or decisions without re-reading everything.

3. **Seamlessness**:
   - If you need to pause a conversation and come back later, the tool ensures you can resume without missing a beat, making your interactions more efficient and productive.

### Customer Support

**Chat GPT History Analyzer** can significantly enhance customer support by providing continuity and context in interactions between customers and support bots. Here’s how:

1. **Continuity in Conversations**:
   - **Problem**: Customers often have to repeat their issues each time they interact with a new support agent or bot.
   - **Solution**: The tool remembers previous interactions, so the bot can pick up the conversation where it left off, providing a seamless experience.

2. **Improved Response Quality**:
   - **Problem**: Without historical context, support bots may provide generic or repetitive solutions, frustrating customers.
   - **Solution**: With access to the chat history, the support bot can give more accurate and personalized responses, improving customer satisfaction.

3. **Efficient Issue Resolution**:
   - **Problem**: Gathering context and understanding previous interactions can delay issue resolution.
   - **Solution**: By analyzing past conversations, the tool helps the bot quickly grasp the problem, leading to faster resolutions.

4. **Consistency Across Channels**:
   - **Problem**: Fragmented support experiences across different channels (email, chat, phone).
   - **Solution**: The tool integrates with various support channels, ensuring all interactions are logged and accessible, providing a consistent support experience.

### Business Use

Businesses can leverage the **Chat GPT History Analyzer** in several ways to enhance operations, customer interactions, and overall efficiency:

1. **Customer Insights and Trends**:
   - **Benefit**: Analyzing chat histories helps businesses understand common issues, customer preferences, and trends. This data can be used to improve products, services, and customer support processes.
   - **Example**: A business can identify frequently asked questions or common problems faced by customers, allowing them to update their FAQs, improve product instructions, or address systemic issues proactively.

2. **Employee Training and Performance**:
   - **Benefit**: By reviewing chat histories, businesses can identify areas where customer support agents excel or need improvement.
   - **Example**: Training programs can be tailored based on real interactions, helping agents learn from actual scenarios. Performance reviews can include concrete examples from chat logs to provide constructive feedback.

3. **Automated Follow-Ups**:
   - **Benefit**: The tool can be used to automate follow-up messages based on previous interactions, ensuring that customers feel valued and their issues are being tracked.
   - **Example**: After a support interaction, the system can automatically send a follow-up message to the customer to check if their issue has been resolved or if they need further assistance.

4. **Compliance and Documentation**:
   - **Benefit**: Keeping detailed records of customer interactions is essential for compliance and legal purposes. The tool ensures that all conversations are logged and easily retrievable.
   - **Example**: In industries with strict compliance requirements (like finance or healthcare), having a complete log of customer interactions helps in audits and regulatory checks.

5. **Personalized Marketing**:
   - **Benefit**: Understanding individual customer interactions allows for more personalized marketing efforts.
   - **Example**: Businesses can use insights from chat histories to tailor marketing campaigns and offers to specific customer needs and preferences, increasing engagement and conversion rates.

## Testing

To ensure that the project works correctly, follow these steps:

1. **Create and Activate the Virtual Environment**:
   `python3 -m venv env`
   `source env/bin/activate`  # On Windows, use `env\Scripts\activate`

2. **Install Dependencies**:
   `pip install -r requirements.txt`

3. **Run the Tests**:
   `python -m unittest discover tests`

4. **Deactivate the Virtual Environment**:
   `deactivate`

## Contributing

Contributions are welcome! Please see `CONTRIBUTING.md` for more information.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

