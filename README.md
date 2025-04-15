
# 📡 SecureTrack - Backend API

Este é o repositório do **backend** da aplicação **SecureTrack**. Ele é uma API RESTful desenvolvida com **Flask**, projetada para gerenciar ativos, controles de segurança e conformidades, com foco no suporte a equipes de segurança da informação.

---

## 🚀 Funcionalidades

- ✅ Gerenciamento de ativos (criação, listagem, atualização, exclusão e consulta de IP).
- ✅ Gerenciamento de controles de segurança.
- ✅ Relatórios de conformidade entre ativos e controles.
- ✅ Cadastro e gerenciamento de responsáveis.
- ✅ Consulta manual e automática de informações de IP via IPinfo.

---

## 🛠️ Configuração do Ambiente Local

Siga os passos abaixo para configurar o ambiente local e executar o projeto.

### 1. Clonar o Repositório

```bash
git clone https://github.com/jella/securetrack-mvp-api.git
cd backend
```

---

### 2. Construir e Executar a Aplicação com Docker

#### 👉 Para buildar:
```bash
docker build -t securetrack-api .
```

#### 👉 Para rodar:
```bash
docker run -p 5000:5000 securetrack-api
```

Depois, acesse a aplicação em:
- `http://localhost:5000`

E a documentação Swagger em:
- `http://localhost:5000/openapi/swagger`

---

## 📁 Documentação da API

[![Documentação da API](https://via.placeholder.com/400x200.png?text=Documenta%C3%A7%C3%A3o+da+API)](http://localhost:5000/openapi/)

---

## 🔗 Integração com o Front-End

Consulte o repositório do front-end para integração:
🔗 [securetrack-mvp-frontend](https://github.com/jella/securetrack-mvp-frontend.git)

---

## 📌 Endpoints Principais

### 🔹 Ativos

| Método | Rota                        | Descrição                                      |
|--------|-----------------------------|-----------------------------------------------|
| GET    | `/ativos/`                  | Lista todos os ativos                         |
| POST   | `/ativos/`                  | Cria um novo ativo                            |
| GET    | `/ativos/{id}`              | Consulta um ativo específico                  |
| PUT    | `/ativos/{id}`              | Atualiza um ativo existente                   |
| DELETE | `/ativos/{id}`              | Remove um ativo                               |
| GET    | `/ativos/{id}/ipinfo`       | Consulta IP automaticamente via IPinfo        |
| GET    | `/ativos/ipinfo/manual?ip=` | Consulta IP manual fornecendo via query param |

---

### 🔹 Controles

| Método | Rota         | Descrição                |
|--------|--------------|--------------------------|
| GET    | `/controles/`| Lista todos os controles |
| POST   | `/controles/`| Cria um novo controle    |

---

### 🔹 Conformidades

| Método | Rota                      | Descrição                                          |
|--------|---------------------------|----------------------------------------------------|
| GET    | `/conformidades/`         | Lista todas as conformidades                       |
| POST   | `/conformidades/`         | Cria uma nova conformidade                         |
| GET    | `/conformidades/status/`  | Lista conformidades filtradas por status (query param `status` com valores `Pendente`, `Andamento`, `Implementada`, `Todos`) |

---

### 🔹 Responsáveis

| Método | Rota                 | Descrição                            |
|--------|----------------------|--------------------------------------|
| GET    | `/responsaveis/`     | Lista todos os responsáveis          |
| POST   | `/responsaveis/`     | Cria um novo responsável             |
| GET    | `/responsaveis/{id}` | Consulta um responsável específico   |
| DELETE | `/responsaveis/{id}` | Remove um responsável específico     |

---

## 🌐 Integração com a API Externa IPinfo

O SecureTrack integra-se à API do [IPinfo](https://ipinfo.io/developers) para enriquecer os dados dos ativos com informações geográficas e de rede com base no endereço IP fornecido. Esta funcionalidade permite obter detalhes como localização, organização, ASN, entre outros, facilitando a análise e o gerenciamento dos ativos.

### 🔧 Como Funciona

- **Endpoint Manual**: `/ativos/ipinfo/manual?ip={IP}`  
  Permite consultar informações de um IP específico fornecido como parâmetro na URL.

- **Endpoint por ID de Ativo**: `/ativos/{id}/ipinfo`  
  Recupera o endereço IP do ativo com o ID fornecido e consulta suas informações na API do IPinfo.

### 🔐 Autenticação

Para utilizar a API do IPinfo, é necessário um token de acesso. Este token pode ser obtido gratuitamente ao se registrar em [ipinfo.io/signup](https://ipinfo.io/signup). O token deve ser incluído nas requisições da seguinte forma:

- **Como parâmetro na URL**:
  ```
  https://ipinfo.io/{IP}/json?token=SEU_TOKEN
  ```

- **No cabeçalho da requisição**:
  ```
  Authorization: Bearer SEU_TOKEN
  ```

**Nota**: Certifique-se de substituir `SEU_TOKEN` pelo seu token real fornecido pelo IPinfo.

### 📄 Exemplo de Resposta

```json
{
  "ip": "8.8.8.8",
  "hostname": "dns.google",
  "city": "Mountain View",
  "region": "California",
  "country": "US",
  "loc": "37.3860,-122.0838",
  "org": "AS15169 Google LLC",
  "postal": "94035",
  "timezone": "America/Los_Angeles"
}
```

### ⚠️ Considerações

- **Limites de Requisições**: A conta gratuita do IPinfo possui limites de requisições mensais. Verifique os detalhes no [site oficial](https://ipinfo.io/pricing).

---

## 🧱 Estrutura dos Schemas

### 🔸 Ativo
```json
{
  "nome": "Servidor X",
  "tipo": "Servidor",
  "responsavel": "João Silva",
  "status": "Ativo",
  "ip": "192.168.0.1",
  "observacoes": "Servidor de produção"
}
```

### 🔸 Controle
```json
{
  "codigo": "CM-02",
  "descricao": "Controle de mudanças organizacionais.",
  "categoria": "Gestão de mudanças",
  "anotacoes": "Controle voltado para garantir que as mudanças sejam seguras."
}
```

### 🔸 Conformidade
```json
{
  "ativo_id": 1,
  "controle_id": 3,
  "status": "Pendente"
}
```

### 🔸 Responsável
```json
{
  "nome": "João Silva",
  "email": "joao@empresa.com",
  "status": "Ativo"
}
```

---

## ⚠️ Respostas de Erro

Os erros são padronizados no seguinte formato:

```json
{
  "mensagem": "Campo obrigatório ausente.",
  "erro": "nome"
}
```

Em caso de erros de validação (HTTP 422), a resposta pode conter uma lista com a localização e o tipo do erro.

---

## 👥 Contribuidores

- [@jella](https://github.com/jella)

---
