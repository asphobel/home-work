import xml.etree.ElementTree as ET

def get_movie_description(movie_title):
    tree = ET.parse('movies.xml')
    root = tree.getroot()
    for movie in root.iter('movie'):
        if movie.get('title') == movie_title:
            return movie.find('description').text
    return None

description = get_movie_description("Ferris Bueller's Day Off")
print(description)