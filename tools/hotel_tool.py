import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Hoteltool:

    def __init__(self):
        self.api_key = os.getenv("hotel_api_key")

    def search_hotels(self, city):

        url = "https://places.googleapis.com/v1/places:searchText"

        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": self.api_key,
            "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.rating,places.photos"
        }

        body = {
            "textQuery": f"Hotels in {city}"
        }

        response = requests.post(url, headers=headers, json=body)

        if response.status_code != 200:
            print(response.text)
            return []

        data = response.json()

        hotels = []

        for hotel in data.get("places", [])[:5]:

            images = []

            if "photos" in hotel:

                for photo in hotel["photos"][:3]:

                    images.append(
                        f"/hotel-photo?photo={photo['name']}"
                    )

            while len(images) < 3:

                images.append(
                    "https://via.placeholder.com/300x200?text=No+Image"
                )

            hotels.append({

                "name": hotel["displayName"]["text"],

                "rating": hotel.get("rating", "N/A"),

                "address": hotel.get("formattedAddress", ""),

                "images": images,

                "link": f"https://www.google.com/maps/place/?q=place_id:{hotel['id']}"

            })
            print(hotel)

        return hotels