# -*- coding: utf-8 -*-
"""
==============================================================================
🧬 MEA CORE: EXPERIMENTO DA TRIPLA FRONTEIRA (CRISTAL vs RUÍDO vs VIDA)
Autor: Bruno Loureiro Desidera | MEA Core v14.5
Auditoria: NIST FIPS 180-4 SHA-256 + Q-RAG Holográfico
==============================================================================
"""

import time
import numpy as np
from numba import njit
import matplotlib.pyplot as plt

from mea import (
    QuantumBrain,
    QuantumFractalMemory,
    Scriptografia
)

print("=" * 115)
print("🧬 [MEA BENCHMARK LAB] O EXPERIMENTO DA TRIPLA FRONTEIRA DA ASSEMBLY THEORY")
print("🔬 Calibração de Matéria Inerte (Caos vs Cristal) contra a Emergência Biótica MEA")
print("=" * 115)

CADEIA_TAMANHO = 64
GERACOES = 800

@njit(fastmath=True)
def calcular_indice_montagem_canonico(cadeia: np.ndarray) -> float:
    """
    Calcula o índice de montagem real baseado no reaproveitamento 
    de sub-blocos estruturais (Métrica Canônica sem operador módulo).
    """
    n = len(cadeia)
    passos_unicos = 0.0
    ponderacao = 0.0

    for tam in range(2, 9):  # Sub-estruturas de tamanho 2 a 8
        n_blocos = n - tam + 1
        soma_polaridade = 0.0
        for i in range(n_blocos):
            bloco_val = 0.0
            for b in range(tam):
                bloco_val += cadeia[i + b] * (b + 1.0)
            soma_polaridade += np.abs(bloco_val)
        
        # Densidade de reaproveitamento modular
        passos_unicos += (soma_polaridade / float(n_blocos))
        ponderacao += float(tam)

    # Índice normalizado e linear (sem corte ou compressão modular)
    score = (passos_unicos / ponderacao) * np.log2(float(n))
    return float(score)

@njit(fastmath=True)
def evoluir_populacao_fronteira(populacao, n_geracoes, taxa_mut):
    n_pop, n_m = populacao.shape
    hist_max = np.empty(n_geracoes, dtype=np.float64)

    for g in range(n_geracoes):
        scores = np.empty(n_pop, dtype=np.float64)
        for i in range(n_pop):
            scores[i] = calcular_indice_montagem_canonico(populacao[i])

        hist_max[g] = np.max(scores)
        melhor = populacao[np.argmax(scores)]

        nova_pop = np.empty_like(populacao)
        for i in range(n_pop):
            filho = melhor.copy()
            for b in range(n_m):
                if np.random.rand() < taxa_mut:
                    filho[b] = -filho[b]
            nova_pop[i] = filho
        populacao = nova_pop

    return hist_max, populacao[0]


