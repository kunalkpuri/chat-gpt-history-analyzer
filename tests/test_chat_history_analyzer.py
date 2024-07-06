import unittest
import os
import json
from chat_history_analyzer import load_config, load_chat_history

class TestChatHistoryAnalyzer(unittest.TestCase):
    def setUp(self):
        self.config_path = 'config.json.example'
        self.config = load_config(self.config_path)
    
    def test_load_config(self):
        self.assertIn('api_key', self.config)
    
    def test_load_chat_history(self):
        history_path = self.config['chat_history_folder']
        os.makedirs(history_path, exist_ok=True)
        chat_history_file = os.path.join(history_path, 'test_history.json')
        with open(chat_history_file, 'w') as f:
            json.dump([], f)
        chat_history = load_chat_history(chat_history_file)
        self.assertIsInstance(chat_history, list)

if __name__ == '__main__':
    unittest.main()
