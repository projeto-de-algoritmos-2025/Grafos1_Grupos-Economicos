document.addEventListener('DOMContentLoaded', () => {
    const groupListDiv = document.getElementById('group-list');
    const detailsContentDiv = document.getElementById('details-content');
    const graphContainer = document.getElementById('graph-visualization');
    let network = null;

    async function loadGroupList() {
        try {
            const response = await fetch('http://127.0.0.1:5001/api/groups');
            const groups = await response.json();
            groupListDiv.innerHTML = '';
            groups.forEach(group => {
                const button = document.createElement('button');
                button.className = 'group-button';
                button.textContent = `${group.nome} (${group.membros_count} membros)`;
                button.dataset.groupId = group.id;
                button.onclick = () => {
                    loadGroupDetails(group.id);
                    document.querySelectorAll('.group-button').forEach(btn => btn.classList.remove('active'));
                    button.classList.add('active');
                };
                groupListDiv.appendChild(button);
            });
        } catch (error) {
            groupListDiv.innerHTML = `<p class="highlight">Erro ao carregar os grupos: ${error.message}</p>`;
        }
    }

    function drawGraph(data) {
        if (network !== null) {
            network.destroy();
            network = null;
        }

        const nodes = new vis.DataSet(data.visualizacao_grafo.nodes);
        const edges = new vis.DataSet(data.visualizacao_grafo.edges.map(e => ({
            from: e.from,
            to: e.to,
            arrows: e.type === 'controle' ? 'to' : undefined,
            dashes: e.type === 'parceria',
            label: e.type
        })));

        const graphData = { nodes: nodes, edges: edges };
        const options = {
            layout: {
                hierarchical: false
            },
            edges: {
                color: '#bdc3c7'
            },
            nodes: {
                shape: 'dot',
                size: 20,
                font: {
                    size: 14,
                    color: '#333'
                },
                borderWidth: 2,
                color: {
                    border: '#2980b9',
                    background: '#3498db',
                    highlight: {
                        border: '#2980b9',
                        background: '#d2e5ff'
                    }
                }
            },
            physics: {
                solver: 'forceAtlas2Based',
                forceAtlas2Based: {
                    gravitationalConstant: -50,
                    centralGravity: 0.01,
                    springLength: 100,
                    springConstant: 0.08,
                    avoidOverlap: 0.5
                }
            }
        };

        network = new vis.Network(graphContainer, graphData, options);
    }

    async function loadGroupDetails(groupId) {
        graphContainer.innerHTML = '';
        try {
            const response = await fetch(`http://127.0.0.1:5001/api/group/${groupId}`);
            if (!response.ok) throw new Error('Grupo não encontrado ou erro no servidor.');

            const data = await response.json();

            drawGraph(data);

        } catch (error) {
            detailsContentDiv.innerHTML = `<p class="highlight">Erro ao carregar detalhes: ${error.message}</p>`;
        }
    }

    loadGroupList();
});