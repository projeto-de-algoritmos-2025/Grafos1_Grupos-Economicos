import pandas as pd
from collections import deque

# Análise de grafos para identificar grupos econômicos
class AnalisadorCorporativo:
    def __init__(self, empresas_path, relacoes_path):
        empresas_df = pd.read_csv(empresas_path)
        relacoes_df = pd.read_csv(relacoes_path)
        
        self.nodes = list(empresas_df['id_empresa'])
        self.node_names = dict(zip(empresas_df['id_empresa'], empresas_df['nome']))

        # Lista de adjacência para parcerias e controle
        self.adj_parcerias = {node: [] for node in self.nodes}
        self.adj_controle = {node: [] for node in self.nodes}
        
        for _, rel in relacoes_df.iterrows():
            u, v, rel_type = rel['origem'], rel['destino'], rel['tipo_relacao']
            if u in self.nodes and v in self.nodes:
                if rel_type == 'controle':
                    self.adj_controle[u].append(v)
                elif rel_type == 'parceria':
                    self.adj_parcerias[u].append(v)
                    self.adj_parcerias[v].append(u)

    # Encontrar componentes conectados
    def analisar_grupos_economicos(self):
        visited = set()
        componentes = []
        for node in self.nodes:
            if node not in visited:
                componente_atual = []
                stack = [node]
                visited.add(node)
                while stack:
                    u = stack.pop()
                    componente_atual.append(u)
                    for v in self.adj_parcerias[u]:
                        if v not in visited:
                            visited.add(v)
                            stack.append(v)
                componentes.append(componente_atual)
        
        resultado_grupos = []
        for i, grupo in enumerate(componentes):
            if not grupo: continue
            resultado_grupos.append({
                "id_grupo": i,
                "membros": [self.node_names[m] for m in grupo],
            })
        return resultado_grupos
    
    # Obter dados do grafo para visualização
    def obter_dados_do_grafo_para_grupo(self, grupo_ids):

        nodes_set = set(grupo_ids)
        edges = []
        
        # Adiciona arestas de parceria
        for u in grupo_ids:
            for v in self.adj_parcerias.get(u, []):
                if v in nodes_set and u < v:
                    edges.append({"from": u, "to": v, "type": "parceria"})
                    
        # Adiciona arestas de controle
        for u in grupo_ids:
            for v in self.adj_controle.get(u, []):
                if v in nodes_set:
                    edges.append({"from": u, "to": v, "type": "controle"})
                    
        nodes_formatados = [{"id": node_id, "label": self.node_names[node_id]} for node_id in grupo_ids]
        
        return {"nodes": nodes_formatados, "edges": edges}
