import re

def extract_hashtags(post):
    """Extract unique hashtags from the given post."""
    hashtags = re.findall(r'#\w+', post)
    unique_hashtags = set(hashtags)
    sorted_hashtags = sorted(unique_hashtags)
    return sorted_hashtags

def main():
    post = input("Enter a social media post: ")
    hashtags = extract_hashtags(post)
    if hashtags:
        print("Unique hashtags found:")
        for tag in hashtags:
            print(tag)
    else:
        print("No hashtags found.")


main()
