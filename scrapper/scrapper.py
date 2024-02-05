import json
import requests
from bson import ObjectId
from bs4 import BeautifulSoup

# Local imports
from utils.constants import MediumTags


async def scrap_articles():
    articles = {}
    
    for tag in MediumTags.TAGS.value:
        req = requests.get(f"https://medium.com/tag/{tag}")
        soup = BeautifulSoup(req.content, "html.parser")

        recommended_stories = soup.select("article")
        dup_href_checker = []

        for article in recommended_stories:
            links = article.find_all('a', class_='af ag ah ai aj ak al am an ao ap aq ar as at')
            authors = article.find_all('p', class_="be b fz z cl nk nl nm nn no np nq bj")
            avatars = article.find_all('img', class_="l he bx ng nh cu")
            titles = article.find_all('h2', class_="be oc lm ln od oe lo lp lq of og lr oh ju oi oj ok ol jx om on oo op ka oq or os cl nl nm no nq bj")
            descs = article.find_all("h3", class_="be b ou z cl ov nl nm ow no nq fy")
            timers = article.find_all("div", class_="ab q")

            for link, author, avatar, title, description, time in zip(links, authors, avatars, titles, descs, timers):
                href = link.get("href")
                aria_label = link.get("aria-label")
                author = author.text.strip()
                avatar = avatar.get('src')
                title = title.text.strip()
                description = description.text.strip()
                time = time.text.strip()

                if not aria_label:
                    continue
                elif (href not in dup_href_checker) and (author.upper() not in dup_href_checker) and (avatar not in dup_href_checker):
                    article_key = str(ObjectId())

                    articles[article_key] = {
                        "href": f"https://medium.com{href}",
                        "aria-label": aria_label,
                        "author": author,
                        "avatar": avatar,
                        "tag": tag,
                    }
                    dup_href_checker.append(href)
                    dup_href_checker.append(author.upper())
                    dup_href_checker.append(avatar)
                
                if 'title' not in list(articles[article_key].keys()):
                    articles[article_key]['title'] = title 
                
                if 'description' not in list(articles[article_key].keys()):
                    articles[article_key]['description'] = description
                
                if 'time' not in list(articles[article_key].keys()):
                    articles[article_key]['time'] = time

    json_articles = json.dumps(articles, indent=2)

    return json_articles