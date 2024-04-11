import re

def update_html(new_link, new_artist):
    filename = 'index.html'  # Default HTML file name

    # Read the current content of the file
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace placeholders with new values
    content = re.sub(r'href="PLACEHOLDER_LINK"', f'href="{new_link}"', content)
    content = re.sub(r'PLACEHOLDER_ARTIST', new_artist, content)

    # Write the updated content back to the file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    new_link = input("Enter the new Dropbox link: ")
    new_artist = input("Enter the new artist name: ")

    update_html(new_link, new_artist)
    print("HTML file has been updated.")

if __name__ == "__main__":
    main()
