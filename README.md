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

### 2. Configurar o Ambiente Virtual

Crie e ative um ambiente virtual para gerenciar as dependências do projeto:

- **Linux/Mac:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

---

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

---

### 4. Configurar o Banco de Dados

Certifique-se de que o diretório `instance/` exista para armazenar o arquivo do banco de dados SQLite:

```bash
mkdir instance
```

Inicialize o banco de dados executando o seguinte comando no shell do Flask:

```bash
flask shell
```

E dentro do shell, execute:

```python
from app import db
db.create_all()
```

---

### 5. Iniciar o Servidor

Execute o servidor Flask localmente:

```bash
python app.py
```

O servidor estará disponível em: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## 📁 Estrutura do Projeto

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
└── README.md               # Documentação do projeto
```

---

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
