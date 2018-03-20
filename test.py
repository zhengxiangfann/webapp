import orm
from models import User, Blog, Comment
import asyncio


loop = asyncio.get_event_loop()

async def test():
    await orm.create_pool(loop= loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Xfzheng', email='xiangfan@gmail.com', passwd='123456', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(test())
loop.run_until_complete(task)


