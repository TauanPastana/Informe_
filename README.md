# 📰 Informe — Agregador de Notícias do Brasil

O **Informe** é uma API desenvolvida em **Django** que coleta e centraliza as últimas notícias de diversos portais brasileiros (como **G1** e **CNN Brasil**), retornando-as em formato **JSON**.  
Os dados são obtidos por meio de **raspagem de conteúdo (web scraping)** com **BeautifulSoup** e servidos através de uma **API REST**, construída com **Django REST Framework (DRF)**.

---

## 🎯 Objetivo

O projeto tem como propósito **centralizar e facilitar o acesso** às últimas notícias publicadas em diferentes fontes, possibilitando:

- Consultas via API.  
- Análises e monitoramento de informação.  
- Integração com outros sistemas (frontends, bots, dashboards, etc.).  

---

## ⚙️ Funcionalidades

### 🧩 Funcionalidades Atuais

- **Coleta automática** das últimas notícias de portais brasileiros configurados (ex.: *G1*, *CNN Brasil*).  
- **Padronização dos dados** armazenados: título, resumo, link, data/hora de publicação, fonte/portal e imagem (quando disponível).  
- **API REST** com endpoints públicos para listar notícias e aplicar filtros, por exemplo:  
  - `?portal=cnn` — retorna apenas notícias da CNN Brasil.  
  - `?search=energia` — busca por termos específicos no título ou resumo.  

### 🚧 Funcionalidades Planejadas

- Adição de novas fontes e portais de notícias.  
- Implementação de filtros avançados (por data, categoria, relevância, etc.).  
- Documentação interativa dos endpoints (ex.: via **Swagger** ou **OpenAPI**).  

---

## 🕒 Atualização e Persistência dos Dados

- A raspagem é executada automaticamente a cada **30 minutos**, buscando novas publicações nas fontes configuradas.  
- As notícias são armazenadas por até **3 dias**. Um processo periódico remove conteúdos antigos, garantindo que apenas informações recentes permaneçam no banco de dados.  

---

## 🧱 Tecnologias Utilizadas

- **Python** — linguagem principal.  
- **Django** — framework backend para modelagem, ORM e interface administrativa.  
- **Django REST Framework (DRF)** — criação e estruturação da API REST (endpoints, filtros, paginação).  
- **BeautifulSoup** — extração e tratamento de dados via web scraping.  
- **SQLite** — banco de dados utilizado no ambiente de desenvolvimento.  

---

## 🗺️ Próximos Passos

No futuro, o projeto pretende disponibilizar um **frontend** que consuma essa API, exibindo as informações de forma interativa e amigável ao usuário.
