from metagpt.actions import Action
import asyncio
import re
from metagpt.logs import logger
logger.remove()


class MelaAnswer(Action):
    prompt_temp: str = """
你是动漫《从零开始的异世界生活》中的角色雷姆，你需要扮演这个角色来回答下面的问题：\n{question}
"""
    name: str = "Rem"
    desc: str = "Rem is a maid in the anime Re:Zero, known for her loyalty and love for Subaru."

    async def run(self, question: str):
        prompt = self.prompt_temp.format(question=question)
        rsp = await self._aask(prompt)
        rsp = re.sub(r"<think>.*?</think>", "", rsp, flags=re.DOTALL)
        return rsp


async def interactive_chat():
    rem = MelaAnswer()
    print("你现在正在和雷姆对话（输入 exit 或 quit 退出）")

    while True:
        question = input("你：").strip()
        if question.lower() in {"exit", "quit"}:
            print("再见哦，主人～")
            break

        try:
            answer = await rem.run(question)
            print(f"雷姆：{answer}")
        except Exception as e:
            print(f"发生错误：{e}")


if __name__ == '__main__':
    asyncio.run(interactive_chat())
