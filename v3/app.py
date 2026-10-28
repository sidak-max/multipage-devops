from flask import Flask, render_template_string, url_for

app = Flask(__name__)
VERSION = "v3"
FEATURES = "Two Pages - Navigation"

def render_page(title, body):
    return render_template_string("""
    <!doctype html>
    <html><head><title>Multi-page App v3</title></head>
    <body style="font-family:Arial;background:#f2f5f9;margin:40px">
      <header style="background:#26394c;color:white;padding:18px">
        Multi-page App | v3 | Two Pages - Navigation
        <nav style="margin-top:12px">
          <a href="{{ url_for('home') }}" style="color:white;margin-right:16px">Home</a>
          <a href="{{ url_for('about') }}" style="color:white">About</a>
        </nav>
      </header>
      <h2>{{ title }}</h2><p>{{ body }}</p>
      <h3>About this version</h3>
      <p>Use the Home and About links to move between pages.</p>
    </body></html>
    """, title=title, body=body)

@app.route("/")
def home():
    return render_page("Welcome to my Multi-page App",
                       "Version 3 links the pages with a navigation bar.")

@app.route("/about")
def about():
    return render_page("About Page",
                       "You reached the About page using the navigation bar.")

@app.route("/health")
def health():
    return {"status": "ok", "version": VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
