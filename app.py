from flask import Flask, jsonify, render_template
from flask_cors import CORS
from analisador import AnalisadorCorporativo

# Configuração do Flask
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

analisador = AnalisadorCorporativo('empresas.csv', 'relacoes.csv')
grupos_economicos_analisados = analisador.analisar_grupos_economicos()

# Mapeamento dos resultados detalhados por grupo
resultados_detalhados = {}
for grupo_info in grupos_economicos_analisados:
    grupo_id_str = str(grupo_info['id_grupo'])
    membros_ids = [k for k, v in analisador.node_names.items() if v in grupo_info['membros']]
    
    dados_grafo = analisador.obter_dados_do_grafo_para_grupo(membros_ids)
    
    resultados_detalhados[grupo_id_str] = {
        "info_grupo": grupo_info,
        "visualizacao_grafo": dados_grafo
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/groups', methods=['GET'])
def get_groups():
    lista_grupos = [{
        "id": g["id_grupo"],
        "nome": f"Grupo {g['id_grupo']}", 
        "membros_count": len(g['membros'])
    } for g in grupos_economicos_analisados]
    return jsonify(lista_grupos)

@app.route('/api/group/<group_id>', methods=['GET'])
def get_group_details(group_id):
    if group_id in resultados_detalhados:
        return jsonify(resultados_detalhados[group_id])
    return jsonify({"error": "Grupo não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)