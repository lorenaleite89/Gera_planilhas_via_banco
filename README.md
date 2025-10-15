# 🚀 GERADOR DE RELATÓRIO FISCAL - GUIA RÁPIDO

## ✨ CARACTERÍSTICAS

✅ **Executável standalone** - Funciona em qualquer Windows (com ou sem Python)  
✅ **Detecção automática do servidor** - Usa o nome do PC automaticamente  
✅ **Simples de configurar** - Apenas ajuste o nome do banco de dados  
✅ **Gera Excel automaticamente** - Salva na área de trabalho  

---

## ⚡ INÍCIO RÁPIDO

### PASSO 1: Configure o banco de dados
Abra `consulta_fiscal.py` e edite a linha 15:
```python
database = 'SEU_BANCO'  # ⬅️ Coloque o nome do seu banco aqui
```

### PASSO 2: Gere o executável
Execute o arquivo: `gerar_executavel.bat`

### PASSO 3: Use!
Execute `dist/Relatorio_Fiscal.exe` em qualquer PC Windows

---

## 📋 ARQUIVOS INCLUÍDOS

| Arquivo | Descrição |
|---------|-----------|
| `consulta_fiscal.py` | Código-fonte principal |
| `requirements.txt` | Dependências Python |
| `gerar_executavel.bat` | Script para gerar o .exe |
| `MANUAL.md` | Manual completo detalhado |
| `CONFIGURACAO.txt` | Guia de configuração rápida |
| `README.md` | Este arquivo |

---

## 🎯 COMO FUNCIONA

1. **Detecta o nome do PC** automaticamente (ex: "CAIXA01")
2. **Conecta ao SQL Server** local usando esse nome
3. **Executa 2 consultas SQL** (Regras Fiscais + Cadastro de Produtos)
4. **Gera arquivo Excel** com 2 abas na área de trabalho
5. **Nomeia automaticamente** como: `[Nome Loja] - [CNPJ].xlsx`

---

## ⚙️ REQUISITOS NO PC DE DESTINO

- Windows 7 ou superior
- SQL Server instalado localmente
- Driver ODBC do SQL Server ([Download aqui](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server))

---

## ❓ PRECISA DE AJUDA?

Consulte o **MANUAL.md** para:
- Instruções detalhadas
- Solução de problemas comuns
- Configurações avançadas
- Exemplos práticos

---

## 📝 EXEMPLO DE USO

```
PC: CAIXA01
Banco: VendasDB

Resultado da detecção automática:
✓ Servidor: CAIXA01
✓ Banco: VendasDB
✓ Conexão: CAIXA01\VendasDB
✓ Arquivo gerado: Loja Centro - 12.345.678-0001-99.xlsx
```

---

**Desenvolvido para simplificar a geração de relatórios fiscais** 💼
