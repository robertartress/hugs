import re
import os

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    for placeholder, new_value in replacements.items():
        content = re.sub(placeholder, new_value, content)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    html_filename = 'index.html'
    js_filename = 'playerData.js'

    new_link = input("Enter the new Dropbox link: ")
    new_title = input("Enter the new title: ")
    new_artist = input("Enter the new artist name: ")
    new_file_name = input("Enter the new file name for playerData.js: ")

    # Remove the file extension for the song title
    new_song_title, _ = os.path.splitext(new_file_name)

    # Update index.html
    html_replacements = {
        r'href="PLACEHOLDER_LINK"': f'href="{new_link}"',
        r'<title>PLACEHOLDER_TITLE': f'<title>{new_title}',
        'PLACEHOLDER_ARTIST': new_artist
    }
    update_file(html_filename, html_replacements)

    # Update playerData.js
    js_replacements = {
        'PLACEHOLDER_FILENAME': new_file_name,
        'PLACEHOLDER_SONG_TITLE': new_song_title
    }
    update_file(js_filename, js_replacements)

    print("HTML and JavaScript files have been updated.")

if __name__ == "__main__":
    main()
