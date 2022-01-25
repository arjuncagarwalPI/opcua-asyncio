import asyncio
import time
from asyncua import Client

#logging.basicConfig(level=logging.INFO)
#_logger = logging.getLogger('asyncua')


async def main():
    url = 'opc.tcp://192.168.250.1:4840/'
    async with Client(url=url) as client:
        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        # Node objects have methods to read and write node attributes as well as browse or populate address space
        start_time = time.time()
        for i in range(100):
            keepSessionAlive:  True
            #_logger.info('Children of root are: %r', await client.nodes.root.get_children())
            #_logger.info("Objects node is: %r", client.nodes.root)

            '''print()

            arr = await client.get_namespace_array()
            print("arr:\n", arr)

            node = client.get_node(ua.NodeId(ua.ObjectIds.Server_ServerStatus_State))
            print("\nnode:\n", node)

            root = client.get_root_node()
            print("\nroot:\n", await root.get_children())

            print()'''
    
            # change the s=value as desired
            #names_1_node = client.get_node("ns=4;s=READ_DATA_NAMES_1")
            #names_1_val = await names_1_node.get_value()
            #print("\nREAD_DATA_NAMES_1:\n", names_1_val)
            #print()
            #names_2_node = client.get_node("ns=4;s=READ_DATA_NAMES_2")
            #names_2_val = await names_2_node.get_value()
            #print("\nREAD_DATA_NAMES_2:\n", names_2_val)
            #print()
            #units_node = client.get_node("ns=4;s=READ_DATA_UNITS")
            #units_val = await units_node.get_value()
            #print("\nREAD_DATA_UNITS:\n", units_val)
            #print()
            values_node = client.get_node("ns=4;s=READ_DATA_VALUES")
            values_val = await values_node.get_value()
            print("\nREAD_DATA_VALUES:\n", values_val)
            #print()
            #print('\nTime:', time.time())
            print('Time elapsed:', time.time() - start_time)
            #print()


if __name__ == '__main__':
    asyncio.run(main())
