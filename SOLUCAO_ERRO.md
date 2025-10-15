# SOLUÇÃO PARA ERRO DE COMPILAÇÃO - Python 3.13

## ❌ ERRO ENCONTRADO:
```
Unknown compiler(s): [['icl'], ['cl'], ['cc'], ['gcc'], ['clang'], ['clang-cl'], ['pgcc']]
```

Este erro ocorre porque o **pandas** precisa compilar código C e não encontrou um compilador instalado no Windows.

---

## ✅ SOLUÇÕES (em ordem de facilidade):

### SOLUÇÃO 1: Use o script alternativo (RECOMENDADO)
Execute o arquivo: `gerar_executavel_v2.bat`

Este script instala as bibliotecas de forma diferente, permitindo que o pip baixe versões pré-compiladas.

---

### SOLUÇÃO 2: Instale Microsoft C++ Build Tools

1. **Baixe** o instalador:
   https://visualstudio.microsoft.com/visual-cpp-build-tools/

2. **Execute** o instalador

3. **Selecione**:
   - "Desenvolvimento para desktop com C++"
   - Certifique-se que está marcado: "MSVC v143" e "Windows 10 SDK"

4. **Instale** (pode levar 20-30 minutos)

5. **Reinicie** o computador

6. **Execute** novamente o `gerar_executavel.bat`

---

### SOLUÇÃO 3: Use versões pré-compiladas (MAIS FÁCIL)

Execute os seguintes comandos **um de cada vez** no CMD:

```cmd
pip install --upgrade pip
pip install pyodbc
pip install openpyxl  
pip install pyinstaller
pip install pandas
```

O pip vai baixar versões **pré-compiladas** (wheels) que não precisam de compilador.

Depois execute:
```cmd
pyinstaller --onefile --console --name="Relatorio_Fiscal" consulta_fiscal.py
```

---

### SOLUÇÃO 4: Downgrade do Python (se nada funcionar)

Se você instalou Python 3.13 muito recentemente, algumas bibliotecas podem não ter versões pré-compiladas ainda.

**Opção A**: Instale Python 3.11 ou 3.12 (versões mais estáveis)
- Baixe em: https://www.python.org/downloads/
- Escolha Python 3.11.x ou 3.12.x
- Marque "Add Python to PATH" durante instalação

**Opção B**: Use o Python que já está instalado, mas instale um por um:
```cmd
pip install --only-binary :all: pandas
pip install pyodbc openpyxl pyinstaller
```

---

## 🎯 QUAL SOLUÇÃO USAR?

| Situação | Solução Recomendada |
|----------|---------------------|
| Quer rapidez | SOLUÇÃO 1 ou 3 |
| Vai desenvolver mais | SOLUÇÃO 2 |
| Tem pouco espaço em disco | SOLUÇÃO 3 |
| Nada funcionou | SOLUÇÃO 4 |

---

## 📝 TESTE SE FUNCIONOU

Após tentar qualquer solução, teste com:

```cmd
python -c "import pandas; print('Pandas OK')"
python -c "import pyodbc; print('PyODBC OK')"
python -c "import openpyxl; print('OpenPyXL OK')"
```

Se todos imprimirem "OK", você pode gerar o executável!

---

## 💡 POR QUE ESTE ERRO ACONTECE?

- **Python 3.13** é muito novo (lançado em outubro de 2024)
- Algumas bibliotecas ainda não têm versões pré-compiladas para 3.13
- O pip tenta compilar do código-fonte
- Windows não tem compilador C instalado por padrão
- Linux/Mac têm compiladores nativos, Windows não

**BOA NOTÍCIA**: As soluções acima resolvem isso! 😊
