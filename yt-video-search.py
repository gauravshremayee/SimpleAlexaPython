from youtube_search import YoutubeSearch

results = YoutubeSearch('expert jatt', max_results=10).to_json()

print(results)

# returns a json string

########################################

results = YoutubeSearch('search terms', max_results=10).to_dict()

print(results)
# returns a dictionary
