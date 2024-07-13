import asyncio
import aiohttp

from enum import Enum

from temporalio.client import Client
from temporalio.worker import Worker

from translate import TranslateActivities
from greeting import GreetSomeone


class TaskQueue(Enum):
    GREETING_TASK_QUEUE = "greeting-tasks"


async def main():
    client = await Client.connect("localhost:7233", namespace="default")

    # Run the worker
    async with aiohttp.ClientSession() as session:
        activities = TranslateActivities(session)

        worker = Worker(
            client,
            task_queue=TaskQueue.GREETING_TASK_QUEUE.value,
            workflows=[GreetSomeone],
            activities=[
                activities.greet_in_spanish,
                activities.farewell_in_spanish,
            ]
        )
        print("Starting the worker....")
        await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
