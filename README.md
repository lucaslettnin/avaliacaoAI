Este repositório apresenta um projeto simples de visão computacional que adapta códigos de monitoramento e rastreamento de pessoas para um contexto de análise de vídeo. A ideia principal é detectar e acompanhar indivíduos em um fluxo de vídeo utilizando métodos clássicos de visão computacional (sem a necessidade de modelos complexos de aprendizado de máquina).

Objetivo
O objetivo do projeto é demonstrar como:
Iniciar com códigos básicos de detecção ou rastreamento de objetos (neste caso, pessoas).
Adaptar tais códigos para um problema específico de visão computacional, como monitoramento de pessoas em uma área, análise de movimento ou contagem de indivíduos.
Utilizar apenas técnicas de visão computacional clássica (ex: HOG+SVM para detecção de pedestres, segmentação de cores, análise de contornos, ou Haar Cascades) sem recorrer a modelos de linguagem ou deep learning.
Não depende de modelos complexos pré-treinados de deep learning e não faz uso de modelos de linguagem (LLM). Ele se baseia em métodos clássicos de análise de imagem e vídeo fornecidos pelo OpenCV.

Bibliotecas : pip install -r requirements.txt
Arquivos em Python que carregam um vídeo, processam cada frame usando técnicas de visão computacional e detectam pessoas na cena.

Exemplo de funcionalidades:
Detecção de pedestres usando o descritor HOG e SVM padrão do OpenCV.
Segmentação por cor ou contornos para isolar objetos em movimento.
Exibição do resultado em tempo real, mostrando os retângulos de detecção ao redor das pessoas.
