import back
import asyncio


def get_by_id():
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(
        back.get_by_id(
            70785, 961142, phones=True, city=True, title="True", address=True
        )
    )


def get_by_provider_id():
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(back.get_by_provider_id())
