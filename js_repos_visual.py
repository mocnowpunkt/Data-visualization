import requests

from plotly.graph_objs import Bar, Layout
from plotly import offline

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process response
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels, forks = [], [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']    
    repo_url = repo_dict['owner']['url']
    repo_link = f"<a href='{repo_url}'> {repo_name}</a>"
    repo_links.append(repo_link)
    forks.append(repo_dict['forks'])
    stars.append(repo_dict['stargazers_count'])
    
    description = repo_dict['description']
    owner = repo_dict['owner']['login']
    label = f"{owner}<br /> {description}"
    labels.append(label)

# Make a visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    'opacity': 0.6,
    }
    }]

my_layout = {
    'title': 'Most JavaScript starred repositories on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
}}  

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='data_visualization/plots/js_repos.html')