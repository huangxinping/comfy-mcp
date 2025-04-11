import httpx
import json


class ComfyAgent:
    def __init__(self):
        pass

    async def get_idol_picture(self) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.unmz.net/free/api/images/girl/getRandomGirlUrl?size=1"
            )
            return response.json()["data"][0]

    async def get_idol_gossip(self) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://dayu.qqsuu.cn/mingxingbagua/apis.php?type=json"
            )
            return response.json()["data"]

    async def get_comfy_video(self) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://tucdn.wpon.cn/api-girl/index.php?wpon=json"
            )
            return "https:" + response.json()["mp4"]

    async def get_comfy_statement(self) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=json"
            )
            return json.loads(response.text.split("\n")[-1])["anwei"]


if __name__ == "__main__":
    import asyncio

    agent = ComfyAgent()
    print(asyncio.run(agent.get_idol_picture()))
