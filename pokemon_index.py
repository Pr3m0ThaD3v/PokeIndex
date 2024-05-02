# A simple tool for querying information about Pokemon
# Import aiopoke

import asyncio
import aiopoke


# function to fetch Pokemon data
# This function uses aiopokeapi to retrieve Pokemon data based on their name.
async def main():
    async with aiopoke.AiopokeClient() as client:
        pokemon_list = await client.get_pokemon("pokemon")
        pokemon_names = [pokemon.name for pokemon in pokemon_list.results]

        while True:
            pokemon_name = input("Enter a Pokemon name (or press 'q' to quit): ").lower()
            if pokemon_name == "q":
                break

            if pokemon_name not in pokemon_names:
                print(f"Pokemon '{pokemon_name}' not found.")
                continue

            pokemon_data = await client.get_pokemon(pokemon_name)

            # Access and display info
            print(f"Name: {pokemon_data.name}")
            print(f"status")
            for stat in pokemon_data.stats:
                print(f"\t- {stat.name}: {stat.base_stat}")

            # Extract and process abilities, strengths, and weaknesses
            print(f"Abilities:")
            for ability in pokemon_data.abilities:
                ability_data = await ability.ability.fetch()
                print(f"\t- {{type_data.name}}")
                
            # Determine strengths and weaknesses based on type matchups
            # You can implement your own logic here

if __name__ == "__main__":
    asyncio.run(main())