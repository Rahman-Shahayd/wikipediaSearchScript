import webbrowser

query = input("Enter a search query: ")

# format the query for Wikipedia search
wikipedia_search_url = "https://en.wikipedia.org/wiki/Special:Search?limit=1&offset=0&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1&search=" + query

# open the Wikipedia page in the default web browser
webbrowser.open_new_tab(wikipedia_search_url)
