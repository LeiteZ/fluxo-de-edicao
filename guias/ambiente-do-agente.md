# Ambiente do agente

O ofício de edição é o mesmo no Codex e no Claude Code. Resolva os caminhos e a forma de chamar as skills antes de escrever qualquer uma. Use o ambiente em que esta skill foi aberta; pergunte só se ele não estiver claro.

## Caminhos e comandos

| Ambiente | Skills pessoais | Skills do projeto | Como chamar |
|---|---|---|---|
| Codex | `~/.agents/skills/` | `<raiz do projeto>/.agents/skills/` | No CLI/IDE: `$fluxo-de-edicao` e `$editar`; também pode pedir pelo nome |
| Claude Code | `~/.claude/skills/` | `<raiz do projeto>/.claude/skills/` | `/fluxo-de-edicao` e `/editar` |

- Para reutilizar o fluxo em vários vídeos, sugira skills pessoais. Se a pessoa quiser manter tudo num repositório, use o escopo do projeto. Registre a escolha e o caminho absoluto em `montagem.md`; não instale nos dois lugares automaticamente.
- No escopo do projeto, abra o Codex dentro desse repositório; as skills não ficam disponíveis automaticamente ao abrir um vídeo em outra pasta fora dele. Para vídeos espalhados pelo computador, prefira o escopo pessoal ou combine onde o agente será aberto, sem mover os vídeos.
- `<pasta de skills>` nos modelos é a pasta escolhida. `<comando da montagem>`, `<comando da skill mestra>` e `<comando da etapa>` incluem o prefixo do ambiente (`$` ou `/`). O campo `name` e o nome da pasta nunca incluem esse prefixo.
- Substitua esses campos por valores concretos em todas as skills geradas, inclusive nas descrições e nos caminhos das regras comuns. Para chamar outra etapa, leia o `SKILL.md` dela pelo caminho registrado e siga-o na sessão; não execute `$editar` ou `/editar` no terminal.
- No Codex, use apenas letras minúsculas, números e hífens nos nomes, com menos de 64 caracteres. Ex.: `edit-camera`. Não aceite barras, `..` ou nomes que escapem da pasta de skills. Confira colisões antes de gravar.
- O Codex permite listar as skills com `/skills` no CLI/IDE. Se uma skill nova não aparecer, reinicie a sessão. Consulte a [documentação oficial de skills](https://learn.chatgpt.com/docs/build-skills) se a interface usada for diferente.

## Arquivos e retomada

- `_CLAUDE/` é o nome histórico da pasta de trabalho do vídeo e continua válido nos dois agentes. Não renomeie projetos existentes por causa da adaptação.
- A continuidade vem de `montagem.md`, `projeto.json` e dos arquivos do perfil. Salve as decisões e pendências antes de encerrar; uma conversa nova deve reler as regras comuns e a segurança antes de retomar.
- No Codex, a pessoa pode continuar na mesma conversa ou abrir outra na pasta do vídeo e chamar a skill mestra. Não prescreva `/clear` nem suponha troca automática de modelo. No Claude Code, `/clear` continua sendo uma opção da pessoa, depois de salvar o estado.
- Registre agente, escopo, pasta de skills e comandos no `montagem.md`. Se estiver retomando uma montagem antiga, complete só os campos ausentes; mudar de agente ou instalar novas cópias exige uma escolha da pessoa.

## Execução local

O ambiente precisa ter acesso aos arquivos do vídeo e às ferramentas escolhidas. Não prometa GPU, navegador, áudio ou editor gráfico sem conferir a disponibilidade. No Codex, respeite o sandbox e as permissões de arquivos e rede da sessão; não altere a configuração para contornar um bloqueio. A revisão no Premiere, Resolve ou outro editor continua sendo feita pela pessoa.
