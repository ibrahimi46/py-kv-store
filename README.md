# py-kv-store

A lightweight, in-memory key-value store built from scratch using Python's socket library.

I built this project to understand the low-level fundamentals of database architecture and TCP networking. It functions similarly to Redis, listening on a specific port and processing text-based commands to store or retrieve data, but it runs without any external frameworks.

Currently, it handles a single connection at a time and stores data in a standard Python dictionary.

## How to Run

You will need two terminal windows: one for the server and one for the client.

1. Start the server:
   python app/server.py

2. In a second terminal, start the client:
   python app/client.py

## Commands

Once the client is connected, you can use the following commands:

- SET key value: Saves a value to the store.
  Example: SET name Ibrahim

- GET key: Retrieves the value associated with the key.
  Example: GET name

- EXIT: Closes the connection.
