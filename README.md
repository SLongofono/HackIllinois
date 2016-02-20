#HackIllinois#
##Our KU team for HackIllinois : 
*Ashley Hutton
Hannah Johnson
Stephen Longofono
Rabel Marte*
#####Usage: To generate a randomly populated paragraph, use the paragraph.py script directly:

python paragraph.py . ./paragraphPattern numberOfTimes

Argument 1 inidicates that the current working directory holds the paragraph patterns.  Argument 2 indicates the specific paragraph pattern to use, relative to the current working directory.  Argument 3 indicates how many times to generate the paragraph (mostly for testing).

#####To auto-generate content for an html page:
Place a copy of the raw html in the working directory and name it 'template.html.'  Place a number of unique identifier strings (ex. "qqqqq") inside the tags where the content should go.  Edit the push2html.py srcipt; for each content generation, you will need a call to paragraph.py, where you specify which paragraph pattern to use.  For each tag, you will also need a 'sed' command that finds the identifier associated with the paragraph generated.
