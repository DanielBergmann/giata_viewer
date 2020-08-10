import aiohttp
import asyncio
import config
import xml.etree.ElementTree as ET


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_by_id(*ids, **params):
    async with aiohttp.ClientSession(
        auth=aiohttp.BasicAuth(config.username, config.password)
    ) as session:
        full_result = []
        for id in ids:
            html = await fetch(session, config.giata_id_url + str(id))
            result = []
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
                        element = group.find("city")
                        result.append(element.text)
                    if params.get("city"):
                        element = group.find("name")
                        result.append(element.text)
                    if params.get("phones"):
                        phones = group.find("phones").findall("phone")
                        phones_text = []
                        for phone in phones:
                            phones_text.append(phone.text)
                        result.append(phones_text)
                else:
                    result = html
            full_result.append(result)
        return full_result


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    test = loop.run_until_complete(
        get_by_id(70785, 961142, phones=True, city=True, title="True", address=True)
    )
    # test = loop.run_until_complete(get_by_id(70785,961142))

    print(test)
