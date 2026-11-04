"""Exemplos que conferem as contas citadas nos guias. Só biblioteca padrão do Python.

Rodar (de dentro da pasta do repositório):
    python3 -m unittest -v exemplos/test_numeros.py

O que isto prova: a ARITMÉTICA que os guias afirmam (conversão de frames, duração da raiz, velocidade do
speed ramp). O que NÃO prova: o comportamento do HyperFrames, do GSAP ou do Premiere. Para isso, o teste curto
com a ferramenta de verdade (`entrega-no-editor.md`, "Teste curto primeiro") continua sendo necessário.
As curvas usam as fórmulas matemáticas: power4.in = t^4 e expo.out = 1 - 2^(-10 t).
"""
import math
import unittest
from fractions import Fraction

NTSC = Fraction(30000, 1001)  # "29,97": a taxa real é 30000/1001, não 29.97


def para_frame(segundos, fps):
    """`entrega-no-editor.md`: converter segundos em frames inteiros, no frame mais próximo, num lugar só.
    Usa Fraction e arredonda metade para cima (o round() do Python arredonda metade para o par)."""
    return math.floor(Fraction(segundos) * Fraction(fps) + Fraction(1, 2))


class ConversaoDeFrames(unittest.TestCase):
    """guias/entrega-no-editor.md: 'frame = round(segundos x 30000 / 1001)'."""

    def test_um_segundo_a_29_97_sao_30_frames(self):
        self.assertEqual(para_frame(1, NTSC), 30)

    def test_ida_e_volta_nao_perde_frame(self):
        # frame n -> segundos n/fps -> frame de novo tem de dar n, para qualquer n
        for n in range(0, 200_000, 37):
            self.assertEqual(para_frame(Fraction(n) / NTSC, NTSC), n, n)

    def test_usar_30_no_lugar_de_29_97_causa_descompasso_crescente(self):
        # 'o erro aparece como descompasso no fim': em 10 minutos são 18 frames (0,6 s)
        com_taxa_certa = para_frame(600, NTSC)
        com_taxa_errada = para_frame(600, 30)
        self.assertEqual((com_taxa_certa, com_taxa_errada), (17982, 18000))
        self.assertEqual(com_taxa_errada - com_taxa_certa, 18)

    def test_descompasso_cresce_com_o_tempo(self):
        d = lambda s: para_frame(s, 30) - para_frame(s, NTSC)
        self.assertLess(d(60), d(600))
        self.assertLess(d(600), d(3600))

    def test_o_literal_29_97_quase_acerta_mas_a_fracao_e_a_forma_segura(self):
        # 29.97 e 30000/1001 diferem em ~0,00003 fps: em 1 h dá menos de 1 frame de diferença,
        # então o literal passa batido em testes curtos. A fração evita o problema por construção.
        diferenca = abs(para_frame(3600, Fraction(2997, 100)) - para_frame(3600, NTSC))
        self.assertLessEqual(diferenca, 1)


class DuracaoDaRaiz(unittest.TestCase):
    """guias/hyperframes.md: 'a duração da raiz é (N - 0,5) / fps ... o render arredonda duração x fps para cima;
    com a conta direta, alguns itens saem com 1 frame a mais.'"""

    FPS = {"24": 24.0, "25": 25.0, "30": 30.0, "60": 60.0, "29,97": 30000 / 1001}

    @staticmethod
    def frames_do_render(duracao, fps):
        return math.ceil(duracao * fps)  # o render 'arredonda para cima', como diz o guia

    def test_formula_do_guia_sempre_da_exatamente_n_frames(self):
        for nome, fps in self.FPS.items():
            for n in range(1, 20_001):
                duracao = (n - 0.5) / fps
                self.assertEqual(self.frames_do_render(duracao, fps), n, f"{nome} fps, N={n}")

    def test_formula_do_guia_aguenta_duracao_gravada_com_3_casas(self):
        # duração escrita em decimal curto (ex.: 0.333) é comum em arquivo de projeto
        for nome, fps in self.FPS.items():
            for n in range(1, 20_001):
                duracao = round((n - 0.5) / fps, 3)
                self.assertEqual(self.frames_do_render(duracao, fps), n, f"{nome} fps, N={n}")

    def test_conta_direta_erra_em_muitos_casos(self):
        # o problema que o guia descreve existe: N/fps x fps cai em N+1 por erro de ponto flutuante
        # e, pior, por arredondar a duração para 3 casas
        for nome in ("25", "30", "29,97"):
            fps = self.FPS[nome]
            erros_float = [n for n in range(1, 20_001) if self.frames_do_render(n / fps, fps) != n]
            self.assertGreater(len(erros_float), 0, f"{nome} fps: conta direta em float deveria errar em algum N")
            erros_3_casas = [n for n in range(1, 20_001) if self.frames_do_render(round(n / fps, 3), fps) != n]
            self.assertGreater(len(erros_3_casas), 100, f"{nome} fps: com 3 casas deveria errar bastante")

    def test_a_30_fps_o_primeiro_erro_da_conta_direta_e_conhecido(self):
        primeiro = next(n for n in range(1, 20_001) if self.frames_do_render(n / 30.0, 30.0) != n)
        self.assertEqual(self.frames_do_render(primeiro / 30.0, 30.0), primeiro + 1)


class SpeedRamp(unittest.TestCase):
    """guias/oficio-motion.md §4: 'velocidade final do power4.in = 4·D/T; inicial do expo.out ~ 6,93·D/T'."""

    @staticmethod
    def derivada_em_0(f, h=1e-9):
        return (f(h) - f(0)) / h

    @staticmethod
    def derivada_em_1(f, h=1e-9):
        return (f(1) - f(1 - h)) / h

    power4_in = staticmethod(lambda t: t ** 4)
    expo_out = staticmethod(lambda t: 1 - 2 ** (-10 * t))

    def test_power4_in_termina_a_4_vezes_a_velocidade_media(self):
        self.assertAlmostEqual(self.derivada_em_1(self.power4_in), 4.0, places=4)

    def test_expo_out_comeca_a_6_93_vezes_a_velocidade_media(self):
        self.assertAlmostEqual(self.derivada_em_0(self.expo_out), 6.93, places=2)
        self.assertAlmostEqual(self.derivada_em_0(self.expo_out), 10 * math.log(2), places=4)

    def test_exemplo_do_guia_700px_em_1s_e_560px_em_1_5s(self):
        saida = 4 * 700 / 1.0           # px/s no frame do corte (saída)
        chegada = 6.93 * 560 / 1.5      # px/s no frame do corte (chegada)
        self.assertEqual(saida, 2800)
        self.assertAlmostEqual(chegada, 2590, delta=5)
        # 'casar a velocidade no corte': as duas ficam dentro de ~10% uma da outra
        self.assertLess(abs(saida - chegada) / saida, 0.10)

    def test_com_1300px_no_mesmo_tempo_as_velocidades_nao_casam(self):
        # o exemplo errado do guia ('com ~1.300 px o conteúdo some antes do corte'): 1300 px em 1 s
        # sai a 5.200 px/s e a chegada de 560 px em 1,5 s continua a ~2.590 px/s
        self.assertGreater(abs(4 * 1300 / 1.0 - 6.93 * 560 / 1.5) / (4 * 1300 / 1.0), 0.4)


if __name__ == "__main__":
    unittest.main()
