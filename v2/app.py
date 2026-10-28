from flask import Flask, render_template_string

app = Flask(__name__)
VERSION = "v2"
FEATURES = "Two Pages - Home and About"

def render_page(title, body):
    return render_template_string("""
    <!doctype html>
    <html><head><title>Multi-page App v2</title></head>
    <body style="font-family:Arial;background:#f2f5f9;margin:40px">
      <header style="background:#26394c;color:white;padding:18px">
        Multi-page App | v2 | Two Pages - Home and About
      </header>
      <h2>{{ title }}</h2><p>{{ body }}</p>
      <h3>About this version</h3>
      <p>Pages available: 2 (Home and About). There are no navigation links yet.</p>
    </body></html>
    """, title=title, body=body)

@app.route("/")
def home():
    return render_page("Welcome to my Multi-page App",
                       "This is the home page. Version 2 adds an About page.")

@app.route("/about")
def about():
    return render_page("About Page",
                       "This is the second page of the app. It has its own address: /about.")

@app.route("/health")
def health():
    return {"status": "ok", "version": VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
