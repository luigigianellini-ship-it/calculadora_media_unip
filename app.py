from flask import Flask, render_template, request
import funcoes

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    historico = []
    resultado = None
    if request.method == "POST":
        acao = request.form.get("acao")
        if acao == "media":
            np1 = float(request.form["np1"])
            np2 = float(request.form["np2"])
            pim = float(request.form["pim"])

            resultado = funcoes.media(np1, np2, pim)
            historico.append({
    "tipo": "Média",
    "NP1": np1,
    "NP2": np2,
    "PIM": pim,
    "Resultado": resultado
})
        elif acao == "pim":
            np1 = float(request.form["np1"])
            np2 = float(request.form["np2"])

            resultado = funcoes.especular(np1, np2)
            historico.append({
    "tipo": "Especulação PIM",
    "NP1": np1,
    "NP2": np2,
    "Resultado": resultado
})
        elif acao == "exame":
            media = float(request.form["media"])
            exame = float(request.form["exame"])

            nota = funcoes.exame(media, exame)
            if nota >= 5:
                resultado = f"{nota} no exame: Aprovado"
            else:
                resultado = f"{nota} no exame: Reprovado"
            historico.append({
    "tipo": "Exame",
    "Média": media,
    "Exame": exame,
    "Resultado": resultado
})
            
    return render_template("index.html", resultado=resultado, historico=historico)
if __name__ == "__main__":
    app.run(debug=True)