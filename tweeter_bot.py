import tweepy
import requests
import shutil
from quote_generator import generate_inspirational_quote  # Import the quote generation function

# Add Twitter API credentials
consumer_key = "HVERKzLCqDBPJQd7xwYmZvpGY"
consumer_secret = "rz2gX7VM1kUNYyH6doXpj3qZdHwVWsT21MmmKkQC78UUi6Thsd"
access_token = "1756881055410270208-PtsXcZhqrMwbCkdMK6DpMKpb87LubU"
access_token_secret = "xJEdoT9M55Fnnk8JvS4z5sbOQYq4utCKHM03ubvEyJuIn"

# Authentication
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api_v1 = tweepy.API(auth)

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True
)

# Fetching a random dog image URL from the API
response = requests.get("https://dog.ceo/api/breeds/image/random")
if response.status_code == 200:
    dog_image_url = response.json()['message']
    print(f"Fetched dog image URL: {dog_image_url}")

    # Download the image
    image_response = requests.get(dog_image_url, stream=True)
    if image_response.status_code == 200:
        # Save the image to a local file
        image_path = "random_dog_image.jpg"
        with open(image_path, 'wb') as out_file:
            shutil.copyfileobj(image_response.raw, out_file)
        print(f"Image saved to {image_path}")

        # Upload the image to Twitter (using API V1.1)
        media = api_v1.media_upload(filename=image_path)

        # Extract media ID from the response
        media_id = media.media_id_string

        # Generate an inspirational quote
        quote = generate_inspirational_quote()  # Use the function from quote_generator.py
        print(f"Generated inspirational quote: {quote}")

        # Post a tweet with the image and the inspirational quote
        tweet_response = client.create_tweet(text=quote, media_ids=[media_id])

        # Print the response from Twitter
        print(tweet_response.data)
    else:
        print("Failed to download the image.")
else:
    print("Failed to fetch a random dog image from the API.")
