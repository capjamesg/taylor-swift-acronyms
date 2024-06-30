# r/TaylorSwift Acronym Analysis

This repository contains the code used for the following blog posts:

- [Taylor Swift Subreddit Acronym Reference](https://jamesg.blog/2024/06/30/taylor-swift-subreddit-acronyms/)
- [Analyzing use of Taylor Swift song name acronyms on Reddit](https://jamesg.blog/2024/06/30/taylor-swift-acronym-use-reddit/)

## Script Reference

- `retrieve_wikipedia_data.py`: Retrieves the list of songs for analysis from Wikipedia.
- `retrieve_acronym_use_from_reddit.py`: Retrieves the number of posts affiliated with an acronym on Reddit.
- `generate_charts_and_counts.py`: Generate charts and lists showing acronyms use. Date is grouped by album, and ordered by use.

## Data Reference

- `duplicates.json`: Used to record songs excluded from analysis because an acronym matches more than one song.
- `acronyms.txt`: A computed list of acronyms used in the [Taylor Swift Subreddit Acronym Reference](https://jamesg.blog/2024/06/30/taylor-swift-subreddit-acronyms/) blog post.
- `acronyms.json`: A list of acronyms included in analysis, without usage counts.
- `acronyms_final.json`: A list of acronyms, with usage counts.

## License

This source code is licensed under an [MIT license](LICENSE).
