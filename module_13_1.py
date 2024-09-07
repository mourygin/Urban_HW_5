# coding='UTF-8'
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование.')
    for i in range(1, 6):
        task_lift = asyncio.create_task(lifting(power))
        await task_lift
        print(f'Силач {name} поднял шар номер {i}')
    print(f'Силач {name} закончил соревнование.')

async def lifting(power):
    await asyncio.sleep(3/power)
    return


async def start_tournament():
    # asyncio.run(start_strongman('Геракл', 5))
    # asyncio.run(start_strongman('Аякс', 3))
    tasks = [start_strongman('Геракл', 5), start_strongman('Аякс', 3), start_strongman('Python', 9)]
    await asyncio.gather(*tasks)

asyncio.run(start_tournament())