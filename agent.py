"""Main AI Agent class for interacting with Ollama"""

import requests
import json
from typing import Optional, Dict, Any
from config import OLLAMA_BASE_URL, OLLAMA_MODEL, MAX_RETRIES, TIMEOUT, AGENT_NAME


class OllamaAgent:
    """AI Agent that communicates with Ollama local LLM"""
    
    def __init__(self, model: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize the Ollama Agent
        
        Args:
            model: Model name (defaults to config)
            base_url: Ollama server URL (defaults to config)
        """
        self.model = model or OLLAMA_MODEL
        self.base_url = base_url or OLLAMA_BASE_URL
        self.conversation_history = []
        self.name = AGENT_NAME
        
    def _make_request(self, prompt: str, stream: bool = False) -> Dict[str, Any]:
        """
        Make a request to Ollama API
        
        Args:
            prompt: The input prompt
            stream: Whether to stream the response
            
        Returns:
            Response from Ollama
        """
        url = f"{self.base_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream
        }
        
        try:
            response = requests.post(
                url,
                json=payload,
                timeout=TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Ollama: {e}")
            raise
    
    def generate(self, prompt: str, stream: bool = False) -> str:
        """
        Generate a response from the model
        
        Args:
            prompt: Input prompt for the model
            stream: Whether to stream the response
            
        Returns:
            Model response text
        """
        try:
            response = self._make_request(prompt, stream=stream)
            return response.get("response", "")
        except Exception as e:
            print(f"Failed to generate response: {e}")
            return ""
    
    def chat(self, user_message: str) -> str:
        """
        Have a conversation with the agent
        
        Args:
            user_message: User's message
            
        Returns:
            Agent's response
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Build context from conversation history
        context = self._build_context()
        
        # Generate response
        response = self.generate(context)
        
        # Add assistant response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })
        
        return response
    
    def _build_context(self) -> str:
        """Build prompt context from conversation history"""
        context = f"You are {self.name}. You are helpful, harmless, and honest.\n\n"
        
        for message in self.conversation_history:
            role = "User" if message["role"] == "user" else "Assistant"
            context += f"{role}: {message['content']}\n"
        
        context += "Assistant: "
        return context
    
    def reset_conversation(self) -> None:
        """Clear conversation history"""
        self.conversation_history = []
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the current model"""
        try:
            url = f"{self.base_url}/api/show"
            response = requests.post(
                url,
                json={"name": self.model},
                timeout=TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Failed to get model info: {e}")
            return {}


if __name__ == "__main__":
    # Example usage
    agent = OllamaAgent()
    
    print(f"Starting {agent.name}...")
    print(f"Using model: {agent.model}")
    print(f"Ollama URL: {agent.base_url}")
    print("-" * 50)
    
    # Interactive chat loop
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Goodbye!")
                break
            
            print(f"\n{agent.name}: ", end="", flush=True)
            response = agent.chat(user_input)
            print(response)
        except KeyboardInterrupt:
            print("\nInterrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
