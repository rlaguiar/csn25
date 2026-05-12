from ultralytics import YOLO

# Carrega um modelo pré-treinado 
# (yolov8n.pt é o modelo "nano", o menor e mais rápido)
model = YOLO('yolov8n.pt')

# Executa a inferência em uma imagem
# Você pode usar 'source=0' para usar a webcam em tempo real
# results = model('toddynatal.jpg') 
results = model('toddyfrio.jpg') 

# Processa e exibe os resultados
for r in results:
    # O método .show() abre uma janela com as detecções
    r.show() 

    # Você também pode acessar os boxes (caixas delimitadoras)
    print(r.boxes)