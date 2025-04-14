# SecureTrack - Backend API

Este é o repositório do **backend** da aplicação SecureTrack. Ele é uma API RESTful desenvolvida com **Flask**, projetada para gerenciar ativos e controles de segurança. com foco em para uma equipe de 

---

## 🚀 Funcionalidades

- Gerenciamento de ativos (criação, listagem, atualização e exclusão).
- Gerenciamento de controles de segurança.
- Relatórios de conformidade entre ativos e controles.

---

## 🛠️ Configuração do Ambiente Local

Siga os passos abaixo para configurar o ambiente local e executar o projeto.

### 1. Clonar o Repositório

Faça o clone deste repositório em sua máquina local:

```bash
git clone https://github.com/jella/securetrack-mvp-api.git
cd backend
```

---

## 🛠️5. Construir e Executar a Aplicação
Siga as etapas abaixo para construir e executar a aplicação com Docker.

Para Construir a Imagem do Docker:

```bash
docker run -p 5000:5000 \
  -v $(pwd)/db:/app \
  securetrack-api
```
Acesse a aplicação Flask no seu navegador em http://localhost:5000. Além disso, o Swagger também estará disponível.

## 🛠️5. Acessando o Banco de Dados PostgreSQL

Para Acessar o contêiner do PostgreSQL:

```bash
Copiar
docker exec -it flask-db psql -U user -d database_name
```

```plaintext
securetrack-mvp-api/
├── app/
│   ├── __init__.py         # Configuração do Flask e SQLAlchemy
│   ├── models/             # Modelos de banco de dados
│   ├── services/           # Lógica de negócios
│   ├── controllers/        # Rotas e endpoints
├── config.py               # Configurações do projeto
├── app.py                  # Ponto de entrada principal
├── requirements.txt        # Dependências do projeto
├── instance/               # Diretório para o banco SQLite
└── README.md               # Documentação do ]]
└── Dockerfile               # Documentação do ]]
└── Dockerfile               # Documentação do ]]

projeto
```

---
## 📁 Documentação da API
  
  [![Documentação da API](https://via.placeholder.com/400x200.png?text=Documenta%C3%A7%C3%A3o+da+API)](http://1localhost/3001/openapi/)


## 🔗

## 🔗 Integração com o Front-End

Certifique-se de que o front-end consuma os endpoints da API corretamente. Consulte o [repositório do front-end](https://github.com/jella/securetrack-mvp-frontend.git) para mais detalhes.

### Endpoints Principais

- **Ativos:**
  - **Listar Ativos (GET):** `/ativos`
  - **Criar Ativo (POST):** `/ativos`

- **Controles:**
  - **Listar Controles (GET):** `/controles`
  - **Criar Controle (POST):** `/controles`

- **Relatório de Conformidade:**
  - **Ver Relatório (GET):** `/conformidade/status`

---

## 👥 Contribuidores

- **Juliana Medella Pereira** - [LinkedIn](https://www.linkedin.com/in/juliana-medella/)
