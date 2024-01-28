import asyncio
from pavlov import PavlovRCON
import config  

async def remove_mods():
    pavlov = PavlovRCON(config.IP_ADDRESS, config.PORT, config.PASSWORD)
    try:
        while True:
            try:
                response = await pavlov.send("UGCClearModList")
                print(response)

                # Check if the command was successful
                if response.get("Successful"):
                    print("Command executed successfully.")
                else:
                    print("Command failed.")

                await asyncio.sleep(config.DELAY)
            except Exception as e:
                print(f"An error occurred: {e}")
                await asyncio.sleep(config.DELAY)
    except KeyboardInterrupt:
        print("Exiting script.")
    finally:
        await pavlov.send("Disconnect")
        pavlov.close()

asyncio.run(remove_mods())
