def get_urls(html):
    urls = []
    eq = 0
    start_point = html.find('<a href=',eq)
    while start_point >= 0:
	eq, url = get_url(html,start_point)
        urls.append(url)
    	start_point = html.find('<a href=',eq)
    return urls

def get_url(html, start_point):
    start_quote = html.find('"',start_point)
    end_quote = html.find('"',end_quote)
    url = html[start_quote+1:end_quote]
    return (end_quote,url)
