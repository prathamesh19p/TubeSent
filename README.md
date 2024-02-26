# TubeSent

TubeSent is a sentiment analysis tool for analyzing comments on YouTube videos. It allows users to fetch comments from YouTube videos, clean them, and perform sentiment analysis using Vader Sentiment Analyzer.

## Features

- Fetch comments from YouTube videos.
- Clean comments to remove emojis.
- Analyze sentiment using both Vader Sentiment Analyzer and TextBlob Sentiment Analyzer.
- Display overall sentiment analysis results.

## Installation

To use TubeSent, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/prathamesh19p/TubeSent.git
    ```

2. Run the program:
    ```bash
    python tubesent.py
    ```

## Usage

1. Run the program by executing `tubesent.py`.
2. Enter the YouTube video ID when prompted.
3. TubeSent will fetch comments, clean them, and perform sentiment analysis.
4. Results will be displayed showing the overall sentiment analysis using both Vader and TextBlob.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or found a bug, please open an issue on the [GitHub repository](https://github.com/prathamesh19p/TubeSent/issues) or submit a pull request.

## Acknowledgements

TubeSent utilizes the following libraries:

- [Google API Client Library](https://github.com/googleapis/google-api-python-client)
- [NLTK](https://www.nltk.org/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
