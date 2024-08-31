
# 🐶 Dog Image and Inspirational Quote Tweeter Bot 🐾

Having a RUFF morning? This project is a simple Python application that uses Google's Gemini API to generate short inspirational quotes and posts them on Twitter along with random dog images. The bot is perfect for bringing a daily dose of positivity and cuteness to your Twitter feed!

## ✨ Features

- 🐕 Fetches a random dog image from the [Dog CEO's Dog API](https://dog.ceo/dog-api/).
- 🌟 Generates a short inspirational quote with a dog-related pun using Google's Gemini API.
- 🐦 Posts the image and quote as a tweet on Twitter using Tweepy.

## 📋 Prerequisites

To run this project, ensure you have the following:

- 🐍 Python 3.9 or higher installed.
- 🐤 Twitter Developer account with API keys and access tokens.
- 🔑 A Google Gemini API key. You can get one from [Google AI Studio](https://studio.google.com/).

## ⚙️ Installation

1. **📥 Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/dog-quote-tweeter-bot.git
   cd dog-quote-tweeter-bot
   ```

2. **📦 Install Dependencies**

   Install the required Python packages using pip:

   ```bash
   pip install tweepy requests shutil google-generativeai
   ```

3. **🔐 Set Up Your API Keys**

   - Obtain your Twitter API keys and access tokens from the Twitter Developer portal and set them in the script.

   - Obtain your Gemini API key from Google AI Studio and configure it in the `quote_generator.py` script.

   - It is recommended to use environment variables for API keys to ensure security:

     On Unix-like systems (Linux, macOS):

     ```bash
     export API_KEY="your_gemini_api_key"
     export TWITTER_CONSUMER_KEY="your_consumer_key"
     export TWITTER_CONSUMER_SECRET="your_consumer_secret"
     export TWITTER_ACCESS_TOKEN="your_access_token"
     export TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
     ```

     On Windows:

     ```cmd
     set API_KEY="your_gemini_api_key"
     set TWITTER_CONSUMER_KEY="your_consumer_key"
     set TWITTER_CONSUMER_SECRET="your_consumer_secret"
     set TWITTER_ACCESS_TOKEN="your_access_token"
     set TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
     ```

## 🚀 Usage

1. **▶️ Run the Script**

   To post a tweet with a random dog image and an inspirational quote, run:

   ```bash
   python tweeter_bot.py
   ```

   Ensure that your API keys are correctly set up before running the script.

2. **📤 Output**

   After running the script, a tweet will be posted on the authenticated Twitter account with a dog image and an inspirational quote.

## 📁 Project Structure

```
dog-quote-tweeter-bot/
│
├── quote_generator.py   # Script for generating inspirational quotes using Gemini API
├── tweeter_bot.py       # Main script for fetching images and posting tweets
├── README.md            # Project documentation
└── requirements.txt     # List of Python dependencies
```

## 📝 Example

Below is an example of what might be posted as a tweet:

```
Image: [A random dog picture]
Text: "Start your day pawsitively! Remember, no mutt-er what, you can fetch your dreams! 🐶"
```

## 🤝 Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Make sure to follow the established coding style and include comments where necessary.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

If you have any questions or suggestions about this project, feel free to contact me at mc8870@nyu.edu.
