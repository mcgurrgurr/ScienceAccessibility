# Scientific readability project

Executing these files is not yet straight forward, as the execution environment is dependency heavy. Docker is used to solve non trivial software dependency issues where possible.

If docker is installed on the base OS, git clone this repository, and assuming the file build.sh is chmod +x , run: `bash build.sh` to perform the dockerbuild. To run the jupyter notebook over docker, enter the docker enivornment interactively in one of two ways, via a bash shell, or via an ipython notebook or
and then launch python via BASH in Linux as follows:

```
'cd this_path; sudo docker run -it -v this_path:/home/jovyan slc'
```

Maybe define a bash alias, if this command get's too big and old.

```
alias drvt='cd this_path; sudo docker run -v this_path:/home/jovyan slc'
```

To Run the project, you need navigaate to the Examples directory and then execute:
`python use_scrape.py`, which scrapes search engines for parameters defined in that file.
Once that is done an analysis program `use_analysis` is then called to run an analysis on the scraped text. This program generates some simple figures. The figures are very basic, and they act to function only as proof of concept.

Given pre-existing data (pickled files consisiting of raw text contents), the analysis file can also be run on it's own by executing: `python use_analysis.py`. To analyse the scraped texts, the jupyter notebook: `vstrl.ipynb` also contains idioms for plotting and analysis based on scrapped data, although it is not maintained. The package bokeh, facilitates pretty interactive plots with data point mouse over data metrics.

Another file `Examples/use_code_complexity.py` reports back about the complexity of the code, used to analyse the complexity of language. Not the code complexity analysis is not thorough enough to include third party modules that were heavily utilized in the analysis, however, the principle of code complexity, with an application limited scope is generally applied in our approach, as it's not desirable to use obfuscated code, as a tool used to advocate for simple language.

Note: a lot of complexity in the code base comes from the need to masquerade as a non bot web surfer.
It's a bad idea to surf naked ie to only use: `urllib`, or `requests`, as these resource grabbers are sure fire bot give aways.
`Selenium`, `Google Scrape` (uses Selenium), and `delver Crawler`, are the surfing clothes I used; they work together to prolong a period feigned humanhood.
The downloading of pdf's as opposed to html usually occurs in the nude, but this does not seem to cause any problems.

Search Engine: 'who are you?' code: 'I am an honest human centric browser, and certainly not a robot surfing in the nude'. Search Engine: 'great, great, I'd love to get to know you, before I can share my resources, I need to make sure that you will store records of our interactions together, that I may reread on future dates'. Code: 'creepy, I mean, cool, yes, sure!' SE: 'great here are some pages'. Time elapses and reality is exposed just like in 'the Emperors New Clothes'.
