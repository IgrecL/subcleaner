# SubCleaner

This script is meant to be used with a condensed audio script like [impd](https://github.com/Ajatt-Tools/impd).<br>
Put the script in the folder containing the .srt and use the "py subcleaner.py {name of .srt file}" to run the script.

It deletes any line with 10 characters or less (max value can be changed), without counting what is inside parentheses, so that lines such as "ああ" or "（大きな物音）" are omitted when running impd.

This script greatly reduces the size of the condensed audios, by removing all the moments where there is music and no speech for example, as well as lines that are too short. For example, with the first episode of Trigun, this script deleted around 200 lines, leaving me with a 12 minutes audio file instead of a 18 minutes one, which is like half of the original length.

Even if some valid lines are deleted, it's not a big deal since they were short and probably easy. So this could also be used to filter only long sentences if you want your passive listening to be even denser.
