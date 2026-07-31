from tools.hotel_tool import Hoteltool


class HotelAgent:

    def __init__(self):
        self.hotel_tool = Hoteltool()

    def get_hotels(self, city):

        hotels = self.hotel_tool.search_hotels(city)

        if not hotels:
            return "<h3>No Hotels Found</h3>"

        result = """
        <h2 style="margin-bottom:25px;color:#4f46e5;">
            🏨 Recommended Hotels
        </h2>
        """

        for hotel in hotels:

            images_html = ""

            for image in hotel["images"]:

                images_html += f"""
                    <img
                        src="{image}"
                        style="
                            width:31%;
                            height:180px;
                            object-fit:cover;
                            border-radius:10px;
                            margin-right:8px;
                        "
                    >
                """

            result += f"""

            <div style="
                background:white;
                margin-bottom:30px;
                padding:20px;
                border-radius:15px;
                box-shadow:0 8px 20px rgba(0,0,0,.12);
            ">

                <div style="
                    display:flex;
                    gap:10px;
                    margin-bottom:20px;
                ">

                    {images_html}

                </div>

                <h3 style="color:#4f46e5;">
                    {hotel['name']}
                </h3>

                <p style="margin:8px 0;">
                    ⭐ <b>Rating:</b> {hotel['rating']}
                </p>

                <p style="margin:8px 0;">
                    📍 {hotel['address']}
                </p>

                <a
                    href="{hotel['link']}"
                    target="_blank"
                    style="
                        display:inline-block;
                        margin-top:12px;
                        background:#4f46e5;
                        color:white;
                        text-decoration:none;
                        padding:10px 18px;
                        border-radius:8px;
                    "
                >
                    📍 Open in Google Maps
                </a>

            </div>

            """

        return result