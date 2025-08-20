#!/usr/bin/env python3
"""
AI Todo Agent - Simple Bubbletea Bot

This follows the exact Bubbletea documentation pattern.
The @bt.chatbot decorator automatically handles all the HTTP endpoint setup.
"""

import bubbletea_chat as bt
from todo_agent import TodoAgent
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the todo agent
todo_agent = TodoAgent()

@bt.chatbot
def todo_agent_bot(message: str):
    """
    AI Todo Agent chatbot that manages todos through natural language
    """
    try:
        # Process the message through the AI agent
        response = todo_agent.process_message(message, [])
        return bt.Text(response)
    except Exception as e:
        return bt.Text(f"Sorry, I encountered an error: {str(e)}")

if __name__ == "__main__":
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY environment variable not set!")
        print("Please create a .env file with your OpenAI API key.")
        exit(1)
    
    print("🤖 AI Todo Agent - Simple Bubbletea Bot")
    print("=" * 50)
    print("This follows the exact Bubbletea documentation pattern.")
    print("The @bt.chatbot decorator automatically handles all the HTTP endpoint setup.")
    print()
    
    # Creates /chat endpoint automatically
    bt.run_server(todo_agent_bot, port=8000, host="0.0.0.0")
