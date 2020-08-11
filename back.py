import aiohttp
import asyncio
import config
import xml.etree.ElementTree as ET


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_by_provider_id(provider, *ids, **params):
    async with aiohttp.ClientSession(
        auth=aiohttp.BasicAuth(config.username, config.password)
    ) as session:
        full_result = []
        full_result.append("provider:" + str(provider)) if len(ids) > 1 else ""
        for id in ids:
            html = await fetch(
                session, config.provider_url + str(provider) + "/" + str(id)
            )
            print(config.provider_url + str(provider) + "/" + str(id))
            result = []
            if len(ids) > 1:
                result.append("id:" + str(id))

            tree = ET.ElementTree(ET.fromstring(html))
            root = tree.getroot()

            for group in root.findall("property"):
                if params:
                    if params.get("address"):
                        element = (
                            group.find("addresses")
                            .find("address")
                            .find("addressLine")
                            .text
                        )
                        result.append(element)
                    if params.get("title"):
                        element = group.find("name")
                        result.append(element.text)
                    if params.get("city"):
                        element = group.find("city")
                        result.append(element.text)
                    if params.get("phones") and group.find("phones"):
                        phones = group.find("phones").findall("phone")
                        phones_text = []
                        for phone in phones:
                            phones_text.append(phone.text)
                        result.append(phones_text)
                    if params.get("country"):
                        element = group.find("country")
                        result.append(element.text)
                    if params.get("emails") and group.find("emails"):
                        emails = group.find("emails").findall("email")
                        emails_text = []
                        for email in emails:
                            emails_text.append(email.text)
                        result.append(emails_text)
                else:
                    if len(ids) == 1:
                        return html
                    result.append(html)

            full_result.append(result)
        return full_result


async def get_by_id(*ids, **params):
    async with aiohttp.ClientSession(
        auth=aiohttp.BasicAuth(config.username, config.password)
    ) as session:
        full_result = []
        # full_result.append('provider:'+  if len(ids)>1 else ''

        for id in ids:
            html = await fetch(session, config.giata_id_url + str(id))
            print(config.giata_id_url + str(id))
            result = []
            if len(ids) > 1:
                result.append("id:" + str(id))
            tree = ET.ElementTree(ET.fromstring(html))
            root = tree.getroot()

            for group in root.findall("property"):
                if params:
                    if params.get("address"):
                        element = (
                            group.find("addresses")
                            .find("address")
                            .find("addressLine")
                            .text
                        )
                        result.append(element)
                    if params.get("title"):
                        element = group.find("name")
                        result.append(element.text)
                    if params.get("city"):
                        element = group.find("city")
                        result.append(element.text)
                    if params.get("phones"):
                        phones = group.find("phones").findall("phone")
                        phones_text = []
                        for phone in phones:
                            phones_text.append(phone.text)
                        result.append(phones_text)
                    if params.get("country"):
                        element = group.find("country")
                        result.append(element.text)
                    if params.get("emails"):
                        emails = group.find("emails").findall("email")
                        emails_text = []
                        for email in emails:
                            emails_text.append(email.text)
                        result.append(emails_text)
                else:
                    if len(ids) == 1:
                        return html
                    result.append(html)
            full_result.append(result)
        return full_result


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # test = loop.run_until_complete(
    #     # get_by_id(70785, 961142, phones=True, city=True, title="True", address=True)
    #     get_by_id(70785, 961142, phones=True, emails=True, title=True)
    # )
    # test = loop.run_until_complete(get_by_id(70785))
    test = loop.run_until_complete(get_by_provider_id("amadeus", "WYORD998"))
    print(test)
