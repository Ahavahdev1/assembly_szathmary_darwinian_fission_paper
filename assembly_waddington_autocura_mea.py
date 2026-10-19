# -*- coding: utf-8 -*-
"""
==============================================================================
🧬 MEA CORE: CANALIZAÇÃO DE WADDINGTON & CINÉTICA DE AUTOCURA MOLECULAR
Autor: Bruno Loureiro Desidera | MEA Core v14.5
Integração: Teste de Bacia de Atração + Resiliência Extrema + NIST SHA-256
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
print("🧬 [MEA WADDINGTON LAB] CINÉTICA DE AUTOCURA & ATRATORES TOPOLÓGICOS")
print("🔬 Avaliação da Resiliência Informacional sob Destruição Catastrófica (15% a 90%)")
print("=" * 115)

CADEIA_TAMANHO = 64
PASSOS_RECUPERACAO = 350
NIVEIS_DANO = np.array([0.15, 0.35, 0.55, 0.75, 0.90])

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
def encontrar_campeao_base(tamanho: int, passos: int):
    pop = np.random.choice(np.array([-1.0, 1.0]), size=(32, tamanho))
    for _ in range(passos):
        scores = np.empty(32, dtype=np.float64)
        for i in range(32):
            scores[i] = calcular_indice_montagem_canonico(pop[i])
        melhor = pop[np.argmax(scores)]
        nova_pop = np.empty_like(pop)
        for i in range(32):
            filho = melhor.copy()
            for b in range(tamanho):
                if np.random.rand() < 0.03:
                    filho[b] = -filho[b]
            nova_pop[i] = filho
        pop = nova_pop
    return pop[0]

@njit(fastmath=True)
def simular_autocura_dinamica(polimero_danificado: np.ndarray, n_passos: int, taxa_mut: float):
    tamanho = len(polimero_danificado)
    pop = np.empty((32, tamanho), dtype=np.float64)
    for i in range(32):
        pop[i] = polimero_danificado.copy()

    hist_rec = np.empty(n_passos, dtype=np.float64)

    for p in range(n_passos):
        scores = np.empty(32, dtype=np.float64)
        for i in range(32):
            scores[i] = calcular_indice_montagem_canonico(pop[i])
        hist_rec[p] = np.max(scores)
        melhor = pop[np.argmax(scores)]

        nova_pop = np.empty_like(pop)
        for i in range(32):
            filho = melhor.copy()
            for b in range(tamanho):
                if np.random.rand() < taxa_mut:
                    filho[b] = -filho[b]
            nova_pop[i] = filho
        pop = nova_pop

    return hist_rec, pop[0]


def executar_laboratorio_waddington():
    brain = QuantumBrain()
    qrag = QuantumFractalMemory(memory_file="blueprints_vault.json", n_qubits=64)
    np.random.seed(2026)

    print("[1/2] Sintetizando Polímero Biótico Original (Alvo)...")
    t0 = time.perf_counter()
    campeao_original = encontrar_campeao_base(CADEIA_TAMANHO, 500)
    score_original = calcular_indice_montagem_canonico(campeao_original)
    print(f"  -> Score Original de Referência: {score_original:.2f}")

    print("[2/2] Aplicando Ciclos de Destruição e Cinética de Regeneração...")
    trajetorias = []
    polimeros_recuperados = []
    polimeros_danificados = []
    recuperacoes_percentuais = []

    for pct in NIVEIS_DANO:
        # Aplica mutação destrutiva forçada em X% dos bits
        danificado = campeao_original.copy()
        n_flips = int(CADEIA_TAMANHO * pct)
        indices_destruidos = np.random.choice(CADEIA_TAMANHO, size=n_flips, replace=False)
        for idx in indices_destruidos:
            danificado[idx] = -danificado[idx]

        score_danificado = calcular_indice_montagem_canonico(danificado)
        polimeros_danificados.append(danificado)

        # Dispara autocura informacional MEA
        hist_rec, curado = simular_autocura_dinamica(danificado, PASSOS_RECUPERACAO, 0.03)
        trajetorias.append(hist_rec)
        polimeros_recuperados.append(curado)

        score_curado = hist_rec[-1]
        taxa_recuperada = (score_curado / score_original) * 100.0
        recuperacoes_percentuais.append(taxa_recuperada)
        print(f"  -> Dano Injetado: {pct*100:4.1f}% | AI Danificado: {score_danificado:5.2f} | AI Regenerado: {score_curado:5.2f} ({taxa_recuperada:.1f}%)")

    duracao = time.perf_counter() - t0

    # Auditoria Criptográfica NIST SHA-256
    taxa_media_cura = np.mean(recuperacoes_percentuais)
    laudo = (
        f"WADDINGTON_CANALIZATION_BENCHMARK\n"
        f"SCORE_ALVO={score_original:.4f}\n"
        f"TAXA_MEDIA_REGENERACAO={taxa_media_cura:.2f}%\n"
        f"DANO_MAXIMO_TESTADO={NIVEIS_DANO[-1]*100:.1f}%\n"
        f"STATUS_ATRADOR={'CANALIZACAO_ROBUSTA_CONFIRMADA' if taxa_media_cura >= 95.0 else 'RESILIENCIA_PARCIAL'}\n"
    )
    selado = Scriptografia.assinar_logica(
        laudo,
        intencao="WADDINGTON_STRUCTURAL_HOMEOSTASIS",
        origem="MEA REGENERATION LAB",
        score_confianca=float(taxa_media_cura)
    )

    node_id = qrag.remember(
        key="waddington_canalization_recovery",
        content=f"ScoreAlvo:{score_original:.2f} | MediaCura:{taxa_media_cura:.1f}%",
        category="homeostasis_life"
    )

    print("\n" + "=" * 115)
    print("📊 RESULTADO DA CINÉTICA DE AUTOCURA & CANALIZAÇÃO")
    print("=" * 115)
    print(f"• Tempo Total de Simulação       : {duracao:.2f} s")
    print(f"• Score Biótico de Referência    : {score_original:.2f}")
    print(f"• Capacidade Média de Regeneração: {taxa_media_cura:.2f}% de integridade recuperada")
    print(f"• Nó Holográfico Gravado         : [{node_id}]")
    print(f"• Assinatura SHA-256 (NIST)      : {Scriptografia.inspecionar_selo(selado).get('hash')[:32]}...")
    print("=" * 115)

    # ==========================================
    # PAINEL MULTI-GRÁFICO DE AUTOCURA (MATPLOTLIB)
    # ==========================================
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(15, 8))
    fig.patch.set_facecolor('#0d1117')
    gs = fig.add_gridspec(2, 3)

    ax_curva = fig.add_subplot(gs[0, :2])
    ax_barras = fig.add_subplot(gs[0, 2])
    ax_orig = fig.add_subplot(gs[1, 0])
    ax_dano = fig.add_subplot(gs[1, 1])
    ax_cura = fig.add_subplot(gs[1, 2])

    for ax in [ax_curva, ax_barras, ax_orig, ax_dano, ax_cura]:
        ax.set_facecolor('#161b22')

    # 1. Trajetórias de Regeneração Temporal
    cores = ['#3fb950', '#58a6ff', '#e3b341', '#f0883e', '#f85149']
    for i, traj in enumerate(trajetorias):
        ax_curva.plot(traj, color=cores[i], lw=2, label=f"Dano {NIVEIS_DANO[i]*100:.0f}% (Início: {traj[0]:.1f})")
    ax_curva.axhline(score_original, color='white', linestyle='--', lw=1.5, label=f"Alvo Biótico ({score_original:.1f})")
    ax_curva.set_title("Cinética de Regeneração Temporal (Bacia de Atração)", color='#58a6ff')
    ax_curva.set_xlabel("Passos de Autocura Informacional", color='#c9d1d9')
    ax_curva.set_ylabel("Índice de Montagem Canônico", color='#c9d1d9')
    ax_curva.legend(facecolor='#21262d', edgecolor='none', fontsize=8)
    ax_curva.grid(True, linestyle=':', alpha=0.3, color='#8b949e')

    # 2. Resiliência por Nível de Dano
    labels = [f"{d*100:.0f}%" for d in NIVEIS_DANO]
    ax_barras.bar(labels, recuperacoes_percentuais, color=cores, width=0.55)
    ax_barras.axhline(100, color='white', linestyle=':', alpha=0.5)
    ax_barras.set_title("Eficiência de Recuperação (%)", color='#3fb950')
    ax_barras.set_xlabel("Dano Injetado", color='#c9d1d9')
    ax_barras.set_ylim([0, 110])
    ax_barras.grid(True, linestyle=':', alpha=0.3, color='#8b949e', axis='y')

    # 3. Comparativo Topológico: Original vs 90% Destruído vs Regenerado
    ax_orig.imshow(campeao_original.reshape((8, 8)), cmap='plasma', interpolation='nearest')
    ax_orig.set_title(f"1. Molécula Original\n(AI = {score_original:.1f})", color='#3fb950', fontsize=10)
    ax_orig.axis('off')

    ax_dano.imshow(polimeros_danificados[-1].reshape((8, 8)), cmap='plasma', interpolation='nearest')
    ax_dano.set_title("2. Dano Crítico de 90%\n(Quase Todo Destruído)", color='#f85149', fontsize=10)
    ax_dano.axis('off')

    ax_cura.imshow(polimeros_recuperados[-1].reshape((8, 8)), cmap='plasma', interpolation='nearest')
    ax_cura.set_title(f"3. Estrutura Autocurada\n(AI = {trajetorias[-1][-1]:.1f})", color='#58a6ff', fontsize=10)
    ax_cura.axis('off')

    fig.suptitle("MEA CORE: CANALIZAÇÃO BIOLÓGICA & HOMEOSTASE INFORMACIONAL", fontsize=13, fontweight='bold', color='#f0f6fc')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    executar_laboratorio_waddington()
