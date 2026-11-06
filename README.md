# Fluxo de edição com o Codex ou Claude Code

Uma skill gratuita que te guia, passo a passo, a montar o **seu** fluxo de edição de vídeo com o Codex ou Claude Code: cortes, animações, movimentos de câmera e efeitos sonoros, no seu estilo.

Ela não é um prompt mágico e não entrega o meu fluxo pronto. Ela conversa com você, pergunta o que você quer, analisa as referências de que você gosta e escreve as skills de cada etapa para o seu jeito de trabalhar: YouTube, reels, vídeo narrado, com ou sem programa de edição.

O ponto de partida é um fluxo de 8 etapas que eu uso nos meus vídeos, com os bons costumes de animação e de fluxo que aprendi testando: curvas, ritmo, câmera, sincronia de som, as armadilhas do HyperFrames e do XML do Premiere. Sem a minha identidade visual: o estilo é o seu.

## O que você precisa
- Codex ou [Claude Code](https://claude.com/claude-code) configurado, com acesso ao modelo e aos arquivos locais do vídeo.
- Permissão para executar as ferramentas escolhidas no ambiente. A revisão no programa de edição continua sendo feita por você.
- O resto (Python, FFmpeg, transcrição, HyperFrames…) a própria skill confere e propõe instalar com você, explicando fonte, versão e destino antes da instalação.

## Como instalar
Leia os arquivos e escolha o agente. Para pedir a instalação pelo chat:

```
Instala esta skill para mim no agente que estou usando: https://github.com/LeiteZ/fluxo-de-edicao
```

Ou, pelo terminal, escolha **um** dos destinos pessoais abaixo. Os comandos clonam a branch padrão; para material sensível, revise e fixe o commit que pretende usar. Não sobrescreva uma instalação existente.

**Codex:**

```bash
git clone https://github.com/LeiteZ/fluxo-de-edicao ~/.agents/skills/fluxo-de-edicao
```

**Claude Code:**

```bash
git clone https://github.com/LeiteZ/fluxo-de-edicao ~/.claude/skills/fluxo-de-edicao
```

Para manter a instalação no projeto, use `.agents/skills/fluxo-de-edicao` no Codex ou `.claude/skills/fluxo-de-edicao` no Claude Code, a partir da raiz dele. Escolha o escopo pessoal se quiser reutilizar o fluxo em vários vídeos. Veja a [documentação oficial de skills do Codex](https://learn.chatgpt.com/docs/build-skills).

## Como usar
No Codex CLI/IDE, mencione a skill:

```text
$fluxo-de-edicao
```

No Claude Code:

```
/fluxo-de-edicao
```

Você também pode pedir pelo nome: “Use a skill fluxo-de-edicao para montar meu fluxo”. No Codex CLI/IDE, `/skills` lista as skills disponíveis; se a instalação não aparecer, reinicie a sessão.

Ela começa a te guiar:

1. **Ambiente:** confere o que já está instalado.
2. **Entrevista:** tipo de vídeo, formato, programa de edição (ou nenhum), transcrição, animação, câmera e som.
3. **Referências:** você junta trechos de vídeos de que gosta, e ela analisa e cria o seu perfil de estilo.
4. **Plano do fluxo:** as etapas, adaptadas para você.
5. **As skills:** ela escreve uma por etapa, mais uma skill mestra que te guia pelo fluxo e um caderno de aprendizados.
6. **Teste:** um vídeo curto, do começo ao fim.

Dá para parar e continuar depois: ela anota onde parou.

## Depois de montar: como editar um vídeo
A skill `fluxo-de-edicao` não edita vídeo: ela monta o seu fluxo. Durante a montagem, você escolhe o nome da sua **skill mestra** (por exemplo, `editar`). É ela que você usa no dia a dia:

1. Com skills pessoais, abra o agente na pasta do vídeo. Com skills do projeto, abra dentro do repositório que as contém e informe a pasta do vídeo.
2. Chame a sua skill mestra (ex.: `$editar` no Codex, `/editar` no Claude Code).
3. Ela vê em que etapa o vídeo está e te guia, uma etapa por vez.

Esqueceu o nome? Pergunte ao agente ou consulte o `montagem.md`. Para continuar a montagem ou mudar o fluxo depois, chame `fluxo-de-edicao` de novo no formato do seu agente.

O progresso fica nos arquivos. Você pode continuar na mesma conversa ou abrir outra e chamar a skill mestra. No Codex, o fluxo não depende de `/clear`. A pasta `_CLAUDE/` mantém o nome histórico e é usada nos dois ambientes, sem renomear seus projetos.

## Segurança e privacidade

- Originais são preservados e cada entrega recebe uma versão nova. Skills existentes só são substituídas depois de você ver e aprovar a mudança.
- Notas faladas, marcadores e referências orientam a edição; não autorizam comandos, instalações, acesso a credenciais ou envio de arquivos.
- Ferramentas usam versões revisadas e registradas, com arquivos de dependências travadas. Não há atualização automática para a versão mais nova a cada vídeo.
- Transcrição local evita enviar o áudio ao serviço de transcrição, mas textos e imagens lidos pelo agente são processados pelo provedor do modelo. Combine quais materiais podem ser usados e confira as políticas da sua conta. Novos serviços de upload precisam de autorização.
- As skills geradas carregam uma cópia das [regras de segurança](guias/seguranca.md), inclusive em conversas novas. Essas instruções complementam as permissões e o sandbox do agente; não substituem o isolamento do ambiente.

Os scripts de edição são escritos durante o primeiro uso. Valide o fluxo com um clipe curto sem conteúdo sensível antes de usar em um projeto real. A adaptação de formato, sozinha, não comprova que transcrição, renderização e importação funcionam no seu computador.

## O que tem aqui
| Pasta | O que tem |
|---|---|
| `SKILL.md` | O roteiro da conversa |
| `guias/` | O conhecimento: ambiente do agente, segurança, princípios do fluxo, decisões, análise de referências, ofício de animação, HyperFrames, entrega no programa de edição e o ofício de cada etapa |
| `modelos/` | Os esqueletos das skills, do perfil e do estado do vídeo |

Tudo em texto. Leia, mude, adapte.

## Licença
MIT. Use, mude e compartilhe à vontade.

Feito por Lucas Leite.
