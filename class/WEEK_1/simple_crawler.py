page = '''
  <div id="courses-overlay" class="overlay">
                    <!-- TODO eventually load course list from database -->
                    <p><a href="/overview/Course/cs101">CS 101: Building a Search Engine</a></p>
                    <hr/>
                    <p><a href="/overview/Course/cs373">CS 373: Programming a Robotic Car</a></p>
                    <hr/>
                    <p><a href="/" class="arrow">SEE ALL UPCOMING CLASSES</a></p>       
                </div>
'''
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
    end_quote = html.find('"',start_quote+1)
    url = html[start_quote+1:end_quote]
    return (end_quote,url)

urls = get_urls(page)
for url in urls:
    print url
