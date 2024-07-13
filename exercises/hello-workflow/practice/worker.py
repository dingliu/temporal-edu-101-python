import asyncio
from enum import Enum

from temporalio.client import Client
from temporalio.worker import Worker

from greeting import GreetSomeone


class TaskQueue(Enum):
    GREETING_TASK_QUEUE = "greeting-tasks"


async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client,
        task_queue=TaskQueue.GREETING_TASK_QUEUE.value,
        workflows=[GreetSomeone],
    )
    print("Starting worker...")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
