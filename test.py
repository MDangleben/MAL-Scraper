# https://docs.python.org/2/library/xml.etree.elementtree.html

import requests
from theAnimeClass import Anime

url = ('http://myanimelist.net/malappinfo.php?u=cloudninek&status=all&type'
       '=anime')

r = requests.get(url)

# print r.text
print r.status_code

# encode otherwise string conversion throws errors
animelist = r.text.encode("utf-8")
animelist = str(animelist)

removeList = ['</anime>', '</series_animedb_id>', '</series_title>',
              '</series_synonyms>', '</series_type>', '</series_episodes>',
              '</series_status>', '</series_start>', '</series_end>',
              '</series_image>', '</my_id>', '</my_watched_episodes>',
              '</my_start_date>', '</my_finish_date>', '</my_score>',
              '</my_status>', '</my_rewatching>', '</my_rewatching_ep>',
              '</my_last_updated>', '</my_tags>']

for item in removeList:
    animelist = animelist.replace(item, '')

aList = animelist.split('<anime>')

splitList = []
for item in removeList:
    itemcut = item[:1] + item[2:]
    splitList.append(itemcut)

for k in range(len(aList)):
    for split in splitList:
        aList[k] = aList[k].replace(split, ',')

tempval = aList.pop(0)  # holds user values not anime values

AnimeList = []  # list of anime objects
for item in aList:
    anilist = item.split(',')
    anilist.pop(0)
    aniObj = Anime(anilist)
    AnimeList.append(aniObj)

for anime in AnimeList:
    print '\n'
    print anime.title

# listsplit = r.text.split(
# root = ET.fromstring(r.text)
