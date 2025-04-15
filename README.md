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

## 🛠️5. Construir e Executar a Aplicação com docker


## 👉 Para buildar:
```bash
docker build -t securetrack-api .
```

## 👉 Para rodar:
```bash
docker run -p 5000:5000 securetrack-api
```

Depois, acesse a aplicação em:
http://localhost:5000
E a documentação Swagger:
http://localhost:5000/openapi/swagger
Siga as etapas abaixo para construir e executar a aplicação com Docker.

## 📁 Documentação da API
  
  [![Documentação da API](https://via.placeholder.com/400x200.png?text=Documenta%C3%A7%C3%A3o+da+API)](http://localhost/5000/openapi/)


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
