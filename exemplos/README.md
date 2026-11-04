# Exemplos que conferem as contas dos guias

Os guias trazem números e fórmulas (frames, duração da raiz, velocidade do speed ramp). Aqui cada um vira um teste que dá para rodar, para você ver que a conta fecha e para alguém que mexer no guia saber se quebrou algo.

```bash
python3 exemplos/test_numeros.py -v
```

Só precisa do Python 3, sem instalar nada.

## O que cada teste confere
| Guia | O que o guia afirma | O que o teste mostra |
|---|---|---|
| `entrega-no-editor.md` | `frame = round(segundos × 30000 / 1001)` em 29,97; erro de taxa vira descompasso no fim | 1 s dá 30 frames; em 10 min a taxa 30 dá 18 000 frames e a 29,97 dá 17 982 (18 frames, 0,6 s); o descompasso cresce com o tempo; a ida e a volta não perdem frame |
| `hyperframes.md` | A duração da raiz é `(N − 0,5) / fps`; com a conta direta, alguns itens saem com 1 frame a mais | Com `(N − 0,5) / fps`, o render que arredonda para cima dá exatamente N, de N = 1 a 20 000, em 24, 25, 30, 60 e 29,97 fps, inclusive com a duração escrita em 3 casas. A conta direta erra em centenas de casos por ponto flutuante e em milhares ao escrever 3 casas |
| `oficio-motion.md` §4 | Velocidade final de `power4.in` = 4·D/T; inicial de `expo.out` ≈ 6,93·D/T; 700 px em 1 s e 560 px em 1,5 s casam (~2 800 e ~2 590 px/s) | As duas derivadas dão 4 e 6,93 (= 10·ln 2); as velocidades do exemplo ficam a menos de 10% uma da outra; com ~1 300 px na saída elas deixam de casar |

## O que isto não prova
- Só confere a **aritmética**. Não testa o HyperFrames, o GSAP nem o Premiere: as curvas usam as fórmulas `t⁴` e `1 − 2^(−10t)`, e a "duração arredondada para cima" do render é a regra que o guia descreve, não o código do HyperFrames.
- As armadilhas que dependem da ferramenta (desfoque de movimento, `fromTo`, fontes no render) continuam precisando do teste curto com a ferramenta de verdade, como diz `entrega-no-editor.md`.

## Como foi validado
Cada teste foi sabotado de propósito (trocar `(N − 0,5)` por `N`, arredondar para baixo em vez de ao mais próximo, usar `3·D/T`, usar 30 fps no lugar de 30000/1001) e falhou, como esperado.
