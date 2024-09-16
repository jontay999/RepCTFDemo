from flask import Flask, request, render_template_string

app = Flask(__name__)

page_header = """
<!doctype html>
<html>
<head><style>
body {
  background: #1a1a1a;
  height: 100vh;
  color: #eee;
  font-family: Calibri, Helvetica, sans-serif;
  margin: auto;
  font-size: 40px;
  text-align: center;
}
</style></head>
  <body id="level1">
      <div style="height:100%; display:grid; place-items:center">
"""

page_footer = """
      </div>
  </body>
</html>
"""

main_page_markup = """
<form action="/" method="GET">
  <input id="query" name="query" value="Enter query here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""

@app.route('/', methods=['GET'])
def main_page():
    query = request.args.get('query')
    if not query:
        # Show main search page
        return render_template_string(page_header + main_page_markup + page_footer)
    else:
        # No results found
        message = f"Sorry, no results were found for <b>{query}</b>."
        message += " <a href='/'>Try again</a>."
        # Display the results page
        return render_template_string(page_header + message + page_footer)

if __name__ == '__main__':
    app.run(debug=True)