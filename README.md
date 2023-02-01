# PyToneGen

### Descrição

Gerador de sons em Python, utilizando-se de ondas senóides. Baseado em PyGame.

### Funcionamento

Segue diagrama de funcionamento do exemplo "Melody.py" disponibilizado)

```mermaid

flowchart LR
  Melody.py --RNG--> Frequência & Duração ---> Audio
  
  subgraph PyToneGen
  id1["Função Seno"] --Numpy--> Array --PyGame--> SineWave
  end
  
  SineWave --> Audio --> Output
```

### Dependências

- pygame
- time
- math
- numpy
- time (Para o exemplo "Melody.py")
