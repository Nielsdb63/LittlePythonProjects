Here follows a short discription of the files in this repository:

- Snakes_and_ladders.ipynb

March 2025
I was watching a youtube video (https://www.youtube.com/watch?v=k2ixp5VozIs) of two guys playing snakes and ladders, but with the twist that every ladder was now a snake. If that was not enough, they decided that everytime one goes down a snake, they have to take a shot. I wondered how many shots they would have to take if they stuck to the rules, so I decided to model the game and simulate the results. This was very easy as snakes and ladders does not have a strategy, it is simply a 100% luck-based dice game. 
Simulating 1000000 games using the normal rules gives a [minimum, maximum, mean, median, mode] number of throws of [7, 569, 56.68, 45, 24]. If we use their rules we get for the [minimum, maximum, mean, median, mode] number of throws [20, 6228, 524.14, 374, 50]. This corresponds to the taking of a [minimum, maximum, mean, median, mode] of shots of [0, 993, 78.52, 55, 8]. 
Funnily enough, the hosts of the game realized this version might take a lot longer, and they decided to cut it after 30 minutes. At this point one of the players had had 9, and the other 14, shots. They were at positions 28 and 16 respectively. 

