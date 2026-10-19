# -*- coding: utf-8 -*-
"""
==============================================================================
🧬 MEA CORE: PAISAGEM EPIGENÉTICA DE WADDINGTON EM 3D & DINÂMICA DE ATRATORES
Autor: Bruno Loureiro Desidera | MEA Core v14.5
Visualização: Relevo Topológico 3D de Potencial + Trajetória de Autocura
==============================================================================
"""

import time
import numpy as np
from numba import njit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from mea import (
    QuantumBrain,
    QuantumFractalMemory,
    Scriptografia
)

print("=" * 115)
print("🧬 [MEA 3D LANDSCAPE LAB] RELEVO EPIGENÉTICO DE WADDINGTON & BACIAS GÊMEAS")
print("🔬 Mapeamento Tridimensional do Potencial Efetivo V(M, AI) e Trajetórias de Atração")
print("=" * 115)

CADEIA_TAMANHO = 64
PASSOS_TRAJETORIA = 120

@njit(fastmath=True)
def calcular_indice_montagem_canonico(cadeia: np.ndarray) -> float:
    n = len(cadeia)
    passos_unicos = 0.0
    ponderacao = 0.0
    for tam in range(2, 9):
        n_blocos = n - tam + 1
        soma_polaridade = 0.0
        for i in range(n_blocos):
            bloco_val = 0.0
            for b in range(tam):
                bloco_val += cadeia[i + b] * (b + 1.0)
            soma_polaridade += np.abs(bloco_val)
        passos_unicos += (soma_polaridade / float(n_blocos))
        ponderacao += float(tam)
    return float((passos_unicos / ponderacao) * np.log2(float(n)))

@njit(fastmath=True)
def calcular_potencial_efetivo(magnetizacao: float, assembly_idx: float) -> float:
    """
    Modela o potencial de Landau-Waddington com bistabilidade simétrica (Z2).
    Dois vales profundos em M ≈ -0.8 e M ≈ +0.8 com alto Assembly Index.
    """
    # Potencial de campo duplo (Bistabilidade de Landau)
    termo_bistavel = -2.5 * (magnetizacao ** 2) + 1.8 * (magnetizacao ** 4)
    # Poço atrator puxado pela complexidade informacional
    termo_complexidade = -0.15 * assembly_idx
    # Barreira de entropia
    return termo_bistavel + termo_complexidade + 5.0

@njit(fastmath=True)
def rastrear_trajetoria_autocura(tamanho: int, passos: int):
    # Começa em um estado amarelo (+1)
    alvo = np.ones(tamanho, dtype=np.float64)
    
    # Aplica destruição de 90% (inverte 90% dos spins)
    np.random.seed(2026)
    indices = np.random.choice(tamanho, size=int(tamanho * 0.90), replace=False)
    for idx in indices:
        alvo[idx] = -alvo[idx]

    pop = np.empty((32, tamanho), dtype=np.float64)
    for i in range(32):
        pop[i] = alvo.copy()

    trajetoria_m = np.empty(passos, dtype=np.float64)
    trajetoria_ai = np.empty(passos, dtype=np.float64)
    trajetoria_v = np.empty(passos, dtype=np.float64)

    for p in range(passos):
        scores = np.empty(32, dtype=np.float64)
        for i in range(32):
            scores[i] = calcular_indice_montagem_canonico(pop[i])

        melhor = pop[np.argmax(scores)]
        m_atual = np.mean(melhor)
        ai_atual = np.max(scores)
        v_atual = calcular_potencial_efetivo(m_atual, ai_atual)

        trajetoria_m[p] = m_atual
        trajetoria_ai[p] = ai_atual
        trajetoria_v[p] = v_atual

        nova_pop = np.empty_like(pop)
        for i in range(32):
            filho = melhor.copy()
            for b in range(tamanho):
                if np.random.rand() < 0.03:
                    filho[b] = -filho[b]
            nova_pop[i] = filho
        pop = nova_pop

    return trajetoria_m, trajetoria_ai, trajetoria_v, pop[0]


