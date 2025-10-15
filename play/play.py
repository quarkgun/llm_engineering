from bs4 import BeautifulSoup
import requests

URL = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
URL2 = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"

class AsciiMap:
    def __init__(self, coords, width, height):
        self.coords = coords
        self.width = width
        self.height = height
    
    def __repr__(self):
        return f"AsciiMap(coords={self.coords}, width={self.width}, height={self.height})"

def get_ascii_map_from_url(url):
    response = requests.get(url)
    html = response.text

    i1 = html.find("<table")
    i2 = html.find("</table>")

    if i1 == -1 or i2 == -1:
        raise ValueError("Could not find table in the HTML content.")

    table = html[i1:i2]

    soup = BeautifulSoup(table, 'html.parser')
    fields = soup.find_all("span")[3:]

    coords = {}
    max_x = 0
    max_y = 0

    for i in range(0, len(fields), 3):
        x = int(fields[i].text)
        y = int(fields[i + 2].text)
        c = fields[i + 1].text

        coords[(x, y)] = c

        max_x = max(max_x, x)
        max_y = max(max_y, y)

    return AsciiMap(coords, max_x, max_y)

def print_ascii_map(ascii_map):
    for y in range(ascii_map.height + 1):
        for x in range(ascii_map.width + 1):
            char = ascii_map.coords.get((x, y), ' ')
            print(char, end="")
        print("")

def print_ascii_map_from_url(url):
    ascii_map = get_ascii_map_from_url(url)
    print_ascii_map(ascii_map)

if __name__ == "__main__":
    print("Map from URL 1:")
    print_ascii_map_from_url(URL)
    print("\nMap from URL 2:")
    print_ascii_map_from_url(URL2)


# The code fetches an ASCII map from a Google Docs URL, parses it, and prints it in a grid format.
# It uses BeautifulSoup to extract coordinates and characters, storing them in an AsciiMap object.
# The map is then printed to the console, showing the characters at their respective coordinates.
# The map is represented as a dictionary with coordinates as keys and characters as values.
# The maximum x and y coordinates are also tracked to define the dimensions of the map.
# The code is designed to work with specific Google Docs documents that contain the ASCII map data.
# The map is printed row by row, with each character corresponding to its position in the grid.
# The output will show the ASCII representation of the map based on the data retrieved from the URL.
# The code is structured to be reusable for different URLs that follow the same format for ASCII maps.
# The AsciiMap class encapsulates the map data and provides a clear representation of the coordinates and dimensions.
# The use of requests and BeautifulSoup allows for easy web scraping and data extraction from HTML content.
# The code is efficient in parsing and displaying the ASCII map, making it suitable for quick visualizations of grid-based data.
# The implementation is straightforward, focusing on clarity and functionality for working with ASCII maps.
# The code can be extended or modified to handle different formats or additional features
