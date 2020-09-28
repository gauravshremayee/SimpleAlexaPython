from youtube_search import YoutubeSearch
import subprocess
results = YoutubeSearch('expert jatt', max_results=10).to_json()

print(results)

# returns a json string

########################################

results = YoutubeSearch('search terms', max_results=10).to_dict()

proc = subprocess.Popen(["chrome", "https://youtu.be/uBpwDnYuVO0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(results)
# returns a dictionary
