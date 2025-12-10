# 🚀 GERADOR DE RELATÓRIO FISCAL - GUIA RÁPIDO

## ✨ CARACTERÍSTICAS

✅ **Executável standalone** - Funciona em qualquer Windows (com ou sem Python)  
✅ **Detecção automática do servidor** - Usa o nome do PC automaticamente  
✅ **Simples de configurar** - Apenas ajuste o nome do banco de dados  
✅ **Gera Excel automaticamente** - Salva na pasta C:/MHI  

---

## ⚡ PASSO A PASSO

### PASSO 1: Configure o arquivo .env
Configure o arquivo .env seguindo o exemplo do .env.example

### Passo 2: Instale as dependências

1. Abra o Prompt de Comando (CMD) como Administrador
2. Navegue até a pasta onde está o arquivo `consulta_fiscal.py`
3. Execute o comando:
   ```
   pip install -r requirements.txt
   ```
### PASSO 2: Gere o executável
Execute o arquivo: `gerar_executavel.bat`

### PASSO 3: Use!
Execute como Administrador `dist/Relatorio_Fiscal.exe` em qualquer PC Windows

O arquivo `Relatorio_Fiscal.exe` pode ser copiado para qualquer computador Windows e funcionará **sem precisar instalar Python**!

**Requisitos no computador de destino:**
- Windows 7 ou superior
- SQL Server instalado localmente
- Driver ODBC do SQL Server instalado ([Download aqui](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server))
- Permissões de escrita na pasta C:/MHI

O programa irá:
   - ✅ Detectar automaticamente o nome do PC
   - ✅ Conectar ao SQL Server local usando o nome do PC
   - ✅ Executar as duas consultas SQL
   - ✅ Gerar um arquivo Excel na pasta C:/MHI
   - ✅ Nomear como: `[Nome da Loja] - [CNPJ].xlsx`

O arquivo Excel conterá duas abas:
- **REGRAS FISCAIS**: Resultado da primeira consulta
- **CADASTRO DE PRODUTOS**: Resultado da segunda consulta

---

## 📋 ARQUIVOS INCLUÍDOS

| Arquivo | Descrição |
|---------|-----------|
| `consulta_fiscal.py` | Código-fonte principal |
| `requirements.txt` | Dependências Python |
| `gerar_executavel.bat` | Script para gerar o .exe |
| `README.md` | Este arquivo |

---

## 🎯 COMO FUNCIONA

1. **Detecta o nome do PC** automaticamente (ex: "CAIXA01")
2. **Conecta ao SQL Server** local usando esse nome
3. **Executa 2 consultas SQL** (Regras Fiscais + Cadastro de Produtos)
4. **Gera arquivo Excel** com 2 abas na área de trabalho
5. **Nomeia automaticamente** como: `[Nome Loja] - [CNPJ].xlsx`

---

## ⚠️ SOLUÇÃO DE PROBLEMAS

### ✗ Erro: Uma ou mais consultas falharam.
Se após executar o programa, retornar o seguinte erro:

```': ('21000', '[21000] [Microsoft][ODBC SQL Server Driver][SQL Server]Subquery returned more than 1 value. This is not permitted when the subquery follows =, !=, <, <= , >, >= or when the subquery is used as an expression. (512) (SQLExecDirectW)')
```

Significa que existem produtos de mais de uma loja no banco de dados.
Nesse caso, é necessário deletar os registros da loja que não correponde à licença autenticada. Delete também das tabelas [Grupo Subgrupo], [Composições] e [Adicionais].


### Erro: "Nome do servidor inválido"
**Causa**: SQL Server não está instalado no computador local
**Solução**: Instale o SQL Server ou ajuste o código para conectar a um servidor remoto

### Erro de conexão com banco de dados:
O programa agora mostra qual servidor foi detectado. Verifique:
- ✅ SQL Server está em execução no computador
- ✅ Nome do banco de dados está correto no código
- ✅ Usuário tem permissão para acessar o banco
- ✅ Windows Authentication está habilitado no SQL Server

### Erro "ODBC Driver não encontrado":
Instale o driver ODBC do SQL Server:
- Baixe em: https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
- Instale a versão 17 ou superior

### Arquivo não é salvo na pasta:
- Verifique as permissões de escrita
- Execute o programa como Administrador

### Consultas retornam vazio:
- Verifique se existem dados na tabela `estoque`
- Confirme os filtros da query (desativado = 0, etc.)

### Antivírus bloqueia o executável:
- Adicione exceção no antivírus
- Assine digitalmente o executável (opcional, para distribuição corporativa)

## 📞 INFORMAÇÕES ADICIONAIS

- O executável tem aproximadamente 50-100 MB (inclui Python e bibliotecas)
- Funciona offline (não precisa de internet)
- Os arquivos gerados sobrescrevem versões anteriores com o mesmo nome
- O programa exibe mensagens de progresso durante a execução
- Mostra qual servidor foi detectado automaticamente
- Pressione Enter ao final para fechar o programa

**Atualizado em 10/12/2025**
