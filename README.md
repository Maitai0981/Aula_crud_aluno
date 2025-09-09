# Sistema de Cadastro de Alunos - Django

Sistema CRUD para cadastro de alunos com upload de imagens, desenvolvido em Django REST Framework.

## Funcionalidades

- ✅ Cadastro de alunos com foto
- ✅ Listagem de alunos
- ✅ Edição de dados dos alunos
- ✅ Exclusão de alunos
- ✅ Upload e remoção de imagens
- ✅ Interface web responsiva
- ✅ API REST completa

## Tecnologias Utilizadas

- **Backend**: Django 5.0 + Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Banco de Dados**: SQLite (padrão) - facilmente configurável para PostgreSQL/MySQL
- **Upload de Arquivos**: Django + Pillow

## Instalação e Configuração

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar Banco de Dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Criar Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

### 4. Executar o Servidor

```bash
python manage.py runserver
```

O sistema estará disponível em: `http://localhost:8000`

## Estrutura da API

### Endpoints Disponíveis

- `GET /api/alunos/listar` - Lista todos os alunos
- `POST /api/alunos/cadastrar` - Cadastra novo aluno
- `GET /api/alunos/{id}` - Busca aluno por ID
- `PUT /api/alunos/` - Atualiza aluno existente
- `DELETE /api/alunos/{id}` - Exclui aluno
- `DELETE /api/alunos/remover-imagem/{id}` - Remove imagem do aluno

### Formato dos Dados

```json
{
  "id": 1,
  "nome": "João Silva",
  "serie": "3º Ano",
  "sexo": "M",
  "data": "2024-01-15",
  "imagemBase64": "data:image/jpeg;base64,..."
}
```

## Funcionalidades da Interface

- **Upload de Imagens**: Arrastar e soltar ou selecionar arquivos
- **Pré-visualização**: Visualização da imagem antes do envio
- **Validação**: Validação de tipos de arquivo e tamanho (máx. 10MB)
- **Responsivo**: Interface adaptável para dispositivos móveis
- **Modal de Imagem**: Visualização ampliada das fotos

## Configurações Avançadas

### Banco de Dados PostgreSQL

1. Instale o psycopg2: `pip install psycopg2-binary`
2. Configure no `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Variáveis de Ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```bash
cp .env.example .env
```

## Testes

Execute os testes com:

```bash
python manage.py test
```

## Administração

Acesse o painel administrativo em: `http://localhost:8000/admin`

## Estrutura do Projeto

```
├── student_crud/          # Configurações do Django
├── students/              # App principal
│   ├── models.py         # Modelo Aluno
│   ├── views.py          # Views da API
│   ├── serializers.py    # Serializers DRF
│   ├── urls.py           # URLs da API
│   └── admin.py          # Configuração do admin
├── static/               # Arquivos estáticos (CSS, JS)
├── templates/            # Templates HTML
├── media/                # Upload de imagens
└── requirements.txt      # Dependências Python
```

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT.