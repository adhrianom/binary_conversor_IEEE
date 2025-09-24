# Conversor IEEE 754 (32 Bits)

Este projeto é uma ferramenta simples em Python para converter números decimais (incluindo negativos e fracionários) para a representação binária no padrão IEEE 754 de 32 bits (ponto flutuante).

## Funcionalidades

- Converte números decimais positivos e negativos para o formato IEEE 754
- Trata tanto a parte inteira quanto a parte fracionária
- Exibe os campos de sinal, expoente e mantissa

## Ferramentas Utilizadas

- **Python 3**: Linguagem principal do projeto
- **VS Code**: IDE recomendada para desenvolvimento
- **Módulo math**: Para operações matemáticas

## Como Usar

1. **Clone o repositório:**
   ```bash
   git clone git@github.com:SEU_USUARIO/NOME_DO_REPOSITORIO.git
   cd NOME_DO_REPOSITORIO/ieee
   ```

2. **Execute o conversor:**
   ```bash
   python3 ieee_conversor.py
   ```

3. **Digite um número** quando solicitado.  
   O programa irá mostrar a representação binária IEEE 754.

## Exemplo

```
Digite um número: 5.75
SIGNAL | EXPONENT | MANTISSA
0 10000001 01110000000000000000000
```

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../LICENSE) para mais detalhes.

---

## Possíveis erros

Resultados podem não ser precisos para valores extremos, como números muito pequenos (ex: 1E-38) ou muito grandes (ex: 1E10), devido a limitações de precisão do formato IEEE 754 de 32 bits.