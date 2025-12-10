import pyodbc
import pandas as pd
from pathlib import Path
import os
import sys
from datetime import datetime

def conectar_banco():
    """
    Estabelece conexão com o banco de dados SQL Server.
    Detecta automaticamente o nome do computador como servidor.
    """
    try:
        # Detecta automaticamente o nome do computador
        server = os.environ.get('COMPUTERNAME', 'localhost')
        
        # CONFIGURAÇÃO DO BANCO - AJUSTE APENAS ESTAS LINHAS
        database = 'MISTERCHEFNET'   # Nome do banco de dados
        
        # Para autenticação SQL Server (opcional)
        username = 'sa' 
        password = 'MISTERCHEFNET'
        
        print(f"Tentando conectar ao servidor: {server}")
        print(f"Banco de dados: {database}")

        # Opção 1: Autenticação SQL Server
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
          
        # Opção 2: Autenticação do Windows
        # connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
      
        conn = pyodbc.connect(connection_string)
        print("✓ Conexão estabelecida com sucesso!")
        return conn
    
    except Exception as e:
        print(f"✗ Erro ao conectar ao banco de dados: {e}")
        print(f"\nDetalhes da conexão:")
        print(f"  - Servidor detectado: {server}")
        print(f"  - Banco de dados: {database}")
        print(f"\nVerifique se:")
        print("  1. O SQL Server está instalado e em execução")
        print("  2. O nome do banco de dados está correto")
        print("  3. O driver ODBC do SQL Server está instalado")
        input("\nPressione Enter para sair...")
        sys.exit(1)

def executar_consulta(conn, sql_query, nome_consulta):
    """
    Executa uma consulta SQL e retorna um DataFrame.
    """
    try:
        print(f"Executando consulta: {nome_consulta}...")
        df = pd.read_sql(sql_query, conn)
        print(f"✓ {nome_consulta} executada com sucesso! ({len(df)} registros)")
        return df
    
    except Exception as e:
        print(f"✗ Erro ao executar {nome_consulta}: {e}")
        return None

def obter_nome_arquivo(df_regras):
    """
    Obtém o nome da loja e CNPJ para nomear o arquivo.
    Remove pontos e traços do CNPJ.
    """
    try:
        if not df_regras.empty:
            nome_loja = str(df_regras['nome loja'].iloc[0]).strip()
            cnpj = str(df_regras['cnpj'].iloc[0]).strip()
            
            # Remove pontos, traços e barras do CNPJ
            cnpj_limpo = cnpj.replace('.', '').replace('-', '').replace('/', '')
            
            return f"{nome_loja} - {cnpj_limpo}.xlsx"
        else:
            return f"Relatorio_Fiscal_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    except:
        return f"Relatorio_Fiscal_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

def salvar_excel(df_regras, df_produtos, nome_arquivo):
    """
    Salva os DataFrames em um arquivo Excel no diretório C:/.
    """
    try:
        # Define o caminho como C:/
        diretorio = Path("C:/MHI/")
        caminho_completo = diretorio / nome_arquivo
        
        # Cria o arquivo Excel com múltiplas abas
        print(f"Salvando arquivo: {nome_arquivo}...")
        with pd.ExcelWriter(caminho_completo, engine='openpyxl') as writer:
            df_regras.to_excel(writer, sheet_name='REGRAS FISCAIS', index=False)
            df_produtos.to_excel(writer, sheet_name='CADASTRO DE PRODUTOS', index=False)
        
        print(f"✓ Arquivo salvo com sucesso em: {caminho_completo}")
        return True
    
    except Exception as e:
        print(f"✗ Erro ao salvar arquivo Excel: {e}")
        return False

