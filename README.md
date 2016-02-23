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


##File List

*b1.txt* - This is a body paragraph template for use with the paragraph.py script

*b2.txt* - This is a body paragraph template for use with the paragraph.py script

*flaskillinois.py* - This is the flask app used to execute the paragraph script.  When a user navigates to either of the target.html pages, it runs the paragraph.py and push2html.py scripts and serves the resultant page.

*index.html* - Our main landing site, with links to the two target sites

*index_1.html* - Artifact of previous testing

*nocache.py* - A flask script that ensures our page is not cached.  Caching interferes with the way we update the content, we want a request to be made every time a user visits target.html.

*p1.txt* - This is a general paragraph template for use with the paragraph.py script

*p2.txt* - This is a general paragraph template for use with the paragraph.py script

*p3.txt* - This is a general paragraph template for use with the paragraph.py script

*paragraph.py* - This script generates a populated paragraph template, using a template argument and lists of filler words.  It may be used as is (see instructions), or called as a part of the flask app

*push2html.py* - This automates the content generation by calling the paragraph.py script with appropriate templates, catching the returned strings, and injecting them into the target.html code.  Note that the use of a unique terget string is used to make sure sed behaves well - do not use it without first adding such a string to the template1.html or template2.html files.

*quote1.txt* - This is a quote paragraph template for use with the paragraph.py script

*quote2.txt* - This is a quote paragraph template for use with the paragraph.py script

*quote3.txt* - This is a quote paragraph template for use with the paragraph.py script

*target1.html* - This is one of two html files which is modified by push2html.py in order to serve a new website.  See push2html.py,template1.html, or template2.html for details as to how this happens.

*target2.html* - This is one of two html files which is modified by push2html.py in order to serve a new website.  See push2html.py,template1.html, or template2.html for details as to how this happens.

*template.html* - Artifact of previous testing

*template1.html* - This is one of two website designs used to generate target.html.  Every time push2html.py is called, one of these templates will be copied over to target.html.  The scripts will then replace the target strings with the generated paragraphs.

*template2.html* - This is one of two website designs used to generate target.html.  Every time push2html.py is called, one of these templates will be copied over to target.html.  The scripts will then replace the target strings with the generated paragraphs.
