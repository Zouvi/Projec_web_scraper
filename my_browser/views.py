import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import FileResponse

def index(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        url = f"https://www.google.com/search?q={search_query}"
        response = requests.get(url, headers={
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        },)

        soup = BeautifulSoup(response.text, "html.parser")
        result_part = soup.find_all("div", attrs={"class": "g"})


        # Zde implementujte konkrétní extrakci dat z HTML stránky
        results = []
        with open("test1.json", "w") as file_test:
            file_test.write("[")
        
        for result in result_part:
            link = result.find("a", href=True)["href"]
            title = result.find("h3").text
            description = result.select_one("div[class*='VwiC3b yXK7lf p4wth r025kc hJNv6b']")
            if description is not None:
                description = description.text
            results.append({'title': title, 'link': link, 'description': description})
            with open("test1.json", "a", encoding="UTF-8") as file_test:
                file_test.write(f'{{"title": "{title}", "link": "{link}", "description": "{description}"}},')

        with open("test1.json", "a") as file_test:
            file_test.write("]")

        response = FileResponse(open("test1.json", 'rb'), as_attachment=True)
        return response
    else:
        return render(request, 'my_browser/index.html')