def main():
    """
    Função principal do programa.
    """
    print("="*60)
    print("GERADOR DE RELATÓRIO FISCAL")
    print("="*60)
    print()
    
    # SQL Query 1 - REGRAS FISCAIS
    sql_query_1 = """

SELECT DISTINCT 
    l.Estado AS UF,
    l.[Código Loja], 
    l.[nome loja], 
    l.cnpj,
    e.cod_ncm, 
    e.cod_cest,
    l.crt AS regimetributario, 
    e.Tributo, 
    e.Imposto,
    LTRIM(RTRIM(ISNULL(e.[CodigoBeneficioFiscal], ''))) AS beneficiofiscal,
    e.cfop_venda, 
    e.cst_csosn_venda,
    ISNULL(e.PER_REDUCAO_BC_ICMS, 0) AS reducaoicms,
    ISNULL(e.PercentualFCP, 0) AS PercentualFCP,
    ISNULL(e.ReducaoIcmsEfetivo, 0) AS ReducaoIcmsEfetivo,
    ISNULL(e.AliquotaIcmsEfetivo, 0) AS AliquotaIcmsEfetivo,
    e.cst_pis, 
    e.pis,
    'PERCENTUAL' AS COFINS_tipo_Calculo, 
    e.cst_cofins, 
    e.COFINS, 
    'PERCENTUAL' AS COFINS_Tipo_Calculo 
FROM estoque e 
INNER JOIN (
    SELECT * 
    FROM lojas 
    WHERE [Código Loja] = (SELECT DISTINCT loja FROM estoque)
) l ON e.loja = l.[código loja]
WHERE (desativado = 0 or desativado is null) 
    AND cfop_venda <> '''' 
    AND [Nao Vendavel] = 0 
    AND [Não Exibir no Cardápio] = 0
    AND grupo NOT in ('ALIMENTO FUNCIONARIOS',
'DESCARTAVEIS',
'DESCARTAVEL',
'EMBALAGEM',
'EMBALAGENS',
'EMBALAGENS E DESCARTAVEIS',
'DESCARTAVEIS',
'EQUIPAMENTOS',
'ESTOQUE',
'ESTOQUE INSUMOS',
'HIGIENE E LIMPEZA',
'IMOBILIZADO',
'INSUMOS',
'LIMPEZA',
'MATERIA PRIMA',
'MATERIAL DE EXPEDIENTE',
'MATERIAL DE LIMPEZA',
'MATERIAL DE USO',
'MATERIAL DE USO E CONSUMO',
'MATERIAL EMBALAGEM',
'MATERIAL SECUNDARIO',
'PROCESSADOS',
'PROCESSOS',
'PRODUCOES',
'SUBPRODUTO',
'UNIFORME FUNCIONARIOS',
'UNIFORME',
'USO E CONSUMO',
'UTENSILIOS',
'MAQUINAS E EQUIPAMENTOS',
'FICHA TECNICA',
'MATERIAIS DE EXPEDIENTE',
'MATERIAIS DE LIMPEZA',
'MATERIAIS DE USO',
'MATERIAIS DE USO E CONSUMO')

AND SUBGRUPO NOT IN ('ALIMENTO FUNCIONARIOS',
'EQUIPAMENTOS',
'ESTOQUE',
'ESTOQUE INSUMOS',
'HIGIENE E LIMPEZA',
'IMOBILIZADO',
'INSUMO',
'INSUMOS',
'LIMPEZA',
'MATERIA PRIMA',
'MATERIAL DE EXPEDIENTE',
'MATERIAL DE LIMPEZA',
'MATERIAL DE USO',
'MATERIAL DE USO E CONSUMO',
'MATERIAL EMBALAGEM',
'MATERIAL SECUNDARIO',
'PROCESSADOS',
'PROCESSOS',
'PRODUCOES',
'SUBPRODUTO',
'UNIFORME FUNCIONARIOS',
'UNIFORME',
'USO E CONSUMO',
'MAQUINAS E EQUIPAMENTOS',
'FICHA TECNICA',
'MATERIAIS DE EXPEDIENTE',
'MATERIAIS DE LIMPEZA',
'MATERIAIS DE USO',
'MATERIAIS DE USO E CONSUMO')

ORDER BY e.cod_ncm, cod_cest

"""
    
    # SQL Query 2 - CADASTRO DE PRODUTOS
    sql_query_2 = """

SELECT DISTINCT 
    l.Estado AS UF, 
    l.[Código Loja],
    l.[nome loja], 
    l.cnpj,
    e.[Código Produto],
    e.Subgrupo,
    e.[nome produto],
    e.[Preço venda],
    e.cod_ncm, 
    e.cod_cest,
    l.crt AS regimetributario, 
    e.Tributo, 
    e.Imposto,
    LTRIM(RTRIM(ISNULL(e.[CodigoBeneficioFiscal], ''))) AS beneficiofiscal,
    e.cfop_venda, 
    e.cst_csosn_venda,
    ISNULL(e.PER_REDUCAO_BC_ICMS, 0) AS reducaoicms,
    ISNULL(e.PercentualFCP, 0) AS PercentualFCP,
    ISNULL(e.ReducaoIcmsEfetivo, 0) AS ReducaoIcmsEfetivo,
    ISNULL(e.AliquotaIcmsEfetivo, 0) AS AliquotaIcmsEfetivo,
    e.cst_pis, 
    e.pis,
    'PERCENTUAL' AS COFINS_tipo_Calculo, 
    e.cst_cofins, 
    e.COFINS, 
    'PERCENTUAL' AS COFINS_Tipo_Calculo 
FROM estoque e 
INNER JOIN (
    SELECT * 
    FROM lojas 
    WHERE [Código Loja] = (SELECT DISTINCT loja FROM estoque)
) l ON e.loja = l.[código loja]
WHERE (desativado = 0 or desativado is null)
    AND cfop_venda <> '''' 
    AND [Nao Vendavel] = 0 
    AND [Não Exibir no Cardápio] = 0
    AND grupo NOT in ('ALIMENTO FUNCIONARIOS',
'DESCARTAVEIS',
'DESCARTAVEL',
'EMBALAGEM',
'EMBALAGENS',
'EMBALAGENS E DESCARTAVEIS',
'DESCARTAVEIS',
'EQUIPAMENTOS',
'ESTOQUE',
'ESTOQUE INSUMOS',
'EPI',
'HIGIENE E LIMPEZA',
'IMOBILIZADO',
'INSUMO',
'INSUMOS',
'LIMPEZA',
'MATERIA PRIMA',
'MATERIAL DE EXPEDIENTE',
'MATERIAL DE LIMPEZA',
'MATERIAL DE USO',
'MATERIAL DE USO E CONSUMO',
'MATERIAL EMBALAGEM',
'MATERIAL SECUNDARIO',
'PROCESSADOS',
'PROCESSOS',
'PRODUCOES',
'SUBPRODUTO',
'UNIFORME FUNCIONARIOS',
'UNIFORME',
'USO E CONSUMO',
'UTENSILIOS',
'MAQUINAS E EQUIPAMENTOS',
'FICHA TECNICA',
'MATERIAIS DE EXPEDIENTE',
'MATERIAIS DE LIMPEZA',
'MATERIAIS DE USO',
'MATERIAIS DE USO E CONSUMO')

AND SUBGRUPO NOT IN ('ALIMENTO FUNCIONARIOS',
'EQUIPAMENTOS',
'ESTOQUE',
'ESTOQUE INSUMOS',
'HIGIENE E LIMPEZA',
'IMOBILIZADO',
'INSUMO',
'INSUMOS',
'LIMPEZA',
'MATERIA PRIMA',
'MATERIAL DE EXPEDIENTE',
'MATERIAL DE LIMPEZA',
'MATERIAL DE USO',
'MATERIAL DE USO E CONSUMO',
'MATERIAL EMBALAGEM',
'MATERIAL SECUNDARIO',
'PROCESSADOS',
'PROCESSOS',
'PRODUCOES',
'SUBPRODUTO',
'UNIFORME FUNCIONARIOS',
'UNIFORME',
'USO E CONSUMO',
'MAQUINAS E EQUIPAMENTOS',
'FICHA TECNICA',
'MATERIAIS DE EXPEDIENTE',
'MATERIAIS DE LIMPEZA',
'MATERIAIS DE USO',
'MATERIAIS DE USO E CONSUMO')

ORDER BY e.subgrupo, e.[nome produto],e.cod_ncm, cod_cest


"""
    
    # Conecta ao banco
    conn = conectar_banco()
    
    # Executa as consultas
    df_regras = executar_consulta(conn, sql_query_1, "SELECT 1 - REGRAS FISCAIS")
    df_produtos = executar_consulta(conn, sql_query_2, "SELECT 2 - CADASTRO DE PRODUTOS")
    
    # Verifica se as consultas foram bem-sucedidas
    if df_regras is None or df_produtos is None:
        print("\n✗ Erro: Uma ou mais consultas falharam.")
        conn.close()
        input("Pressione Enter para sair...")
        sys.exit(1)
    
    if df_regras.empty or df_produtos.empty:
        print("\n⚠ Aviso: Uma ou mais consultas não retornaram dados.")
    
    # Obtém o nome do arquivo
    nome_arquivo = obter_nome_arquivo(df_regras)
    
    # Salva o arquivo Excel
    sucesso = salvar_excel(df_regras, df_produtos, nome_arquivo)
    
    # Fecha a conexão
    conn.close()
    print("\n✓ Conexão com banco de dados encerrada.")
    
    if sucesso:
        print("\n" + "="*60)
        print("PROCESSO CONCLUÍDO COM SUCESSO!")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("PROCESSO FINALIZADO COM ERROS")
        print("="*60)
    
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()

