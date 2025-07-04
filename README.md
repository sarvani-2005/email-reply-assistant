# Email Reply Assistant

Email Reply Assistant is a web application that leverages AI to help users quickly read, generate, and send email replies using Google's Gmail API and Gemini language models. The app provides a simple UI to fetch unread emails, generate smart replies in various tones, and send responses directly from your Gmail account.

## Features

- **Gmail Integration**: Authenticate with your Gmail account to fetch unread emails and send replies seamlessly.
- **AI-Powered Reply Generation**: Uses Gemini language models to generate context-aware replies to incoming emails.
- **Customizable Tone**: Choose the tone of your reply—formal, casual, friendly, or apologetic.
- **Editable Replies**: Edit the generated reply before sending.
- **Streamlit Interface**: Simple and interactive web UI for managing email replies.

## How It Works

1. **Authenticate**: The app uses Google OAuth2 to connect to your Gmail account.
2. **Fetch Latest Email**: Pulls the latest unread email from your inbox.
3. **Generate Reply**: The AI reads the email and generates a reply in your chosen tone.
4. **Edit & Send**: You can review and edit the reply before sending it back to the sender.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sarvani-2005/email-reply-assistant.git
    cd email-reply-assistant
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    - Create a `.env` file with your Gemini API key:
      ```
      GEMINI_API_KEY=your_gemini_api_key_here
      ```
    - Download your Gmail API credentials as `credentials.json` from Google Cloud Console.

4. **Run the app**:
    ```bash
    streamlit run app.py
    ```

## File Overview

- `app.py`: Streamlit app that provides the UI and main workflow.
- `reply_generator.py`: Handles AI-powered reply generation using Gemini.
- `email_utils.py`: Functions for Gmail authentication, fetching emails, and sending replies.

## Requirements

- Python 3.x
- Gmail API credentials (`credentials.json`)
- Gemini API key

## License

This project is open source and available under the [MIT License](LICENSE).
