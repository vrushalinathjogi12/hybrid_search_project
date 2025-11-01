from flask import Flask, render_template, request, jsonify
import os, csv
from trie import Trie
from hashmap import HashMap

# Tell Flask where to find frontend templates
app = Flask(__name__, template_folder="../frontend/templates")

trie = Trie()
hashmap = HashMap()
search_history = []

CSV_PATH = os.path.join(os.path.dirname(__file__), "keywords.csv")



# Load keywords into Trie and HashMap
def load_keywords():
    if not os.path.exists(CSV_PATH):
        print(f"⚠️ keywords.csv not found at {CSV_PATH}")
        return

    with open(CSV_PATH, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header if any
        for row in reader:
            if len(row) < 2:
                continue
            word = row[0].strip()
            try:
                freq = int(row[1])
            except ValueError:
                freq = 1
            trie.insert(word)
            hashmap.add(word, freq)
    print(f"✅ Loaded {len(hashmap.data)} keywords from {CSV_PATH}")


# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    global search_history
    keyword = ""
    suggestions = []
    exact_match = False

    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip().lower()

        if keyword:
            search_history.append(keyword)
            suggestions = trie.starts_with(keyword)
            exact_match = hashmap.exists(keyword)

    return render_template("index.html",
                           keyword=keyword,
                           suggestions=suggestions,
                           exact_match=exact_match,
                           history=search_history)


# API endpoint to clear search history
@app.route("/clear_history", methods=["POST"])
def clear_history():
    global search_history
    search_history.clear()
    return jsonify({"message": "🧹 Search history cleared successfully!"})


if __name__ == "__main__":
    load_keywords()
    app.run(debug=True)
