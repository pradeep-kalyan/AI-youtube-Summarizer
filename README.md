# AI YouTube Summarizer

**AI YouTube Summarizer** is a Streamlit app powered by Google's Gemini-1.5-pro, designed to summarize YouTube videos efficiently by processing their transcripts.

## Features

- **Transcription**: Extracts and processes transcripts from YouTube videos.
- **Summarization**: Generates concise, clear summaries of video content.
- **User-Friendly Interface**: Streamlit-based UI with easy-to-use input fields and clear instructions.
- **Interactive Elements**: Includes success notifications, error handling, and loading indicators.

## How to Use

1. **Enter YouTube URL**:

   - Paste the YouTube video URL into the provided text input field.

2. **Submit**:

   - Click on the "Submit" button.
   - The app will retrieve the transcript from the video.

3. **Wait**:
   - The app will process the transcript and generate a summary.
   - View the summary displayed on the screen.

## Installation and Setup

### Prerequisites

- Python 3.6 or later
- Streamlit
- google-generativeai
- youtube-transcript-api
- re

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/ai-youtube-summarizer.git
   cd ai-youtube-summarizer
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   ```bash
   streamlit run your_script_name.py
   ```

## Configuration

Configure the API key for Google Generative AI by setting the `api_key`:

```python
configure(api_key="YOUR_API_KEY")
```
