# Star Wars Imperial Assault - RAIV helper script

This is a little helper script to manage easily the event deck needed for RAIV Star Wars Imperial Assault variant.
Please visit [bgg](https://boardgamegeek.com/thread/2189979/redjaks-automated-imperial-expanded) for more info.

What you need:
- A working installation of python (version 3. version 2 might work as well.)
- A list of the RAIV cards as single jpg files as downloaded on the drive. More precisely download the folder 'Cards - Single JPGs', put it at the root of the project and rename it 'cards'.

Instructions:
- cd into the root dir and run `python script.sh'. Choose option 1. It'll create a 'campaign' dir and put every event card needed for a campaign into the folder 'event_deck'.
- After every mission run the script again and choose option 2 or 3 depending on a rebel win or loss.
- While playing, draw event card from the 'event_deck' folder, they are already shuffled.
- Enjoy!

Thanks.
