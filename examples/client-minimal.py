import asyncio
import sys
# sys.path.insert(0, "..")
import logging
from asyncua import Client, Node, ua

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')


async def main():
    url = 'opc.tcp://192.168.250.1:4840/'
    async with Client(url=url) as client:
        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        # Node objects have methods to read and write node attributes as well as browse or populate address space
        keepSessionAlive:  True
        
        _logger.info('Children of root are: %r', await client.nodes.root.get_children())
        _logger.info("Objects node is: %r", client.nodes.root)
        
        print()

        arr = await client.get_namespace_array()
        print("arr:\n", arr)

        node = client.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_State))
        print("\nnode:\n", node)

        root = client.get_root_node()
        print("\nroot:\n", await root.get_children())

        print()
 
        # change the s=value as desired
        var1node = client.get_node("ns=4;s=READ_DATA_VALUES")
        var1val = await var1node.get_value()
        print("\nvar1val:\n", var1val)
        print()


if __name__ == '__main__':
    asyncio.run(main())
