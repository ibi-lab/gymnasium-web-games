import modal
from pathlib import Path

html_dir = Path(__file__).parent.resolve()

app = modal.App(
    "gymnasium-portal",
    image=modal.Image.debian_slim()
    .pip_install("flask")
    .add_local_dir(html_dir, remote_path="/html"),
)

@app.function()
@modal.wsgi_app()
def flask_app():
    from flask import Flask, send_from_directory, render_template_string

    web_app = Flask(__name__)

    @web_app.get("/")
    def home():
        html_content = """
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Gymnasium Games Portal</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body { background-color: #f8f9fa; }
                .card { transition: transform 0.2s; }
                .card:hover { transform: translateY(-5px); }
            </style>
        </head>
        <body>
            <div class="container py-5">
                <div class="text-center mb-5">
                    <h1 class="display-4 fw-bold text-primary">Gymnasium Games Portal</h1>
                    <p class="lead text-muted">各環境（ゲーム）のシミュレーションガイドを選択してください。</p>
                </div>
                
                <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
                    <div class="col">
                        <div class="card h-100 shadow-sm border-0">
                            <div class="card-body">
                                <h5 class="card-title text-success fw-bold">CartPole</h5>
                                <p class="card-text text-muted">ポールを立てたままカートを制御する古典的な問題。</p>
                                <a href="/games/cartpole.html" class="btn btn-outline-success w-100">プレイする</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card h-100 shadow-sm border-0">
                            <div class="card-body">
                                <h5 class="card-title text-success fw-bold">MountainCar</h5>
                                <p class="card-text text-muted">非力な車を勢いをつけて山の上に到達させる問題。</p>
                                <a href="/games/mountaincar.html" class="btn btn-outline-success w-100">プレイする</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card h-100 shadow-sm border-0">
                            <div class="card-body">
                                <h5 class="card-title text-success fw-bold">LunarLander</h5>
                                <p class="card-text text-muted">月面着陸船を目標地点に安全に着陸させる問題。</p>
                                <a href="/games/lunarlander.html" class="btn btn-outline-success w-100">プレイする</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card h-100 shadow-sm border-0">
                            <div class="card-body">
                                <h5 class="card-title text-success fw-bold">BipedalWalker</h5>
                                <p class="card-text text-muted">二足歩行ロボットを進ませる強化学習の難問。</p>
                                <a href="/games/bipedalwalker.html" class="btn btn-outline-success w-100">プレイする</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card h-100 shadow-sm border-0">
                            <div class="card-body">
                                <h5 class="card-title text-success fw-bold">CarRacing</h5>
                                <p class="card-text text-muted">ランダムに生成されるコースで車を走らせる問題。</p>
                                <a href="/games/carracing.html" class="btn btn-outline-success w-100">プレイする</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <footer class="text-center mt-5 py-4 text-muted">
                <small>&copy; 2026 Gymnasium Portal</small>
            </footer>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        """
        return render_template_string(html_content)

    @web_app.get("/games/<path:filename>")
    def serve_game(filename):
        return send_from_directory("/html", filename)

    return web_app
