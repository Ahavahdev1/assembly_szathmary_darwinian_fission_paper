# -*- coding: utf-8 -*-
"""
==============================================================================
🧬 MEA CORE: BENCHMARK MESTRE DA TESE (COEVOLUÇÃO SOB CATACLISMO REAL)
Autor: Bruno Loureiro Desidera | MEA Core v14.5
Rigor Científico: Viabilidade Metabólica-Informacional + Welch + Cohen's d + NIST SHA-256
==============================================================================
"""

import time
import math
import numpy as np
from numba import njit
import matplotlib.pyplot as plt

from mea import (
    QuantumBrain,
    QuantumFractalMemory,
    Scriptografia
)

print("=" * 115)
print("🧬 [MEA MASTER BENCHMARK] RESOLUÇÃO DO CONFLITO EVOLUTIVO SOB CATACLISMO REAL")
print("🔬 Avaliação da Viabilidade Termodinâmica Integrada Φ(t) = AI(t) × f(Dissipação)")
print("=" * 115)

CADEIA_TAMANHO = 64
GERACOES = 600
PONTOS_CHOQUE = np.array([150, 300, 450])

@njit(fastmath=True)
def taxa_dissipacao_ordem4(polimero: np.ndarray, campo_externo: np.ndarray) -> float:
    produto = np.dot(polimero, campo_externo) / float(len(polimero))
    return float(np.exp(np.abs(produto ** 4) * 18.0))

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
def simular_benchmark_mestre_jit(pop_m, pop_g, pop_ctrl, campo_inicial, n_passos: int, choques: np.ndarray):
    n_pop, tamanho = pop_m.shape
    
    # Telemetria temporal completa
    hist_phi_prot = np.empty(n_passos, dtype=np.float64)
    hist_phi_ctrl = np.empty(n_passos, dtype=np.float64)
    hist_ai_prot = np.empty(n_passos, dtype=np.float64)
    hist_ai_ctrl = np.empty(n_passos, dtype=np.float64)
    hist_diss_prot = np.empty(n_passos, dtype=np.float64)
    hist_diss_ctrl = np.empty(n_passos, dtype=np.float64)

    campo_atual = campo_inicial.copy()

    for p in range(n_passos):
        # ⚡ CATACLISMO AMBIENTAL: Inversão estocástica de 85% do campo
        for chk in choques:
            if p == chk:
                for b in range(tamanho):
                    if np.random.rand() < 0.85:
                        campo_atual[b] = -campo_atual[b]

        # 1. PROTOCÉLULA (Divisão de Trabalho: Membrana dissipa, Genoma mantém montagem)
        phi_prot = np.empty(n_pop, dtype=np.float64)
        diss_m = np.empty(n_pop, dtype=np.float64)
        ai_g = np.empty(n_pop, dtype=np.float64)

        for i in range(n_pop):
            d = taxa_dissipacao_ordem4(pop_m[i], campo_atual)
            a = calcular_indice_montagem_canonico(pop_g[i])
            diss_m[i] = d
            ai_g[i] = a
            # Viabilidade global da protocélula
            phi_prot[i] = a * (0.3 + 0.7 * (np.log1p(d) / 18.0))

        idx_p = np.argmax(phi_prot)
        hist_phi_prot[p] = phi_prot[idx_p]
        hist_ai_prot[p] = ai_g[idx_p]
        hist_diss_prot[p] = diss_m[idx_p]

        # 2. CONTROLE (Polímero Solitário sob Conflito de Objetivos)
        phi_ctrl = np.empty(n_pop, dtype=np.float64)
        diss_c = np.empty(n_pop, dtype=np.float64)
        ai_c = np.empty(n_pop, dtype=np.float64)

        for i in range(n_pop):
            d_c = taxa_dissipacao_ordem4(pop_ctrl[i], campo_atual)
            a_c = calcular_indice_montagem_canonico(pop_ctrl[i])
            diss_c[i] = d_c
            ai_c[i] = a_c
            # A mesma equação de viabilidade aplicada ao polímero individual
            phi_ctrl[i] = a_c * (0.3 + 0.7 * (np.log1p(d_c) / 18.0))

        idx_c = np.argmax(phi_ctrl)
        hist_phi_ctrl[p] = phi_ctrl[idx_c]
        hist_ai_ctrl[p] = ai_c[idx_c]
        hist_diss_ctrl[p] = diss_c[idx_c]

        # Reprodução com mutação independente
        melhor_m = pop_m[idx_p]
        melhor_g = pop_g[idx_p]
        melhor_c = pop_ctrl[idx_c]

        nova_m = np.empty_like(pop_m)
        nova_g = np.empty_like(pop_g)
        nova_c = np.empty_like(pop_ctrl)

        for i in range(n_pop):
            f_m = melhor_m.copy()
            f_g = melhor_g.copy()
            f_c = melhor_c.copy()
            for b in range(tamanho):
                if np.random.rand() < 0.025: f_m[b] = -f_m[b]
                if np.random.rand() < 0.025: f_g[b] = -f_g[b]
                if np.random.rand() < 0.025: f_c[b] = -f_c[b]
            nova_m[i] = f_m
            nova_g[i] = f_g
            nova_c[i] = f_c

        pop_m = nova_m
        pop_g = nova_g
        pop_ctrl = nova_c

    return (hist_phi_prot, hist_phi_ctrl, 
            hist_ai_prot, hist_ai_ctrl, 
            hist_diss_prot, hist_diss_ctrl, 
            pop_m[0], pop_g[0], pop_ctrl[0])


