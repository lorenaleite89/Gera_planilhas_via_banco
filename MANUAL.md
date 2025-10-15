# MANUAL DE INSTALAÇÃO E USO - GERADOR DE RELATÓRIO FISCAL

## 📋 REQUISITOS

- Windows 7 ou superior
- Python 3.8 ou superior instalado (APENAS para gerar o executável)
- SQL Server instalado no computador
- Driver ODBC do SQL Server instalado
- Permissões de escrita na área de trabalho

## ✨ NOVIDADE: DETECÇÃO AUTOMÁTICA DO SERVIDOR

O executável agora detecta **automaticamente** o nome do computador e usa como servidor SQL.

**Você NÃO precisa mais configurar o servidor!**

## 🔧 PASSO 1: INSTALAÇÃO DAS DEPENDÊNCIAS (Apenas para gerar o .exe)

1. Abra o Prompt de Comando (CMD) como Administrador
2. Navegue até a pasta onde está o arquivo `consulta_fiscal.py`
3. Execute o comando:
   ```
   pip install -r requirements.txt
   ```

## ⚙️ PASSO 2: CONFIGURAÇÃO DO BANCO DE DADOS

Abra o arquivo `consulta_fiscal.py` em um editor de texto e localize a função `conectar_banco()` (linha ~15).

**Você só precisa ajustar UMA linha:**

```python
database = 'SEU_BANCO'   # ⬅️ Altere para o nome do seu banco de dados
```

**Exemplo:**
```python
database = 'VendasDB'
# ou
database = 'Estoque2024'
```

### ✅ O que é detectado automaticamente:
- **Servidor**: Nome do computador (via variável de ambiente COMPUTERNAME)
- **Autenticação**: Windows Authentication (Trusted_Connection)

### Opções de Autenticação:

**Opção 1 - Autenticação do Windows (Padrão - Recomendado):**
```python
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
```
✅ Esta opção já está ativa por padrão

**Opção 2 - Autenticação SQL Server:**
Se precisar usar usuário e senha:
1. Configure username e password
2. Comente a linha com `Trusted_Connection=yes`
3. Descomente a linha:
```python
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
```

## 🚀 PASSO 3: GERAR O EXECUTÁVEL (.EXE)

### Método 1 - Automático (Recomendado):
1. Execute o arquivo `gerar_executavel.bat`
2. Aguarde a conclusão (pode levar alguns minutos)
3. O executável estará em `dist/Relatorio_Fiscal.exe`

### Método 2 - Manual:
```
pyinstaller --onefile --console --name="Relatorio_Fiscal" consulta_fiscal.py
```

## 📦 DISTRIBUIÇÃO DO EXECUTÁVEL

O arquivo `Relatorio_Fiscal.exe` pode ser copiado para qualquer computador Windows e funcionará **sem precisar instalar Python**!

**Requisitos no computador de destino:**
- Windows 7 ou superior
- SQL Server instalado localmente
- Driver ODBC do SQL Server

## 📝 COMO USAR O EXECUTÁVEL

1. Copie o arquivo `Relatorio_Fiscal.exe` para o computador
2. Execute o arquivo (duplo clique)
3. O programa irá:
   - ✅ Detectar automaticamente o nome do PC
   - ✅ Conectar ao SQL Server local usando o nome do PC
   - ✅ Executar as duas consultas SQL
   - ✅ Gerar um arquivo Excel na área de trabalho
   - ✅ Nomear como: `[Nome da Loja] - [CNPJ].xlsx`

4. O arquivo Excel conterá duas abas:
   - **REGRAS FISCAIS**: Resultado da primeira consulta
   - **CADASTRO DE PRODUTOS**: Resultado da segunda consulta

## 🔍 EXEMPLO DE FUNCIONAMENTO

Se o executável for executado em um PC chamado **"CAIXA01"**:
- Servidor detectado: `CAIXA01`
- String de conexão: `DRIVER={SQL Server};SERVER=CAIXA01;DATABASE=SeuBanco;Trusted_Connection=yes;`

Se o executável for executado em um PC chamado **"NOTEBOOK-LOJA"**:
- Servidor detectado: `NOTEBOOK-LOJA`
- String de conexão: `DRIVER={SQL Server};SERVER=NOTEBOOK-LOJA;DATABASE=SeuBanco;Trusted_Connection=yes;`

## ⚠️ SOLUÇÃO DE PROBLEMAS

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

### Arquivo não é salvo na área de trabalho:
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

## 🎯 VANTAGENS DA DETECÇÃO AUTOMÁTICA

✅ Mesmo executável funciona em todos os computadores  
✅ Não precisa ajustar configuração para cada PC  
✅ Reduz erros de configuração  
✅ Facilita a manutenção  
✅ Simplifica o deploy em múltiplos computadores
