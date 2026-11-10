# Método Convênio Zero · página de pré-venda

Site estático (HTML, CSS e JS puros) publicado no GitHub Pages.

## Como editar

Tudo o que muda fica no bloco `CONFIG`, no topo do `index.html`:

| Chave | O que é |
|---|---|
| `CHECKOUT_URL` | Link do checkout da Kiwify. Os botões repassam UTMs e `fbclid` para ele. |
| `META_PIXEL_ID` | ID do Pixel do Meta. Vazio = o pixel não carrega. PageView e ViewContent ao carregar; InitiateCheckout no clique. Purchase fica na Kiwify. |
| `PRECO`, `MOEDA` | Valor exibido na página e enviado nos eventos do Pixel. |
| `DEPOIMENTO_VIDEO_URL`, `DEPOIMENTO_POSTER`, `DEPOIMENTO_NOME`, `DEPOIMENTO_DESCRICAO`, `DEPOIMENTO_FOTO` | Arquivo .mp4 em `assets/` (player nativo, 9:16) ou link *embed* do YouTube/Vimeo; capa; nome, descrição e foto redonda do caso real. Vazio = a seção fica oculta. |

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