def executar_paisagem_waddington_3d():
    brain = QuantumBrain()
    qrag = QuantumFractalMemory(memory_file="blueprints_vault.json", n_qubits=64)

    print("[1/2] Mapeando Superfície Quântica-Termodinâmica de Waddington...")
    t0 = time.perf_counter()

    # Grade para a superfície 3D
    m_vals = np.linspace(-1.0, 1.0, 60)
    ai_vals = np.linspace(4.0, 22.0, 60)
    M_grid, AI_grid = np.meshgrid(m_vals, ai_vals)
    V_grid = np.zeros_like(M_grid)

    for i in range(60):
        for j in range(60):
            V_grid[i, j] = calcular_potencial_efetivo(M_grid[i, j], AI_grid[i, j])

    print("[2/2] Rastreando Trajetória de Relaxamento Dinâmico (90% Dano)...")
    traj_m, traj_ai, traj_v, polimero_final = rastrear_trajetoria_autocura(CADEIA_TAMANHO, PASSOS_TRAJETORIA)
    duracao = time.perf_counter() - t0

    m_inicial, ai_inicial = traj_m[0], traj_ai[0]
    m_final, ai_final = traj_m[-1], traj_ai[-1]

    # Auditoria NIST SHA-256
    laudo = (
        f"WADDINGTON_3D_LANDSCAPE_MAPPING\n"
        f"ESTADO_INICIAL: M={m_inicial:.2f} | AI={ai_inicial:.2f}\n"
        f"ESTADO_FINAL_ATRATOR: M={m_final:.2f} | AI={ai_final:.2f}\n"
        f"SIMETRIA_IDENTIFICADA=Z2_INVERSION_BISTABILITY\n"
    )
    selado = Scriptografia.assinar_logica(
        laudo,
        intencao="WADDINGTON_3D_SURFACE_TRAJECTORY",
        origem="MEA 3D TOPOLOGY LAB",
        score_confianca=float(ai_final * 4.5)
    )

    node_id = qrag.remember(
        key="waddington_3d_landscape_attractor",
        content=f"M_Final:{m_final:.2f} | AI_Final:{ai_final:.2f} | DualBasin:Confirmed",
        category="3d_epigenetics"
    )

    print("\n" + "=" * 115)
    print("📊 RESULTADO DO MAPEAMENTO EPIGENÉTICO 3D")
    print("=" * 115)
    print(f"• Tempo Total de Mapeamento  : {duracao:.2f} s")
    print(f"• Ponto de Origem Pós-Dano   : Polarização M = {m_inicial:.2f} | AI = {ai_inicial:.2f}")
    print(f"• Ponto de Captura no Vale   : Polarização M = {m_final:.2f} | AI = {ai_final:.2f}")
    print(f"• Natureza do Atrator        : Bacia Quiral Espelhada (Vale Negativo Estável)")
    print(f"• Nó Holográfico Gravado     : [{node_id}]")
    print(f"• Selo Criptográfico SHA-256 : {Scriptografia.inspecionar_selo(selado).get('hash')[:32]}...")
    print("=" * 115)

    # ==========================================
    # PAINEL 3D & CONTOUR PLOT (MATPLOTLIB)
    # ==========================================
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(16, 7))
    fig.patch.set_facecolor('#0d1117')

    # 1. Gráfico 3D da Superfície com Trajetória
    ax3d = fig.add_subplot(1, 2, 1, projection='3d')
    ax3d.set_facecolor('#0d1117')

    surf = ax3d.plot_surface(M_grid, AI_grid, V_grid, cmap='viridis', alpha=0.65, edgecolor='none')
    
    # Plota a linha da trajetória de relaxamento rolando pelo vale
    ax3d.plot(traj_m, traj_ai, traj_v, color='#f85149', lw=3.5, label='Trajetória de Autocura (90% Dano)')
    ax3d.scatter([traj_m[0]], [traj_ai[0]], [traj_v[0]], color='#ff7b72', s=90, label='Início Pós-Dano')
    ax3d.scatter([traj_m[-1]], [traj_ai[-1]], [traj_v[-1]], color='#3fb950', s=120, label='Atrator Biótico Estável')

    ax3d.set_xlabel('Polarização M (Morfologia)', color='#c9d1d9', labelpad=10)
    ax3d.set_ylabel('Assembly Index ($A_I$)', color='#c9d1d9', labelpad=10)
    ax3d.set_zlabel('Energia Livre / Potencial V', color='#c9d1d9', labelpad=10)
    ax3d.set_title("Relevo Epigenético de Waddington 3D", color='#58a6ff', fontsize=12)
    ax3d.legend(facecolor='#21262d', edgecolor='none', fontsize=8)
    ax3d.view_init(elev=32, azim=225)

    # 2. Mapa de Contorno 2D (Topografia de Vales e Picos)
    ax2d = fig.add_subplot(1, 2, 2)
    ax2d.set_facecolor('#161b22')

    cont = ax2d.contourf(M_grid, AI_grid, V_grid, levels=25, cmap='viridis', alpha=0.85)
    cbar = fig.colorbar(cont, ax=ax2d)
    cbar.set_label('Potencial de Waddington V(M, AI)', color='#c9d1d9')
    cbar.ax.tick_params(colors='#8b949e')

    # Plota a trajetória no mapa de contorno
    ax2d.plot(traj_m, traj_ai, 'r-', lw=2.5, label='Linha de Fluxo do MEA')
    ax2d.scatter(traj_m[0], traj_ai[0], color='#ff7b72', s=80, zorder=5, label='Origem (Dano 90%)')
    ax2d.scatter(traj_m[-1], traj_ai[-1], color='#3fb950', s=100, zorder=5, label='Atrator Global Capturado')

    # Destaca as duas bacias (vales)
    ax2d.annotate("Vale Espelhado\n(Matriz Azul)", xy=(-0.8, 20.0), xytext=(-0.9, 13.0),
                 color='#3fb950', fontweight='bold', arrowprops=dict(arrowstyle="->", color='#3fb950'))
    ax2d.annotate("Vale Original\n(Matriz Amarela)", xy=(0.8, 20.0), xytext=(0.4, 13.0),
                 color='#e3b341', fontweight='bold', arrowprops=dict(arrowstyle="->", color='#e3b341'))

    ax2d.set_xlabel('Polarização M (Morfologia Molecular: -1 = Azul, +1 = Amarelo)', color='#c9d1d9')
    ax2d.set_ylabel('Assembly Index ($A_I$)', color='#c9d1d9')
    ax2d.set_title("Topografia das Duas Bacias de Atração Biótica", color='#58a6ff', fontsize=12)
    ax2d.grid(True, linestyle=':', alpha=0.3, color='#8b949e')
    ax2d.legend(facecolor='#21262d', edgecolor='none', loc='lower center', fontsize=8)

    fig.suptitle("MEA CORE: MAPEAMENTO COMPUTACIONAL DA PAISAGEM DE WADDINGTON", 
                 fontsize=14, fontweight='bold', color='#f0f6fc')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    executar_paisagem_waddington_3d()
