"""
For public streams, api_key and secret_key is not required i.e.
    ws_client = WebsocketClient()
For private streams, api_key, secret_key are required while initialising WebsocketClient i.e.
    ws_client = WebsocketClient(api_key=api_key, secret_key=secret_key)

"""

from wazirx_sapi_client.websocket import WebsocketClient

api_key = "4oXWPfRBqkGLE7YjLTZQ7aVOhZowAkjdrPi1QRsPIlLm98cevhY2kUFa6exmw5sd"
secret_key = "4kMJ4B0ljYHMtsUjSjDxdyxzSIobgzw5GqpyqYjz"
ws_client = WebsocketClient(api_key=api_key, secret_key=secret_key)

asyncio.create_task(
    ws_client.connect(
    )
)

# to subscribe
await ws_client.subscribe(
    events=["btcinr@depth"],
)

await ws_client.subscribe(
    events=["wrxinr@depth"],
    id=1  # id param not mandatory
)

await ws_client.subscribe(
    events=["orderUpdate"]
)

await ws_client.subscribe(
    events=["outboundAccountPosition"],
    id=2  # id param not mandatory
)

### to unsubscribe
#await ws_client.unsubscribe(
#    events=["outboundAccountPosition", "wrxinr@depth"],
#)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()