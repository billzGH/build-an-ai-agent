import argparse
import os
from dotenv import load_dotenv
from call_function import available_functions
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import call_function

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set.")
    client = genai.Client(api_key=api_key)
    user_prompt = args.user_prompt
    verbose_flag = args.verbose
    model_name = "gemini-2.5-flash"
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        )
    )
    if response.usage_metadata is None:
        raise RuntimeError("Response is missing usage metadata.")
    if verbose_flag:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls is not None:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=verbose_flag)
            if not function_call_result.parts:
                raise Exception("Function call result has no parts")
            if function_call_result.parts[0].function_response is None:
                raise Exception("Function call result has no function response")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("Function call result has no response")
            if verbose_flag:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print(f"Response: {response.text}")


if __name__ == "__main__":
    main()
