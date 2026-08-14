from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Fake patterns (can be expanded)
fake_patterns = [
    "breaking shocking news",
    "you won't believe",
    "100% cure",
    "government conspiracy",
    "miracle solution",
    "secret revealed",
    "doctors hate this"
]

# ---------------- KMP ----------------
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                i += 1
    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            return True
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


# ---------------- UI ----------------
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Fake News Detector</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI';
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            width: 650px;
            padding: 30px;
            border-radius: 20px;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(20px);
            box-shadow: 0 0 25px rgba(0,0,0,0.4);
            text-align: center;
        }

        h1 {
            margin-bottom: 20px;
        }

        textarea {
            width: 100%;
            height: 150px;
            border-radius: 10px;
            border: none;
            padding: 10px;
            font-size: 16px;
        }

        button {
            margin-top: 20px;
            padding: 12px 30px;
            border: none;
            border-radius: 25px;
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            transform: scale(1.1);
        }

        #loader {
            display: none;
            margin-top: 15px;
        }

        #result {
            margin-top: 20px;
            font-size: 22px;
            font-weight: bold;
        }

        .bar {
            margin-top: 10px;
            height: 10px;
            background: #ddd;
            border-radius: 10px;
            overflow: hidden;
        }

        .fill {
            height: 100%;
            width: 0%;
            background: red;
            transition: 1s;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>📰 Fake News Detector</h1>

    <textarea id="text" placeholder="Paste news here..."></textarea>

    <button onclick="checkNews()">Analyze</button>

    <div id="loader">⏳ Analyzing...</div>

    <div id="result"></div>

    <div class="bar">
        <div id="fill" class="fill"></div>
    </div>
</div>

<script>
async function checkNews() {
    let text = document.getElementById("text").value;

    if (!text.trim()) {
        alert("Enter some news!");
        return;
    }

    document.getElementById("loader").style.display = "block";

    let res = await fetch("/check", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text: text})
    });

    let data = await res.json();

    document.getElementById("loader").style.display = "none";

    let resultDiv = document.getElementById("result");
    let fill = document.getElementById("fill");

    let score = data.score;

    fill.style.width = score + "%";

    if (data.result === "FAKE NEWS") {
        resultDiv.innerHTML = "🚨 FAKE NEWS<br>" + data.matched_patterns.join(", ");
        fill.style.background = "red";
    } else {
        resultDiv.innerHTML = "✅ REAL NEWS";
        fill.style.background = "green";
    }
}
</script>

</body>
</html>
"""

# ---------------- ROUTES ----------------
@app.route('/')
def home():
    return render_template_string(HTML_PAGE)


@app.route('/check', methods=['POST'])
def check():
    data = request.json
    text = data.get("text", "").lower()

    matched = []

    for pattern in fake_patterns:
        if kmp_search(text, pattern):
            matched.append(pattern)

    score = min(len(matched) * 20, 100)

    if matched:
        return jsonify({
            "result": "FAKE NEWS",
            "matched_patterns": matched,
            "score": score
        })
    else:
        return jsonify({
            "result": "REAL",
            "matched_patterns": [],
            "score": 10
        })


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)