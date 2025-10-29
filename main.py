import os 
from dotenv import load_dotenv
from google import genai 

def main():
    # Load environment variables from the .env file into os.environ
    load_dotenv()

    # Retrieve the Gemini API key from the environment 
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in env variables")
    
    # Initialize the Gemini API Client with the provided key 
    client = genai.Client(api_key=api_key)

    # Send a single prompt to the Gemnini model and receive a response
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )

    # Display the text output returned by the model 
    print("\n=== Model Response ===")
    print(response.text)
    
    # Collect token usage information for cost/efficieny awareness
    usage = response.usage_metadata
    print("\n=== Token Usage ===")
    print(f"- Prompt Tokens: {usage.prompt_token_count}")
    print(f"- Response Tokens: {usage.candidates_token_count}")


if __name__ == "__main__":
    main()
