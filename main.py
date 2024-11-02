# Import necessary libraries
from google.generativeai import GenerativeModel, configure
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import re
import streamlit as st
import os

# Retrieve the API key from environment variable
# data = os.environ["API_KEY"]
data=st.secrets["API_KEY"]
# Configure the API key for Google Generative AI
configure(api_key=data)

# Define generation configuration for the AI model
generation_config = {
    "temperature": 0.6,  # Controls randomness of the output
    "top_p": 0.95,  # Nucleus sampling parameter
    "top_k": 40,  # Limits the number of highest probability vocabulary tokens
    "max_output_tokens": 8192,  # Maximum number of tokens to generate in the output
    "response_mime_type": "text/plain",  # Specifies the format of the response
}

# Initialize the GenerativeModel with the specified configuration and instructions
model = GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="Using the transcript/data above, summarize the video/data in a crisp and clear manner. Ensure the data is understandable and format the data to provide it in points for better understanding.",
)


# Function to retrieve the transcript from a given YouTube link
def transcription(link):
    # Use regex to extract video ID from the provided YouTube URL
    video_id_match = re.search(r"v=([^&]+)", link)
    if not video_id_match:
        raise ValueError("Invalid YouTube URL")  # Raise an error if the URL is invalid
    video_id = video_id_match.group(1)  # Extract the video ID from the match
    # Retrieve the transcript for the video using the YouTubeTranscriptApi
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    # Join the transcript lines into a single string
    transcript = " ".join([line["text"] for line in transcript])
    return transcript  # Return the formatted transcript


# Streamlit UI setup
st.set_page_config(page_title="AI YouTube Summarizer", layout="wide")

# Customize the sidebar
with st.sidebar:
    st.title("AI YouTube Summarizer")
    st.markdown("Powered by Google's Gemini-1.5-pro")
    st.markdown("### How it Works:")
    st.markdown(
        """
    1. Enter your YouTube URL.
    2. Our AI processes the video transcript.
    3. Receive a concise, clear summary!
    """
    )

# Main layout
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>AI YouTube Summarizer</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: #0d47a1;'>Summarize YouTube videos with ease!</h3>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Get a quick and accurate summary of any YouTube video. Simply paste the link below and hit 'Submit'.</p>",
    unsafe_allow_html=True,
)

# Create a text input for the user to paste the YouTube URL
link = st.text_input("Paste your YouTube URL here:")

# Check if the user has provided a link
if link:
    # If the submit button is pressed
    if st.button("Submit"):
        st.success("URL submitted successfully")
        try:
            with st.spinner("Summarizing...."):
                # Retrieve the transcript using the transcription function
                trans = transcription(link)
                # Generate a summary using the AI model
                response = model.generate_content(trans)
                # Display the summary
                st.markdown("<h2>Summary</h2>", unsafe_allow_html=True)
                st.write(response.text)
        except Exception as e:
            # Handle any exceptions that occur during processing
            st.error(f"Oops, an error occurred: {e}")
else:
    # Warning message if no URL is provided
    st.warning("Please provide a valid URL.")
