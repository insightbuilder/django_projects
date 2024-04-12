from websockets import serve
from peewee import (
    SqliteDatabase,
)
from peeweemodels import ShopQuestions
import asyncio
import os
import logging
import json
import random

logging.basicConfig(format="%(message)s|%(levelname)s",
                    level=logging.INFO)

# no need as the tables are imported from peeweemodels
# db = SqliteDatabase("D:\\gitFolders\\django_projects\\streamdjango\\db.sqlite3")
# db.connect()

async def socket_llm(websocket):
    async for msg in websocket:
        if msg == 'give_data':
            if ShopQuestions.select():
                logging.info("Got SQL data...")
                for data in ShopQuestions.select():
                    row = dict(user_prompt=data.prompt,
                            llm_reply=data.answer)

                    out_data = {"ptbl": row}

                    out_str = json.dumps(out_data)
                    logging.info(out_str)
                    await websocket.send(out_str)

                    await asyncio.sleep(random.randint(0, 5) + 1)
            else:
                send_data = {"ptbl": "Table deleted"}
                await websocket.send(json.dumps(send_data))


async def main():
    async with serve(socket_llm, 'localhost', 7568):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
