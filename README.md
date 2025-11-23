# CS3060FinalProject - AI Agent with Ollama

A Python-based AI agent that integrates with Ollama for local LLM inference. This project enables interactive conversations with locally-running language models.

## Features

- **Local LLM Integration**: Uses Ollama for running language models locally
- **Conversational Memory**: Maintains conversation history for context-aware responses
- **Easy Configuration**: Environment-based configuration system
- **Interactive Chat Interface**: Simple command-line chat interface
- **Model Flexibility**: Easy model switching via configuration

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running locally
- pip (Python package manager)

## Installation

### 1. Clone or navigate to the project directory

```bash
cd CS3060FinalProject
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Copy `.env.example` to `.env` and customize if needed:

```bash
cp .env.example .env
```

Default configuration uses:
- **Ollama URL**: `http://localhost:11434`
- **Model**: `llama2`

### 4. Start Ollama

Make sure Ollama is running on your system:

```bash
ollama serve
```

In another terminal, pull a model if you haven't already:

```bash
ollama pull llama2
```

Other available models: `mistral`, `neural-chat`, `dolphin-mixtral`, etc.

## Usage

### Run the agent

```bash
python main.py
```

### Interactive chat

```
You: What is the capital of France?
AI Agent: The capital of France is Paris...
```

Type `exit`, `quit`, or `bye` to end the conversation.

### Direct agent usage in code

```python
from agent import OllamaAgent

agent = OllamaAgent()
response = agent.generate("Hello, how are you?")
print(response)
```

## Configuration

Edit `.env` to customize:

```env
OLLAMA_BASE_URL=http://localhost:11434    # Ollama server URL
OLLAMA_MODEL=llama2                        # Model to use
AGENT_NAME=AI Agent                        # Agent display name
MAX_RETRIES=3                              # API retry attempts
TIMEOUT=30                                 # Request timeout in seconds
```

## Project Structure

```
.
├── main.py              # Entry point for the application
├── agent.py             # Main OllamaAgent class
├── config.py            # Configuration management
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
└── README.md            # This file
```

## API Reference

### OllamaAgent Class

#### `__init__(model=None, base_url=None)`
Initialize the agent with optional model and URL overrides.

#### `generate(prompt, stream=False)`
Generate a response from the model.

#### `chat(user_message)`
Have a conversation with the agent (maintains history).

#### `reset_conversation()`
Clear the conversation history.

#### `get_model_info()`
Retrieve information about the current model.

## Troubleshooting

**Error: Connection refused**
- Ensure Ollama is running: `ollama serve`
- Check the `OLLAMA_BASE_URL` in `.env` is correct

**Error: Model not found**
- Pull the model: `ollama pull llama2`
- Verify the model name in `.env` matches available models

**Slow responses**
- Check system resources (CPU/RAM)
- Consider using a smaller model (e.g., `mistral` vs `llama2`)
- Increase `TIMEOUT` in `.env`

## Models Available

Popular Ollama models:
- `llama2` - Meta's Llama 2 (7B)
- `mistral` - Mistral 7B
- `neural-chat` - Intel's Neural Chat
- `dolphin-mixtral` - Dolphin Mixtral 8x7B

View all: [Ollama Model Library](https://ollama.ai/library)

## License

This project is part of CS3060 Final Project.