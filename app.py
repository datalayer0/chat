from pathlib import Path
import chainlit as cl
import yaml

@cl.on_chat_start
def start():
   cl.Message("How can I help you today?").send()

@cl.on_message
async def main(message: str):
   await cl.Message(content=f"Received: {message}").send()

if __name__ == "__main__":
   cl.run()
