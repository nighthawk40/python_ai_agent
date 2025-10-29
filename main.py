import os 
import sys
from dotenv import load_dotenv
from google import genai 
from google.genai import types

def main():
    # Load environment variables from the .env file into os.environ
    load_dotenv()

    # Ensure user supplied a prompt on command line
    if len(sys.argv) < 2:
        print('Error: No prompt provided.\nUsage: uv run main.py "your prompt here"', file=sys.stderr)
        sys.exit(1)

    
    # Store user input  
    user_prompt = sys.argv[1]

    # Retrieve the Gemini API key from the environment 
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in env variables")
    
    # Initialize the Gemini API Client with the provided key 
    client = genai.Client(api_key=api_key)

     messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Send a single prompt to the Gemnini model and receive a response
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    # Display the text output returned by the model 
    # print("\n=== Model Response ===")
    print(response.text)
    
    # Collect token usage information for cost/efficieny awareness
    usage = response.usage_metadata
    # print("\n=== Token Usage ===")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")


if __name__ == "__main__":
    main()
