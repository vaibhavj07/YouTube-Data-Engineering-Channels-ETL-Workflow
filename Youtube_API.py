from googleapiclient.discovery import build
import pandas as pd

def fetch_data_engineering_channels():
    # Set up API key and initialize YouTube API service
    api_key = 'apikey'  # Replace with your YouTube API key
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Search for channels related to data engineering
    print("Fetching channels...")
    search_response = youtube.search().list(
        q='data engineering',  # Query term
        type='channel',  # Limit results to channels
        part='id',  # Only need the channel ID for now
        maxResults=10  # Maximum number of results to return (adjust as needed)
    ).execute()

    # Extract channel IDs from search results
    channel_ids = [search_result['id']['channelId'] for search_result in search_response.get('items', [])]

    # Prepare lists to store channel information
    channels_info = []

    # Iterate over each channel ID to fetch additional information
    for channel_id in channel_ids:
        # Fetch channel details
        print(f"Fetching details for channel ID: {channel_id}")
        channel_response = youtube.channels().list(
            part='snippet,statistics',
            id=channel_id
        ).execute()

        # Extract relevant channel information
        channel_info = {
            'Channel ID': channel_id,
            'Channel Title': channel_response['items'][0]['snippet']['title'],
            'Channel Description': channel_response['items'][0]['snippet']['description'],
            'Channel URL': f"https://www.youtube.com/channel/{channel_id}"
        }

        # Fetch the latest video from the channel
        print(f"Fetching latest video for channel ID: {channel_id}")
        latest_video_response = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            order='date',  # Order by upload date to get the latest video
            maxResults=1  # Fetch only the latest video
        ).execute()

        if latest_video_response.get('items'):
            latest_video_id = latest_video_response['items'][0]['id']['videoId']
            latest_video_title = latest_video_response['items'][0]['snippet']['title']
            latest_video_link = f"https://www.youtube.com/watch?v={latest_video_id}"
            channel_info['Latest Video Title'] = latest_video_title
            channel_info['Latest Video Link'] = latest_video_link

        # Fetch the most-watched video from the channel
        print(f"Fetching most watched video for channel ID: {channel_id}")
        most_watched_video_response = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            order='viewCount',  # Order by view count to get the most-watched video
            maxResults=1  # Fetch only the most-watched video
        ).execute()

        try:
            most_watched_video_id = most_watched_video_response['items'][0]['id']['videoId']
            most_watched_video_title = most_watched_video_response['items'][0]['snippet']['title']
            most_watched_video_link = f"https://www.youtube.com/watch?v={most_watched_video_id}"
            channel_info['Most Watched Video Title'] = most_watched_video_title
            channel_info['Most Watched Video Link'] = most_watched_video_link
        except KeyError:
            print(f"KeyError: 'videoId' not found in most_watched_video_response for channel ID: {channel_id}")
            print("Most Watched Video Response:", most_watched_video_response)

        # Append channel information to the list
        channels_info.append(channel_info)

    # Convert data to a DataFrame
    df = pd.DataFrame(channels_info)

    # Save DataFrame to a CSV file
    df.to_csv('s3://airflow-op-bucket/data_engineering_channels_info.csv', index=False)
    print("Data saved to 'data_engineering_channels_info.csv'")

if __name__ == '__main__':
    fetch_data_engineering_channels()
