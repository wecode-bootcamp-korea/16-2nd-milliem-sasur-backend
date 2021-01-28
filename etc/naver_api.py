import os
import re
import sys
import json
import pandas as pd
import urllib.request

client_id = "D0lj0dwSs9pw8T4tHNo2"
client_secret = "bog5VuUDnc"

query = urllib.parse.quote(input("검색할 단어: "))
idx = 0
display = 1
start = 1
end = 200
sort = "sim"

book_df = pd.DataFrame(
    columns=(
        "title",
        "link",
        "image",
        "author",
        "price",
        "discount",
        "publisher",
        "isbn",
        "description",
        "pubdate",
    )
)

for start_index in range(start, end, display):

    url = (
        "https://openapi.naver.com/v1/search/book?query="
        + query
        + "&display="
        + str(display)
        + "&start="
        + str(start_index)
        + "&sort="
        + sort
    )

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        response_dict = json.loads(response_body.decode("utf-8"))
        items = response_dict["items"]

        for item_index in range(0, len(items)):
            remove_tag = re.compile("<.*?>")

            title = re.sub(remove_tag, "", items[item_index]["title"])
            link = items[item_index]["link"]
            image = items[item_index]["image"]
            author = items[item_index]["author"]
            price = items[item_index]["price"]
            discount = items[item_index]["discount"]
            publisher = items[item_index]["publisher"]
            isbn = items[item_index]["isbn"]
            description = re.sub(remove_tag, "", items[item_index]["description"])
            pubdate = items[item_index]["pubdate"]

            book_df.loc[idx] = [
                title,
                link,
                image,
                author,
                price,
                discount,
                publisher,
                isbn,
                description,
                pubdate,
            ]

            idx += 1
    else:
        print("Error Code:" + rescode)

book_df.to_json("일반소설.json", force_ascii=False)
book_df