from operator import itemgetter

import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts, titles, comments, discussion_links = [], [], [], []
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }

    discussion_name = response_dict['title'],
    discussion_url = submission_dict['hn_link']
    discussion_link = f"<a href='{discussion_url}'> {discussion_name}</a>"
    discussion_links.append(discussion_link)


    titles.append(response_dict['title'])
    comments.append(response_dict['descendants'])
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

# Make data visualization
data = [{
    'type': 'bar',
    'x': discussion_links,
    'y': comments,
}]

# make each submission act as a link to the discussion page for
    # that submission
my_layout = {
    'title': 'Most active discussions on Hacker News as of April 9, 2022',
    'xaxis': {'title': 'Title'},
    'yaxis': {'title': 'Number of comments'}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news.html')
