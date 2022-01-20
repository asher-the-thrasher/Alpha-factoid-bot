1) copy json_fields and paste into https://phrasefix.com/tools/remove-lines-containing-a-certain-word/ and remove lines that contain ": [" and "],":

2) copy and paste the results into jsonforreadme.json 

3) find and replace \n with <br> 

4) find and replace } with },

5) delete the last line

6) change first line from { to [

7) copy those results to https://kdelmonte.github.io/json-to-markdown-table/

8) copy the markdown results and paste into readME.md 

9) use https://markdowntohtml.com/ and take the results and put it in utils/website/assets/templates/commands.html with 

{% extends "basecommands.html" %} {% block content %} 

on top and 

{% endblock %}

on the bottom

9) commit and merge the results.