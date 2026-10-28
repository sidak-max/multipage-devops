from flask import Flask, render_template_string

app = Flask(__name__)
VERSION = "v1"
FEATURES = "One Page - Basic UI"

@app.route("/")
def home():
    return render_template_string("""
    <!doctype html>
    <html><head><title>Multi-page App v1</title></head>
    <body style="font-family:Arial;background:#f2f5f9;margin:40px">
      <header style="background:#26394c;color:white;padding:18px">
        Multi-page App | v1 | One Page - Basic UI
      </header>
      <h2>Welcome to my Multi-page App</h2>
      <p>This is the home page. Version 1 has only one page with a basic user interface.</p>
      <h3>About this version</h3>
      <p>Pages available: 1 (Home)</p>
    </body></html>
    """)

@app.route("/health")
def health():
    return {"status": "ok", "version": VERSION}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
