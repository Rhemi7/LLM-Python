import os
import requests


def scrape_linkedin_profile(profile_url: str):
    """scrape information from Linkedin profiles,
    Manually scrape the information from the Linkedin profile
    """
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    api_endpoint = "https://gist.githubusercontent.com/Rhemi7/8d506da63394c5e33393ab89689dacc7/raw/5140236f333c2834100394a5de5752030982a583/remi.json"
    headers = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(api_endpoint,
                            #  params={"url": profile_url}, headers=headers
                            )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