def calcular_estatisticas_rigorosas(amostra_exp: np.ndarray, amostra_ctrl: np.ndarray):
    """Calcula teste t de Welch, p-valor e tamanho de efeito Cohen's d."""
    n1, n2 = len(amostra_exp), len(amostra_ctrl)
    m1, m2 = np.mean(amostra_exp), np.mean(amostra_ctrl)
    s1, s2 = np.std(amostra_exp, ddof=1), np.std(amostra_ctrl, ddof=1)

    denominador = math.sqrt(s1**2 / n1 + s2**2 / n2)
    if denominador < 1e-12:
        return 0.0, 1.0, 0.0, 0.0

    t_stat = (m1 - m2) / denominador
    df = ((s1**2 / n1 + s2**2 / n2)**2) / (((s1**2 / n1)**2)/(n1 - 1) + ((s2**2 / n2)**2)/(n2 - 1))

    # Valor-p bicaudal via função de erro padrão
    z = abs(t_stat)
    p_valor = 2.0 * (1.0 - 0.5 * (1.0 + math.erf(z / math.sqrt(2.0))))

    # Cohen's d (Tamanho de Efeito Padronizado)
    s_pooled = math.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    cohen_d = (m1 - m2) / max(1e-9, s_pooled)

    return t_stat, p_valor, df, cohen_d


