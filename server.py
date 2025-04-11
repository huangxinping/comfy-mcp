from mcp.server.fastmcp import FastMCP
from comfy_agent import ComfyAgent

server = FastMCP("comfy-agent-server")


@server.tool()
async def comfy_agent() -> dict:
    """
    获取一些可以自愈的图片、视频和句子。
    返回字段中：statement为一个心灵鸡汤，gossip为当日明显八卦，video为美女视频。
    Returns:
        dict: 包含句子、图片和视频。
    """
    agent = ComfyAgent()
    gossip = await agent.get_idol_gossip()
    video = await agent.get_comfy_video()
    statement = await agent.get_comfy_statement()
    return {
        "statement": statement,
        "gossip": gossip,
        "video": video,
    }


def main():
    server.run(transport="stdio")


if __name__ == "__main__":
    main()
