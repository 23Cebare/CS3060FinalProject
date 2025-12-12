# Code Translator (Llama 2)

This project is a web-based code translator that uses Llama 2 (via Ollama) to translate code between programming languages, such as C to Python.

## Prerequisites
- Python 3.8+
- [Ollama](https://ollama.com/) installed and running
- Llama 2 model pulled with Ollama

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd CS3060FinalProject/code_translator
   ```

2. **Install Python dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Install and Start Ollama**
   - Download and install Ollama from [ollama.com](https://ollama.com/).
   - Open a terminal and run:
     ```sh
     ollama serve
     ```
   - Pull the Llama 2 model:
     ```sh
     ollama pull llama2
     ```

4. **Run the Flask Application**
   ```sh
   python app.py
   ```
   The app will be available at [http://localhost:5000](http://localhost:5000)

5. **Usage**
   - Open your browser and go to [http://localhost:5000](http://localhost:5000)
   - Paste your source code, select source and target languages, and click "Translate".

## Troubleshooting
- If you see connection errors, make sure Ollama is running and the Llama 2 model is pulled.
- If you get model errors, try restarting Ollama and the Flask app.

## Project Structure
```
CS3060FinalProject/
  code_translator/
    app.py
    requirements.txt
    translator.py
    templates/
      index.html
  frontend/
    index.html
```


