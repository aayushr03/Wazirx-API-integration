from wazirx_sapi_client.rest import Client
import time

# public
client = Client()
print(client.send("ping"))
print(client.send("time"))
print(client.send("system_status"))
print(client.send("exchange_info"))

# private
api_key = "4oXWPfRBqkGLE7YjLTZQ7aVOhZowAkjdrPi1QRsPIlLm98cevhY2kUFa6exmw5sd"
secret_key = "4kMJ4B0ljYHMtsUjSjDxdyxzSIobgzw5GqpyqYjz"

client = Client(api_key=api_key, secret_key=secret_key)

print(client.send("historical_trades",
             {"limit": 10, "symbol": "btcinr", "recvWindow": 10000, "timestamp": int(time.time() * 1000)}
             ))

print(client.send('create_order',
             {"symbol": "btcinr", "side": "buy", "type": "limit", "price": 500, "quantity": 1, "recvWindow": 10000,
              "timestamp": int(time.time() * 1000)}))