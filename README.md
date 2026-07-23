# Idle Bud — Internal Documentation

Este repositório mantém a documentação interna viva e oficial de **Idle Bud**.

## Portal

O conteúdo é publicado pelo GitHub Pages a partir do workflow em `.github/workflows/pages.yml`.

Endereço permanente:

`https://gezada.github.io/idlebud-internaldocs/`

O portal centraliza:

- **Game Design Document** — documento vivo disponível em `/gdd/`;
- **Economy** — TBD;
- **Enemies, Drops, Itemization & Forge** — TBD;
- **Technology Guidelines** — TBD.

## Publicação

O GitHub Pages usa **GitHub Actions**. O workflow reconstrói o GDD a partir do payload estático, aplica os patches validados, publica o documento em `/gdd/` e gera a página inicial e os documentos placeholder.

## Estrutura publicada

- `/` — portal de documentação;
- `/gdd/` — Game Design Document;
- `/economy/` — TBD;
- `/enemies-drops-craft/` — TBD;
- `/technology-guidelines/` — TBD.
