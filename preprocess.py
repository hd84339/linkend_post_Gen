import json


def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    with open(raw_file_path, encoding="utf-8") as file:
        posts = json.load(file)

    enriched_posts = []

    for post in posts:
        metadata = extract_metadata(post["text"])
        post_with_metadata = post | metadata
        enriched_posts.append(post_with_metadata)

    for epost in enriched_posts:
        print(epost)

    with open(processed_file_path, "w", encoding="utf-8") as file:
        json.dump(enriched_posts, file, indent=4)


def extract_metadata(post):
    return {
        "line_count": 10,
        "language": "English",
        "tags": ["Mental Health", "Motivation"]
    }


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")