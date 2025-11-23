"""Main entry point for the AI Agent application"""

from agent import OllamaAgent


def main():
    """Main application function"""
    print("=" * 60)
    print("AI Agent with Ollama")
    print("=" * 60)
    
    # Initialize agent
    agent = OllamaAgent()
    
    print(f"\n✓ Agent initialized: {agent.name}")
    print(f"✓ Model: {agent.model}")
    print(f"✓ Ollama URL: {agent.base_url}")
    
    # Check model info
    print("\nFetching model information...")
    model_info = agent.get_model_info()
    if model_info:
        print(f"✓ Model loaded successfully")
    else:
        print("⚠ Could not fetch model info. Make sure Ollama is running.")
    
    print("\n" + "=" * 60)
    print("Interactive Chat Mode")
    print("Type 'exit' or 'quit' to end the conversation")
    print("=" * 60)
    
    # Start interactive loop
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\n✓ Thank you for using the AI Agent. Goodbye!")
                break
            
            print(f"\n{agent.name}: ", end="", flush=True)
            response = agent.chat(user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\n\n✓ Interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()
