# YOLO

Este diretório contém scripts de exemplo para trabalhar com o YOLOv8 da Ultralytics em Python.

## Estrutura

- `split.py` - divide um conjunto de imagens em `train`, `val` e `test`, copiando cada classe para a nova estrutura de pastas.
- `yolo-cls.py` - treina um modelo de classificação YOLOv8 usando os dados já preparados na pasta `splited`.
- `ml.py` - exemplo simples de inferência com um modelo YOLOv8 pré-treinado.

## Requisitos

Instale as dependências necessárias:

```bash
pip install ultralytics scikit-learn
```

Também é recomendado ter o Python 3.8+ e, caso use GPU, a versão adequada do PyTorch/CUDA.

## Uso

### 1. Preparar os dados

Coloque as imagens em uma estrutura de pastas por classe dentro de `db`:

```
db/
  classe1/
    imagem1.jpg
    imagem2.jpg
  classe2/
    imagem3.jpg
```

Execute o script para criar a divisão de conjuntos:

```bash
python split.py
```

O resultado será copiado para `splited/train`, `splited/val` e `splited/test`.

### 2. Treinar o classificador YOLOv8

Execute o treinamento usando `yolo-cls.py`:

```bash
python yolo-cls.py
```

O script carrega o modelo `yolov8n-cls.pt` e inicia o treinamento com os dados em `splited`.

### 3. Fazer inferência

Use `ml.py` para rodar um exemplo de inferência sobre uma imagem:

```bash
python ml.py
```

O script carrega o modelo `yolov8n.pt` e executa a detecção na imagem especificada.

## Observações

- `split.py` usa `shutil.copy2`, portanto não move os arquivos originais.
- Ajuste `PASTA_ORIGEM`, `PASTA_DESTINO` e as proporções de divisão no `split.py` conforme necessário.
- Substitua os nomes dos modelos e imagens para o seu próprio caso de uso.
