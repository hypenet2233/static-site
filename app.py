import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Python service is running ✅"

@app.route("/healthz")
def health():
    return jsonify(ok=True)

# مثال: نقطة نهاية مستقبلًا تقرأ من uploads/ وتكتب في processing/
@app.route("/process")
def process():
    uploads_dir = os.path.join(os.getcwd(), "uploads")
    processing_dir = os.path.join(os.getcwd(), "processing")
    os.makedirs(processing_dir, exist_ok=True)
    # هنا تحط منطقك الحقيقي للمعالجة
    return jsonify(msg="processing stub", uploads=uploads_dir, output=processing_dir)

if __name__ == "__main__":
    # Render يمرّر البورت عبر متغير البيئة PORT
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
