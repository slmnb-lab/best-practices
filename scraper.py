import os
import requests
import html2text
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_gongjiyun_docs(start_url, output_dir="articles"):
    """
    Scrapes all articles from a specific section of gongjiyun.com docs.

    Args:
        start_url (str): The URL of the main documentation page.
        output_dir (str): The directory to save the markdown files.
    """
    print(f"Starting scrape for URL: {start_url}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(start_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the main page: {e}")
        return

    # Explicitly set encoding to utf-8 to handle potential issues
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the "最佳实践" (Best Practices) section header based on its text content
    # The text might be inside a span within the summary
    summary_tag = soup.find('summary', class_='astro-nt3f64gu', string=lambda t: t and '最佳实践' in t)

    if not summary_tag:
        # Fallback: try finding any summary that contains the text if the class changes
        all_summaries = soup.find_all('summary')
        summary_tag = next((s for s in all_summaries if '最佳实践' in s.get_text()), None)

    if not summary_tag:
        print("Could not find the '最佳实践' section header. Exiting.")
        return

    # The list of links is in the <ul> tag that is a sibling to the <summary>
    # inside a <details> tag.
    details_tag = summary_tag.find_parent('details')
    if not details_tag:
        print("Could not find the parent <details> tag for '最佳实践' section. Exiting.")
        return
        
    ul_tag = details_tag.find('ul')
    if not ul_tag:
        print("Could not find the <ul> list for '最佳实践' section. Exiting.")
        return

    article_links = []
    # Find all link tags within that section
    for link in ul_tag.find_all('a'):
        href = link.get('href')
        # The title is usually within a span inside the link
        title_span = link.find('span')
        title = title_span.text.strip() if title_span else link.text.strip()
        
        if href and title:
            # Construct the full URL
            full_url = urljoin(start_url, href)
            article_links.append({'url': full_url, 'title': title})

    if not article_links:
        print("No article links found under '最佳实践'.")
        return

    print(f"Found {len(article_links)} articles to scrape.")

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize html2text converter
    converter = html2text.HTML2Text()
    converter.body_width = 0 # Don't wrap lines

    for article in article_links:
        url = article['url']
        title = article['title']
        # Sanitize title to be a valid filename
        filename = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        filepath = os.path.join(output_dir, f"{filename}.md")

        print(f"Scraping: {title} ({url})")

        try:
            article_response = requests.get(url, headers=headers)
            article_response.raise_for_status()
            # Explicitly set encoding for article pages as well
            article_response.encoding = 'utf-8'
            article_soup = BeautifulSoup(article_response.text, 'html.parser')
            
            # Find the main content of the article
            # Updated class for main content
            content_div = article_soup.find('div', class_='sl-markdown-content')

            if content_div:
                # Resolve relative image URLs
                for img in content_div.find_all('img'):
                    src = img.get('src')
                    if src and src.startswith('/'):
                        img['src'] = urljoin('https://www.gongjiyun.com', src)

                # Convert HTML content to Markdown
                html_content = str(content_div)
                markdown_content = converter.handle(html_content)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"# {title}\n\n")
                    f.write(markdown_content)
                print(f"  -> Saved to {filepath}")
            else:
                print(f"  -> Could not find content for: {title}")

        except requests.exceptions.RequestException as e:
            print(f"  -> Error fetching article {title}: {e}")
        except IOError as e:
            print(f"  -> Error saving file {filepath}: {e}")

if __name__ == '__main__':
    target_url = "https://www.gongjiyun.com/docs/y/ofl0wheysi5kwhkh2nfcownhnxf/"
    scrape_gongjiyun_docs(target_url)
    print("\nScraping process finished.") 