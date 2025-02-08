# Extração de bytes brutos de imagem com hash SHA-26
> Estudando criptografia
## Ideia
Extraimos os bytes brutos da imagem, geramos uma seed e com ela alimentamos o algoritmo HKDF para gerar bytes aleatórios e por fim concatenamos os bytes em um número inteiro aleatório em base 256.

## Calculando a entropia
> Fórmula de Shannon

$$ H(X) = -\sum_{i=1}^{n} p(x_i) \log_2 p(x_i) $$

Onde $$p(x_i)$$ é a probabilidade do pixel $$i$$
