import os
import google.generativeai as genai

# Configure the Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def check_api_health():
    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Use a simple prompt to check if the API is responsive
        test_prompt = "Please confirm if the API is working."
        response = model.generate_content(test_prompt)

        # Check if the response is valid
        if response and hasattr(response, "text") and response.text:
            return True  # API is working
        else:
            return False  # API did not return valid text
    except Exception as e:
        print(f"Health check error with Gemini API: {e}")
        return False  # API is not working

def dramatize_text(text, drama_level):
    if not check_api_health():
        return "The Gemini API is currently unavailable. Please try again later."

    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Construct the prompt with a Regina George-like tone
        prompt = (
            f"Imagine Regina George from Mean Girls is telling a juicy story. "
            f"Make the following story sound super dramatic and sassy, with a drama level of {drama_level}:\n"
            f"{text}"
        )

        # Generate content using the Gemini model
        response = model.generate_content(prompt)

        # Check and return the response text if available
        if response and hasattr(response, "text") and response.text:
            return response.text.strip()
        else:
            return "The story could not be processed due to content restrictions. Please try a different story or adjust the drama level."
    except Exception as e:
        print(f"Error with Gemini API: {e}")
        return "An error occurred while processing your request. Please try again later."
