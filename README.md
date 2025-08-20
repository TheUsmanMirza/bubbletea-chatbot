# AI Agent Todo List App

A AI-powered todo list application that follows the Bubbletea documentation pattern exactly. This bot manages todos through natural language conversation using OpenAI's GPT-4o.

## 🌟 **Features**

- **Natural Language Processing** - Understands conversational requests
- **Smart Todo Management** - Add, delete, and list todos intelligently
- **Context Awareness** - Remembers conversation context
- **Confirmation System** - Safe bulk deletion with confirmation
- **General Conversation** - Handles greetings, thank you, and casual chat
- **Bubbletea Integration** - Professional chat interface with zero frontend code
- **Intelligent Text Cleaning** - Automatically removes action words and articles
- **Duplicate Prevention** - Prevents adding the same task multiple times

## 🛠️ **Technology Stack**

- **Python 3.8+** - Core language
- **OpenAI GPT-4o** - Advanced AI processing
- **Bubbletea Chat** - Professional chat interface
- **ngrok** - Internet exposure for local development

## 📋 **Prerequisites**

- Python 3.8+ installed
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- ngrok account ([Sign up here](https://ngrok.com/signup))

## 💬 **Conversation Examples**

Your AI Todo Agent understands natural language and handles conversations exactly like this:

**Example Conversation Flow:**
```
Agent: Hello! I can help you keep track of your todo list. It's currently empty. Would you like to add anything?

User: I need to buy milk
Agent: Task 'buy milk' added.

User: also eggs
Agent: Task 'buy eggs' added.

User: Show me my list
Agent: Your tasks:
- buy milk
- buy eggs

User: Remove eggs
Agent: Task 'buy eggs' deleted.

User: Show me my list
Agent: Your tasks:
- buy milk
```

**Key Features:**
- **Smart Text Cleaning**: "I need to buy milk" → stores "buy milk" (preserves action)
- **Context Awareness**: "also eggs" → understands you want to add eggs
- **Natural Commands**: "Show me my list", "Remove eggs", "Clear all"
- **Duplicate Prevention**: Won't add the same task twice
- **Bulk Operations**: "Remove all" with confirmation
- **Action Preservation**: Keeps purpose like "buy", "call", "schedule", "visit"

## 🚀 **Complete Setup & Execution Guide**

### **Step 1: Project Setup**

1. **Clone/Download** 
    ```bash
    clone https://github.com/iamsaifali/todo-mate.git
    ```
2. **Navigate to project directory**:
   ```bash
   cd todo-mate
   ```

### **Step 2: Virtual Environment Setup**

1. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   ```

2. **Activate virtual environment**:
   ```bash
   # On macOS/Linux
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

**Required packages:**
- `bubbletea-chat[llm]` - Chat interface framework
- `openai` - OpenAI API client
- `python-dotenv` - Environment variable management

### **Step 4: Environment Configuration**

1. **Create `.env` file**:
   ```bash
   touch .env
   ```

2. **Add your OpenAI API key**:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

### **Step 5: Start Your AI Bot**

1. **Start the bot**:
   ```bash
   python main.py
   ```

2. **Expected output**:
   ```
   🤖 AI Todo Agent - Simple Bubbletea Bot
   ==================================================
   This follows the exact Bubbletea documentation pattern.
   The @bt.chatbot decorator automatically handles all the HTTP endpoint setup.
   
   🚀 Starting Bubbletea server on port 8000...
   ```

3. **Your bot is now running** on `http://localhost:8000`

### **Step 6: ngrok Setup for Internet Access**

1. **Install ngrok** (if not already installed):
   ```bash
   # macOS (using Homebrew)
   brew install ngrok
   
   # Or download directly
   curl -O https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-darwin-amd64.tgz
   tar xvzf ngrok-v3-stable-darwin-amd64.tgz
   sudo mv ngrok /usr/local/bin
   ```

2. **Sign up for ngrok account**:
   - Go to [https://ngrok.com/signup](https://ngrok.com/signup)
   - Create free account
   - Verify your email

3. **Get your authtoken**:
   - Go to [https://dashboard.ngrok.com/get-started/your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)
   - Copy your authtoken

4. **Configure ngrok**:
   ```bash
   ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
   ```

5. **Expose your bot to internet**:
   ```bash
   ngrok http 8000
   ```

6. **Copy your public URL** (e.g., `https://abc123.ngrok-free.app`)

### **Step 7: Connect to Bubbletea Platform**

1. **Go to** [Bubbletea Developer Dashboard](https://bubbletea.chat/developer)
2. **Enable Developer Mode** to get your API key
3. **Click "Add Bot"**
4. **Enter bot details**:
   - **Bot Name**: `todo-mate` (or any name you prefer)
   - **Bot URL**: Your ngrok URL (e.g., `https://abc123.ngrok-free.app/chat`)
5. **Click "Test"** to verify connection
6. **Click "Create Bot"** if test passes

### **Step 8: Start Chatting!**

Your bot is now accessible at:
- 🌐 **Web**: `https://bubbletea.chat/your-bot-name`
- 📱 **Mobile**: Bubbletea mobile app

## 💬 **Example Conversations**

### **Basic Todo Management**
```
User: I need to buy milk
Bot: Task 'milk' added.

User: also eggs
Bot: Task 'eggs' added.

User: Show me my list
Bot: Your tasks:
- milk
- eggs

User: Remove eggs
Bot: Task 'eggs' deleted.
```

### **General Conversation**
```
User: hello
Bot: Hello! Here's your current todo list:
- milk

User: how are you?
Bot: I'm doing great, thanks for asking! Here's your current todo list:
- milk

User: thank you
Bot: You're welcome! Here's your current todo list:
- milk
```

### **Bulk Operations**
```
User: remove all
Bot: Are you sure you want to delete ALL todos? Type 'yes' to confirm.

User: yes
Bot: All todos have been deleted. Your list is now empty.
```

## 🔧 **API Endpoints**

The `@bt.chatbot` decorator automatically creates:
- `POST /chat` - Chat endpoint for messages
- Other endpoints as needed

## 📁 **Project Structure**

```
Todo/
├── main.py                # Main bot application with Bubbletea integration
├── todo_agent.py          # AI agent logic with GPT-4o
├── models.py              # Data models and structures
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (your OpenAI API key)
└── README.md              # This comprehensive guide
```

## 🧪 **Testing Your Setup**

### **Local Testing**
```bash
# Test the chat endpoint
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

### **Public Testing**
Once connected to Bubbletea, test through the web interface.

## 📚 **Additional Resources**

- [Bubbletea Documentation](https://bubbletea.chat/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [ngrok Documentation](https://ngrok.com/docs)

## 🎯 **Success Checklist**

- ✅ Virtual environment activated
- ✅ Dependencies installed
- ✅ OpenAI API key configured
- ✅ Bot running on port 8000
- ✅ ngrok configured and running
- ✅ Connected to Bubbletea platform
- ✅ Bot responding to messages
- ✅ Todos being added/deleted correctly

## 🎉 **You're All Set!**

Your AI Todo Agent is now:
- **Running locally** on port 8000
- **Exposed to internet** via ngrok
- **Connected to Bubbletea** platform
- **Ready for users** worldwide

Start chatting and managing todos through natural language! 🚀
