from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import requests
import re
from rich.console import Console

console = Console()


class YoutubeTranscript:

    @staticmethod
    def get_video_id(youtube_url):
        """
        Extract the video ID from a YouTube URL.
        Args:
            youtube_url (str): The YouTube URL.
        Returns:
            str: The extracted video ID or None if not found.
        """
        pattern = (r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?['
                   r'?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
        match = re.search(pattern, youtube_url)
        return match.group(1) if match else None

    @staticmethod
    def get_video_title(video_id):
        """
        Get the title of the YouTube video.
        Args:
            video_id (str): The YouTube video ID.
        Returns:
            str: The title of the video or "Unknown" if not found.
        """
        url = f"https://www.youtube.com/watch?v={video_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            matches = re.findall(r'<title>(.*?)</title>', response.text)
            return matches[0].replace(" - YouTube", "") if matches else "Unknown"
        except requests.RequestException as e:
            console.log(f"Error fetching video title: {e}", style='bold red')
            return "Unknown"

    @staticmethod
    def download_transcript(video_id):
        """
        Download the transcript and return as a string.
        Args:
            video_id (str): The YouTube video ID.
        Returns:
            str: The transcript text or an empty string if an error occurs.
        """
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_generated_transcript(['en'])

            formatter = TextFormatter()
            transcript_text = formatter.format_transcript(transcript.fetch())

            # Remove timecodes and speaker names
            transcript_text = re.sub(r'\[\d+:\d+:\d+\]', '', transcript_text)
            transcript_text = re.sub(r'<\w+>', '', transcript_text)
            return transcript_text
        except Exception as e:
            console.log(f"Error downloading transcript: {e}", style='bold red')
            return ""

    @staticmethod
    def get_transcript(youtube_url):
        video_id = YoutubeTranscript.get_video_id(youtube_url)
        if video_id:
            transcript_text = YoutubeTranscript.download_transcript(video_id)
            if transcript_text:
                return transcript_text
            else:
                console.log("Unable to download transcript.", style='bold red')
        else:
            console.log("Invalid YouTube URL.", style='bold red')


# if __name__ == '__main__':
#     print(YoutubeTranscript.get_transcript("https://youtu.be/dzog64ENKG0?si=f1DCubchrrSBbug2"))
