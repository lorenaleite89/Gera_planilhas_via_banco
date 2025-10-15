@echo off
echo ============================================
echo GERADOR DE EXECUTAVEL - RELATORIO FISCAL
echo ============================================
echo.
echo Verificando versao do Python...
python --version
echo.

echo ============================================
echo METODO 1: Instalacao com versoes flexiveis
echo ============================================
echo.

echo Instalando dependencias (pode levar alguns minutos)...
echo.

REM Tenta instalar com o arquivo simples primeiro
pip install --upgrade pip
pip install pyodbc
pip install openpyxl
pip install pyinstaller
pip install pandas

echo.
echo ============================================
echo Verificando instalacoes...
echo ============================================
python -c "import pyodbc; print('pyodbc: OK')"
python -c "import pandas; print('pandas: OK')"
python -c "import openpyxl; print('openpyxl: OK')"
python -c "import PyInstaller; print('pyinstaller: OK')"
echo.

echo ============================================
echo Gerando executavel...
echo ============================================
echo Isso pode levar alguns minutos...
echo.

pyinstaller --onefile --console --icon=NONE --name="Relatorio_Fiscal" consulta_fiscal.py

if %errorlevel% neq 0 (
    echo.
    echo ============================================
    echo ERRO ao gerar executavel!
    echo ============================================
    echo.
    echo Tente executar manualmente:
    echo pyinstaller --onefile --console --name="Relatorio_Fiscal" consulta_fiscal.py
    echo.
    pause
    exit /b 1
)

echo.
echo Limpando arquivos temporarios...
if exist build rmdir /s /q build
if exist Relatorio_Fiscal.spec del /q Relatorio_Fiscal.spec
if exist __pycache__ rmdir /s /q __pycache__
echo.

echo ============================================
echo CONCLUIDO COM SUCESSO!
echo ============================================
echo.
echo O executavel foi criado em: dist\Relatorio_Fiscal.exe
echo.
echo Tamanho aproximado: 50-100 MB
echo Funciona em qualquer Windows (com ou sem Python)
echo.
pause
