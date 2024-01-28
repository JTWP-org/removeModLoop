import asyncio
from pavlov import PavlovRCON
import config  

async def remove_mods():
    while True:
        try:
            
            pavlov = PavlovRCON(config.IP_ADDRESS, config.PORT, config.PASSWORD)

            
            response = await pavlov.send("UGCClearModList")
            print(response)


            
            await pavlov.send("Disconnect")
            pavlov.close()

        except Exception as e:
            print(f"An error occurred: {e}")

        
        await asyncio.sleep(config.DELAY)  # Waits for 60 seconds before the next loop

asyncio.run(remove_mods())
