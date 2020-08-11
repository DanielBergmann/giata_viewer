import back
import asyncio


def get_by_id(*ids, **params):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(back.get_by_id(*ids, **params))


def get_by_provider_id(provider, *ids, **params):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(back.get_by_provider_id(provider, *ids, **params))
