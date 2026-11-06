# Método Convênio Zero · página de pré-venda

Site estático (HTML, CSS e JS puros) publicado no GitHub Pages.

## Como editar

Tudo o que muda fica no bloco `CONFIG`, no topo do `index.html`:

| Chave | O que é |
|---|---|
| `CHECKOUT_URL` | Link do checkout da Kiwify. Enquanto for `#oferta`, os botões só rolam até a oferta. |
| `META_PIXEL_ID` | ID do Pixel do Meta. Vazio = o pixel não carrega. |
| `DEPOIMENTO_VIDEO_URL` | Link *embed* do vídeo (YouTube/Vimeo). Vazio = a seção fica oculta. |
| `DEPOIMENTO_NOME` | Nome e especialidade de quem dá o depoimento. |
| `PRECO_FUNDADOR`, `PRECO_CHEIO`, `PRECO_CLUBE` | Valores exibidos na página. |
| `DATA_DECISAO`, `DATA_MODULO_1` | Data limite da turma e liberação do Módulo 1. |

A meta tag de verificação de domínio do Meta entra no `<head>`, onde está o comentário indicando.

## Fotos

Coloque `gustavo-retrato.jpg` e `gustavo-trabalhando.jpg` em `assets/` e rode:

```bash
python3 scripts/otimizar-fotos.py
```

O script gera os `.webp` com até 1600px de largura. Enquanto as fotos não existirem, as molduras mostram o monograma.

## Domínio próprio

Quando o domínio `conveniozero.com.br` estiver apontado, troque as três URLs absolutas no `<head>` (`canonical`, `og:url` e `og:image`/`twitter:image`) e crie o arquivo `CNAME` na raiz com o conteúdo `conveniozero.com.br`.

## Onde está publicado

Hoje o site está no Netlify, no projeto `conveniozero`: https://conveniozero.netlify.app/ (painel: https://app.netlify.com/projects/conveniozero). Para reenviar depois de uma alteração, use o deploy manual pelo painel (arraste a pasta do projeto) ou conecte o repositório do GitHub ao projeto no Netlify para publicar a cada push.
