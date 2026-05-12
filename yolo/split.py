import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

# --- CONFIGURAÇÕES ---
PASTA_ORIGEM = "db"                 # Onde estão suas pastas de classes hoje
PASTA_DESTINO = "splited"           # Onde a nova estrutura será criada
RATIO_TRAIN = 0.75                  # 75% Treino
RATIO_VAL = 0.15                    # 15% Validação
RATIO_TEST = 0.10                   # 10% Teste
SEED = 159                          # Semente para garantir que o sorteio seja reproduzível

def split_and_move():
    # 1. Mapear todas as imagens
    origem_path = Path(PASTA_ORIGEM)
    files_data = []
    
    # Varre as pastas das classes
    classes = [d for d in origem_path.iterdir() if d.is_dir()]
    
    print(f"🔍 Lendo arquivos de {len(classes)} classes...")
    
    for class_dir in classes:
        # Pega arquivos (jpg, png, jpeg, etc)
        for file_path in class_dir.glob('*.*'): 
            if file_path.is_file():
                # Guarda o caminho completo e o nome da classe
                files_data.append({
                    'path': file_path,
                    'class': class_dir.name
                })

    print(f"Total de imagens encontradas: {len(files_data)}")

    # Se não tiver arquivos, para
    if not files_data:
        print("❌ Nenhum arquivo encontrado. Verifique o caminho.")
        return

    # Separar apenas as labels e caminhos para o sklearn
    X = [x['path'] for x in files_data]
    y = [x['class'] for x in files_data]

    # 2. Primeira Divisão: Treino vs (Validação + Teste)
    # O 'stratify=y' garante o balanceamento das classes
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, 
        train_size=RATIO_TRAIN, 
        stratify=y, 
        random_state=SEED
    )

    # 3. Segunda Divisão: Validação vs Teste
    # Calculamos a proporção relativa. Se sobrou 20% e queremos 10%/10%, dividimos ao meio (0.5)
    ratio_remaining = RATIO_TEST / (RATIO_VAL + RATIO_TEST)
    
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, 
        test_size=ratio_remaining, 
        stratify=y_temp, 
        random_state=SEED
    )

    print(f"📝 Divisão calculada:")
    print(f" - Treino: {len(X_train)} imagens")
    print(f" - Validação: {len(X_val)} imagens")
    print(f" - Teste: {len(X_test)} imagens")

    # 4. Função para mover/copiar os arquivos
    def processar_arquivos(arquivos, labels, tipo_split):
        dest_root = Path(PASTA_DESTINO) / tipo_split
        
        for file_path, label in zip(arquivos, labels):
            # Cria: dataset_final/train/gato/
            dest_dir = dest_root / label
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            # Define o destino final
            dest_file = dest_dir / file_path.name
            
            # AÇÃO: Copiar (seguro) ou Mover (destrutivo)
            shutil.copy2(file_path, dest_file) # Use shutil.move() se quiser recortar
            
    print("🚀 Copiando arquivos...")
    processar_arquivos(X_train, y_train, 'train')
    processar_arquivos(X_val, y_val, 'val')
    processar_arquivos(X_test, y_test, 'test')
    
    print("✅ Concluído com sucesso!")

if __name__ == "__main__":
    # Instale o sklearn se não tiver: pip install scikit-learn
    split_and_move()