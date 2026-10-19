# MEA Core — Simulações Computacionais de Teoria da Montagem e Dinâmica Populacional

Repositório contendo scripts em Python para exploração e simulação computacional de modelos teóricos de biologia de sistemas, termodinâmica de não-equilíbrio e algoritmos genéticos baseados na **Teoria da Montagem (Assembly Theory)**.

---

## 📌 Visão Geral do Projeto

Este projeto implementa modelos numéricos acelerados via compilação Just-In-Time (JIT) para analisar o comportamento de cadeias de polímeros sob diferentes regras de seleção e perturbação:

- **Métrica de Montagem (Assembly Index):** Cálculo de complexidade estrutural e reutilização de sub-blocos.
- **Adaptação Dissipativa:** Simulação de ressonância sob campos oscilantes externos.
- **Dinâmica de Paisagem (Waddington):** Mapeamento de bacias de atração e recuperação após perturbações estruturais.
- **Modelagem de Compartimentalização:** Sistemas protocelulares acoplados (membrana metabólica + genoma interno).
- **Seleção Multinível e Fissão:** Simulação estocástica de divisão celular e dinâmica de populações.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **NumPy:** Vetorização e manipulação de arrays multidimensionais.
- **Numba (njit):** Aceleração de loops de simulação com velocidade de hardware.
- **Matplotlib:** Plotagem de telemetria científica, superfícies 3D e matrizes topológicas.
- **Hashlib / Padrão NIST FIPS 180-4:** Registro de integridade de dados via SHA-256 para auditoria local.

---

## 📂 Estrutura de Arquivos

| Arquivo | Descrição |
| :--- | :--- |
| `assembly_theory_life_mea.py` | Implementação base do algoritmo de montagem com Numba. |
| `assembly_tripla_fronteira_mea.py` | Comparativo entre ruído aleatório, padrão periódico e seleção informacional. |
| `assembly_waddington_autocura_mea.py` | Teste de resiliência e recuperação sob dano estrutural forçado. |
| `assembly_waddington_landscape_3d_mea.py` | Visualização tridimensional da superfície de potencial e trajetórias de relaxamento. |
| `assembly_master_thesis_benchmark_mea.py` | Ensaio comparativo de viabilidade integrada sob inversões ambientais. |
| `assembly_szathmary_darwinian_fission_mea.py` | Modelo populacional com fissão binária assimétrica e seleção de linhagem. |

---

## 🚀 Como Executar

### Pré-requisitos
Instale as dependências necessárias no terminal:

```bash
pip install numpy numba matplotlib
