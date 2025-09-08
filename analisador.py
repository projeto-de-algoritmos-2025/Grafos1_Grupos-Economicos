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
                    vizinhos = self.adj_parcerias.get(u, []) + self.adj_controle.get(u, [])
                    for v_adj_list in self.adj_controle.values():
                        if u in v_adj_list and u not in vizinhos:
                            origem = [key for key, val in self.adj_controle.items() if u in val]
                            vizinhos.extend(origem)
        
                    for v in vizinhos:
                        if v not in visited:
                            visited.add(v)
                            stack.append(v)
                
                if componente_atual:
                    componente_set = set(componente_atual)
                    merged = False
                    for i, comp in enumerate(componentes):
                        if not componente_set.isdisjoint(comp):
                            componentes[i] = list(set(comp) | componente_set)
                            merged = True
                            break
                    if not merged:
                        componentes.append(componente_atual)

        resultado_grupos = []
        for i, grupo in enumerate(componentes):
            if not grupo: continue
            resultado_grupos.append({
                "id_grupo": i,
                "membros": [self.node_names[m] for m in grupo if m in self.node_names],
                "membros_ids": grupo
            })
        return resultado_grupos
    
    def detectar_ciclo_e_ordenacao_topologica(self, grupo_ids):
        adj = {u: [] for u in grupo_ids}
        in_degree = {u: 0 for u in grupo_ids}

        for u in grupo_ids:
            for v in self.adj_controle.get(u, []):
                if v in grupo_ids:
                    adj[u].append(v)
                    in_degree[v] += 1
        
        queue = deque([u for u in grupo_ids if in_degree[u] == 0])
        topological_order = []
        
        while queue:
            u = queue.popleft()
            topological_order.append(u)
            
            for v in adj.get(u, []):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        if len(topological_order) == len(grupo_ids):
            return {"tem_ciclo": False, "ordem_topologica": [self.node_names[n] for n in topological_order]}
        else:
            return {"tem_ciclo": True, "ordem_topologica": []}

    def encontrar_empresa_principal(self, grupo_ids):
        graus = {node: 0 for node in grupo_ids}
        for u in grupo_ids:
            for v in self.adj_parcerias.get(u, []):
                if v in grupo_ids:
                    graus[u] += 1

        if not any(graus.values()):
            return {"principais": [], "mensagem": "Este grupo não possui relações de parceria."}

        max_grau = max(graus.values())
        
        if max_grau == 0:
            return {"principais": [], "mensagem": "Nenhuma empresa se destaca por número de conexões."}

        principais = [node for node, grau in graus.items() if grau == max_grau]
        
        if len(principais) <= 3:
            return {"principais": [self.node_names[p] for p in principais], "mensagem": ""}
        else:
            return {"principais": [], "mensagem": "Não há uma empresa principal clara neste grupo (empate entre mais de 3 empresas)."}

    def obter_dados_do_grafo_para_grupo(self, grupo_ids):

        nodes_set = set(grupo_ids)
        edges = []
        
        # Adiciona arestas de parceria
        is_directed = False
        for u in grupo_ids:
            for v in self.adj_controle.get(u, []):
                if v in nodes_set:
                    edges.append({"from": u, "to": v, "type": "controle"})
                    is_directed = True

        # Adiciona arestas de controle
        for u in grupo_ids:
            for v in self.adj_parcerias.get(u, []):
                if v in nodes_set and u < v:
                    edges.append({"from": u, "to": v, "type": "parceria"})
                    
        nodes_formatados = [{"id": node_id, "label": self.node_names[node_id]} for node_id in grupo_ids]
        
        analise_adicional = {}
        if is_directed:
            analise_adicional = self.detectar_ciclo_e_ordenacao_topologica(grupo_ids)
        else:
            analise_adicional = self.encontrar_empresa_principal(grupo_ids)

        return {"nodes": nodes_formatados, "edges": edges, "analise": analise_adicional}