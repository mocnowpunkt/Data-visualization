import requests

from plotly.graph_objs import Bar, Layout
from plotly import offline

def get_response():
    """Make an API call and store the response"""
    url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    return r
        
def get_repo_dicts(r):
    """Make an API call and store the response"""
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def get_project_data(repo_dicts):
    """Return data needed for project visualization"""
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']    
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'> {repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])
        
        description = repo_dict['description']
        owner = repo_dict['owner']['login']
        label = f"{owner}<br /> {description}"
        labels.append(label)
    
    return repo_links, stars, labels
        
def make_visualization(repo_links, stars, labels):
    """Generate visualization for most commented articles"""
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
        'title': 'The most popular JavaScript repositories on git hub',
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

if __name__ == '__main__':
    r = get_response()
    repo_dicts = get_repo_dicts(r)
    repo_links, stars, labels = get_project_data(repo_dicts)
    make_visualization(repo_links, stars, labels)