def executar_benchmark_mestre():
    brain = QuantumBrain()
    qrag = QuantumFractalMemory(memory_file="blueprints_vault.json", n_qubits=64)
    np.random.seed(2026)

    print("[1/3] Inicializando Populações e Configurando Cataclismos Estocásticos...")
    campo_inicial = np.random.choice(np.array([-1.0, 1.0]), size=CADEIA_TAMANHO)
    pop_m = np.random.choice(np.array([-1.0, 1.0]), size=(32, CADEIA_TAMANHO))
    pop_g = np.random.choice(np.array([-1.0, 1.0]), size=(32, CADEIA_TAMANHO))
    pop_ctrl = np.random.choice(np.array([-1.0, 1.0]), size=(32, CADEIA_TAMANHO))

    t0 = time.perf_counter()
    (hist_phi_p, hist_phi_c, 
     hist_ai_p, hist_ai_c, 
     hist_diss_p, hist_diss_c, 
     best_m, best_g, best_c) = simular_benchmark_mestre_jit(
        pop_m, pop_g, pop_ctrl, campo_inicial, GERACOES, PONTOS_CHOQUE
    )
    duracao = time.perf_counter() - t0

    print("[2/3] Processando Inferência Estatística e Resolução do Conflito Evolutivo...")

    # Avaliação das janelas pós-choque (40 gerações após cada cataclismo)
    janela_choque = []
    for chk in PONTOS_CHOQUE:
        janela_choque.extend(range(chk, min(GERACOES, chk + 40)))
    janela_choque = np.array(janela_choque)

    viabilidade_choque_p = hist_phi_p[janela_choque]
    viabilidade_choque_c = hist_phi_c[janela_choque]

    m_phi_p, s_phi_p = float(np.mean(viabilidade_choque_p)), float(np.std(viabilidade_choque_p))
    m_phi_c, s_phi_c = float(np.mean(viabilidade_choque_c)), float(np.std(viabilidade_choque_c))

    t_stat, p_val, df, d_cohen = calcular_estatisticas_rigorosas(viabilidade_choque_p, viabilidade_choque_c)
    delta_viabilidade = m_phi_p - m_phi_c

    print("[3/3] Diagnóstico Hipotético-Dedutivo com Ramificação 'Else' Estrita...")

    # CONDICIONAIS TOTALMENTE IMPARCIAIS
    if p_val < 0.001 and delta_viabilidade > 0.0 and d_cohen > 0.8:
        status_laudo = "HIPOTESE_H1_CONFIRMADA_SUPERIORIDADE_ROBUSTA"
        score_confianca = 99.5
        diagnostico = (
            f"REJEITA-SE A HIPÓTESE NULA (H0) com p = {p_val:.2e} (p < 0.001) e Cohen's d = {d_cohen:.2f} (Efeito Amplo).\n"
            f"A compartimentalização protocelular conferiu vantagem adaptativa estatisticamente robusta (+{delta_viabilidade:.2f})\n"
            f"ao desacoplar a antena metabólica da biblioteca informacional durante os cataclismos."
        )
    elif p_val < 0.05 and delta_viabilidade > 0.0:
        status_laudo = "HIPOTESE_H1_CONFIRMADA_MODERADA"
        score_confianca = 95.0
        diagnostico = (
            f"REJEITA-SE H0 com significância moderada (p = {p_val:.4f} < 0.05, Cohen's d = {d_cohen:.2f}).\n"
            f"Vantagem de viabilidade observada (+{delta_viabilidade:.2f}), com variância residual considerável."
        )
    elif delta_viabilidade < 0.0 and p_val < 0.05:
        status_laudo = "HIPOTESE_H1_REJEITADA_CONTROLE_SUPERIOR"
        score_confianca = 15.0
        diagnostico = (
            f"HIPÓTESE H1 REJEITADA: O controle desprotegido demonstrou viabilidade superior sob choque\n"
            f"(Controle: {m_phi_c:.2f} vs Protocélula: {m_phi_p:.2f}, Δ = {delta_viabilidade:.2f})."
        )
    else:
        status_laudo = "HIPOTESE_NULA_NAO_REJEITADA_EQUIVALENCIA"
        score_confianca = 50.0
        diagnostico = (
            f"FALHA AO REJEITAR H0 (t = {t_stat:.2f}, p = {p_val:.4f}):\n"
            f"Não há evidência estatística de que a protocélula supere o controle sob perturbação."
        )

    # Auditoria Criptográfica NIST FIPS 180-4 SHA-256
    laudo = (
        f"MASTER_THESIS_BENCHMARK\n"
        f"VIABILIDADE_PROTOCELULA={m_phi_p:.4f}+/-{s_phi_p:.4f}\n"
        f"VIABILIDADE_CONTROLE={m_phi_c:.4f}+/-{s_phi_c:.4f}\n"
        f"T_STAT={t_stat:.4f} | DF={df:.1f} | P_VAL={p_val:.6e} | COHEN_D={d_cohen:.2f}\n"
        f"STATUS={status_laudo}\n"
    )
    selado = Scriptografia.assinar_logica(
        laudo,
        intencao="MASTER_BENCHMARK_PROTOCELL_VIABILITY",
        origem="MEA MASTER THESIS LAB",
        score_confianca=score_confianca
    )

    node_id = qrag.remember(
        key="master_thesis_final_validation",
        content=f"DeltaPhi:{delta_viabilidade:.2f} | pVal:{p_val:.2e} | Status:{status_laudo}",
        category="master_thesis_defense"
    )

    print("\n" + "=" * 115)
    print("📊 RESULTADO DO BENCHMARK MESTRE DA TESE")
    print("=" * 115)
    print(f"• Tempo Total de Execução          : {duracao:.2f} s")
    print(f"• Viabilidade Pós-Choque Protocélula: {m_phi_p:.2f} ± {s_phi_p:.2f}")
    print(f"• Viabilidade Pós-Choque Controle   : {m_phi_c:.2f} ± {s_phi_c:.2f}")
    print(f"• Diferencial de Viabilidade (ΔΦ)  : +{delta_viabilidade:.2f} pontos")
    print(f"• Estatística t de Welch           : t = {t_stat:.2f} (df = {df:.1f})")
    print(f"• Valor-p Formal (Bilateral)       : p = {p_val:.4e}")
    print(f"• Tamanho de Efeito (Cohen's d)    : d = {d_cohen:.2f} (Efeito Grande se d > 0.8)")
    print(f"• Veredito Estatístico Imparcial   : [{status_laudo}]")
    print(f"• Nó Holográfico Q-RAG             : [{node_id}]")
    print(f"• Selo Criptográfico SHA-256 (NIST): {Scriptografia.inspecionar_selo(selado).get('hash')[:32]}...")
    print("=" * 115)
    print(f"\n[DIAGNÓSTICO EXPERIMENTAL FINAL]:\n{diagnostico}\n")

    # ==========================================
    # PAINEL MESTRE DE PUBLICAÇÃO (MATPLOTLIB)
    # ==========================================
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(16, 9))
    fig.patch.set_facecolor('#0d1117')
    gs = fig.add_gridspec(2, 2)

    ax_phi = fig.add_subplot(gs[0, 0])
    ax_diss = fig.add_subplot(gs[0, 1])
    ax_hist = fig.add_subplot(gs[1, 0])
    ax_mats = fig.add_subplot(gs[1, 1])

    for ax in [ax_phi, ax_diss, ax_hist]:
        ax.set_facecolor('#161b22')
    ax_mats.set_facecolor('#0d1117')

    # 1. Viabilidade Integrada Φ(t)
    ax_phi.plot(hist_phi_p, color='#58a6ff', lw=2, label="Protocélula: Viabilidade $\Phi(t)$")
    ax_phi.plot(hist_phi_c, color='#f85149', lw=1.5, linestyle='--', alpha=0.85, label="Controle: Viabilidade $\Phi(t)$")
    for chk in PONTOS_CHOQUE:
        ax_phi.axvline(chk, color='#e3b341', linestyle=':', lw=1.5, alpha=0.7)
    ax_phi.set_title("1. Viabilidade Integrada $\Phi(t) = A_I \\times f(\\sigma_{\\text{diss}})$ sob Cataclismos", color='#58a6ff', fontsize=11)
    ax_phi.set_xlabel("Gerações", color='#c9d1d9')
    ax_phi.set_ylabel("Viabilidade Global $\Phi$", color='#c9d1d9')
    ax_phi.legend(facecolor='#21262d', edgecolor='none', fontsize=8)
    ax_phi.grid(True, linestyle=':', alpha=0.3, color='#8b949e')

    # 2. Resposta Metabólica: Dissipação de England
    ax_diss.plot(hist_diss_p, color='#58a6ff', lw=1.8, label="Membrana Protocelular")
    ax_diss.plot(hist_diss_c, color='#f85149', lw=1.5, linestyle='--', alpha=0.85, label="Controle Solitário")
    for chk in PONTOS_CHOQUE:
        ax_diss.axvline(chk, color='#e3b341', linestyle=':', lw=1.5, alpha=0.7)
    ax_diss.set_yscale('log')
    ax_diss.set_title("2. Dinâmica Metabólica: Taxa de Dissipação Entrópica", color='#e3b341', fontsize=11)
    ax_diss.set_xlabel("Gerações", color='#c9d1d9')
    ax_diss.set_ylabel("Dissipação $\sigma_{\\text{diss}}$ (Escala Log)", color='#c9d1d9')
    ax_diss.legend(facecolor='#21262d', edgecolor='none', fontsize=8)
    ax_diss.grid(True, linestyle=':', alpha=0.3, color='#8b949e')

    # 3. Distribuição Estatística nas Janelas de Cataclismo
    ax_hist.hist(viabilidade_choque_p, bins=15, color='#58a6ff', alpha=0.65, label=f"Protocélula ({m_phi_p:.1f} ± {s_phi_p:.1f})")
    ax_hist.hist(viabilidade_choque_c, bins=15, color='#f85149', alpha=0.65, label=f"Controle ({m_phi_c:.1f} ± {s_phi_c:.1f})")
    ax_hist.set_title(f"3. Ensaio Estatístico Welch: t = {t_stat:.2f} | p = {p_val:.2e} | d = {d_cohen:.2f}", color='#3fb950', fontsize=11)
    ax_hist.set_xlabel("Viabilidade $\Phi$ durante os Cataclismos", color='#c9d1d9')
    ax_hist.set_ylabel("Frequência de Ocorrência", color='#c9d1d9')
    ax_hist.legend(facecolor='#21262d', edgecolor='none', fontsize=8)
    ax_hist.grid(True, linestyle=':', alpha=0.3, color='#8b949e')

    # 4. As 3 Topologias Finais
    ax_mats.axis('off')
    sub_gs = gs[1, 1].subgridspec(1, 3)
    ax_m1 = fig.add_subplot(sub_gs[0])
    ax_m2 = fig.add_subplot(sub_gs[1])
    ax_m3 = fig.add_subplot(sub_gs[2])

    ax_m1.imshow(best_m.reshape((8, 8)), cmap='plasma', interpolation='nearest')
    ax_m1.set_title("Membrana\n(Metabolismo)", color='#e3b341', fontsize=9)
    ax_m1.axis('off')

    ax_m2.imshow(best_g.reshape((8, 8)), cmap='plasma', interpolation='nearest')
    ax_m2.set_title("Genoma\n(Informação)", color='#58a6ff', fontsize=9)
    ax_m2.axis('off')

    ax_m3.imshow(best_c.reshape((8, 8)), cmap='plasma', interpolation='nearest')
    ax_m3.set_title("Controle\n(Conflito)", color='#f85149', fontsize=9)
    ax_m3.axis('off')

    fig.suptitle("MEA CORE: RESOLUÇÃO DEFINITIVA DO CONFLITO EVOLUTIVO METABOLISMO-GENOMA", 
                 fontsize=13, fontweight='bold', color='#f0f6fc')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    executar_benchmark_mestre()