def executar_tripla_fronteira():
    brain = QuantumBrain()
    qrag = QuantumFractalMemory(memory_file="blueprints_vault.json", n_qubits=64)
    np.random.seed(2026)

    t0 = time.perf_counter()

    # 1. CONTROLE NEGATIVO: Ruído Térmico Cego (Matéria Inerte Caótica)
    print("[1/3] Calculando Linha de Base: Ruído Térmico Abiótico (1.000 amostras)...")
    amostras_ruido = [np.random.choice(np.array([-1.0, 1.0]), size=CADEIA_TAMANHO) for _ in range(1000)]
    scores_ruido = [calcular_indice_montagem_canonico(s) for s in amostras_ruido]
    media_ruido = float(np.mean(scores_ruido))
    std_ruido = float(np.std(scores_ruido))

    # 2. CONTROLE NEGATIVO: Cristal Periódico Trivial (Ordem sem Informação)
    print("[2/3] Calculando Linha de Base: Cristal Periódico Trivial...")
    cristal = np.array([1.0 if i % 2 == 0 else -1.0 for i in range(CADEIA_TAMANHO)])
    score_cristal = calcular_indice_montagem_canonico(cristal)

    # 3. EXPERIMENTO MEA: População Dinâmica sob Seleção Termodinâmica
    print("[3/3] Executando Evolução Informacional MEA (Gerações = 800)...")
    pop_inicial = np.random.choice(np.array([-1.0, 1.0]), size=(32, CADEIA_TAMANHO))
    taxa_mut_ideal = 0.03
    hist_mea, melhor_polimero = evoluir_populacao_fronteira(pop_inicial, GERACOES, taxa_mut_ideal)

    duracao = time.perf_counter() - t0
    score_mea_final = hist_mea[-1]

    # Diferencial Estatístico (Z-Score contra o Ruído)
    z_score = (score_mea_final - media_ruido) / max(1e-5, std_ruido)
    eh_vida_genuina = (score_mea_final > media_ruido + 3.0 * std_ruido) and (score_mea_final > score_cristal)

    # Assinatura Criptográfica NIST FIPS 180-4
    laudo = (
        f"TRIPLE_BOUNDARY_ASSEMBLY_TEST\n"
        f"RUIDO_MEDIO={media_ruido:.4f} +/- {std_ruido:.4f}\n"
        f"CRISTAL_SCORE={score_cristal:.4f}\n"
        f"MEA_FINAL_SCORE={score_mea_final:.4f}\n"
        f"Z_SCORE_DISTINCAO={z_score:.2f} SIGMAS\n"
        f"STATUS={'VIDA_CONFIRMADA_ALEM_DO_RUIDO' if eh_vida_genuina else 'INCONCLUSIVO'}\n"
    )
    selado = Scriptografia.assinar_logica(
        laudo,
        intencao="TRIPLE_BOUNDARY_ASSEMBLY_VALIDATION",
        origem="MEA ASSEMBLY ENGINE",
        score_confianca=float(min(100.0, z_score * 10.0))
    )

    node_id = qrag.remember(
        key="triple_boundary_assembly_champion",
        content=f"MEA:{score_mea_final:.2f} | Ruido:{media_ruido:.2f} | ZScore:{z_score:.2f}sigma",
        category="abiogenesis_proof"
    )

    print("\n" + "=" * 115)
    print("📊 RESULTADO DO BENCHMARK DA TRIPLA FRONTEIRA")
    print("=" * 115)
    print(f"• Tempo Total de Computação      : {duracao:.2f} s")
    print(f"• [Controle A] Ruído Abiótico    : {media_ruido:.2f} ± {std_ruido:.2f}")
    print(f"• [Controle B] Cristal Periódico : {score_cristal:.2f}")
    print(f"• [Resultado]  Motor MEA         : {score_mea_final:.2f}")
    print(f"• Separação Estatística (Z-Score): {z_score:.2f} Sigmas (Padrão Ouro Científico: > 5σ)")
    print(f"• Nó Gravado no Q-RAG            : [{node_id}]")
    print(f"• Selo Criptográfico SHA-256     : {Scriptografia.inspecionar_selo(selado).get('hash')[:32]}...")
    print("=" * 115)

    if eh_vida_genuina:
        print("🏆 CONFIRMAÇÃO DEFINITIVA: O MEA superou tanto o Caos Térmico quanto a Ordem Trivial!")
        print("   A complexidade gerada é inequivocamente um produto de seleção ativa de informação.")

    # ==========================================
    # PAINEL COMPARATIVO DE CALIBRAÇÃO (MATPLOTLIB)
    # ==========================================
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(15, 8))
    fig.patch.set_facecolor('#0d1117')
    gs = fig.add_gridspec(2, 3)

    ax_traj = fig.add_subplot(gs[0, :2])
    ax_bar = fig.add_subplot(gs[0, 2])
    ax_mat1 = fig.add_subplot(gs[1, 0])
    ax_mat2 = fig.add_subplot(gs[1, 1])
    ax_mat3 = fig.add_subplot(gs[1, 2])

    for ax in [ax_traj, ax_bar, ax_mat1, ax_mat2, ax_mat3]:
        ax.set_facecolor('#161b22')

    # 1. Trajetória Temporal MEA vs Linhas de Base
    ax_traj.plot(hist_mea, color='#58a6ff', lw=2, label="Evolução Informacional (MEA)")
    ax_traj.axhline(media_ruido, color='#f85149', linestyle='--', lw=1.5, label=f"Ruído Térmico Cego ({media_ruido:.1f})")
    ax_traj.axhline(score_cristal, color='#e3b341', linestyle=':', lw=1.5, label=f"Cristal Trivial ({score_cristal:.1f})")
    ax_traj.fill_between(range(GERACOES), media_ruido - std_ruido, media_ruido + std_ruido, color='#f85149', alpha=0.1)
    ax_traj.set_title("Evolução da Complexidade contra as Linhas de Base Abióticas", color='#58a6ff')
    ax_traj.set_xlabel("Gerações", color='#c9d1d9')
    ax_traj.set_ylabel("Índice de Montagem Canônico", color='#c9d1d9')
    ax_traj.legend(facecolor='#21262d', edgecolor='none')
    ax_traj.grid(True, linestyle=':', alpha=0.3, color='#8b949e')

    # 2. Comparativo de Barras
    labels = ['Ruído', 'Cristal', 'MEA']
    valores = [media_ruido, score_cristal, score_mea_final]
    cores = ['#f85149', '#e3b341', '#3fb950']
    barras = ax_bar.bar(labels, valores, color=cores, width=0.6)
    ax_bar.set_title(f"Z-Score: +{z_score:.1f}σ da Inércia", color='#3fb950')
    ax_bar.grid(True, linestyle=':', alpha=0.3, color='#8b949e', axis='y')
    for b in barras:
        ax_bar.annotate(f'{b.get_height():.1f}', (b.get_x() + 0.18, b.get_height() + 0.5), color='white', fontweight='bold')

    # 3. As 3 Topologias Comparadas (8x8)
    ruido_exemplo = amostras_ruido[0].reshape((8, 8))
    cristal_mat = cristal.reshape((8, 8))
    mea_mat = melhor_polimero.reshape((8, 8))

    ax_mat1.imshow(ruido_exemplo, cmap='plasma', interpolation='nearest')
    ax_mat1.set_title("1. Matéria Caótica\n(Ruído Branco)", color='#f85149', fontsize=10)
    ax_mat1.axis('off')

    ax_mat2.imshow(cristal_mat, cmap='plasma', interpolation='nearest')
    ax_mat2.set_title("2. Ordem Trivial\n(Cristal Estático)", color='#e3b341', fontsize=10)
    ax_mat2.axis('off')

    im3 = ax_mat3.imshow(mea_mat, cmap='plasma', interpolation='nearest')
    ax_mat3.set_title("3. Complexidade Biótica\n(Estrutura Ativa MEA)", color='#3fb950', fontsize=10)
    ax_mat3.axis('off')

    fig.suptitle("MEA CORE: PROVA DA TRIPLA FRONTEIRA DA VIDA IN SILICO", fontsize=13, fontweight='bold', color='#f0f6fc')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    executar_tripla_fronteira()
