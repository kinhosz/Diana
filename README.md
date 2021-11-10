# Diana
## Um Bot que gerencia chats no Google Meet

Este projeto foi realizado para obter informações de reuniões no google Meet.  

## Dependências
Você precisa instalar o Selenium via pip
```sh
pip install selenium
```

No arquivo `data.json` adicione a versão do seu google Chrome na área designada. Apenas informe os dois primeiros dígios:
ex.: `95.0.4638.69` adicione apenas `95`.

Para encontrar a versão do google chrome, abra o navegador e vá em: `configurações > sobre o google chrome`.

## Modo de uso

Edite o arquivo ```data.json``` e substitua os valores ```code```, ```email``` e ```password``` pelo código da sala meet, email utilizado para acessar e a senha deste email respectivamente. Não compartilhe este software com sua senha exposta no ```data.json```. Seja cuidadoso.

## Como rodar

No prompt de comando digite
```python Diana.py```
Ou com double click (talvez funcione)

## Observações

Não precisa interagir, o software já fará tudo para você. Evite erros. Interaja apenas depois de 3 min de funcionamento, ou interaja fechando a janela se preferir.
Caso o software apresente alguma falha, apenas reinicie (confia).

## Tá, mas o que ele vai fazer?

O software nota um padrão nas mensagens enviadas pelos presentes na reunião e replica. Ele não replica periodicamente (não floda), o delay é de 5 minutos por envio.

## Considerações finais

Use esse software com cuidado. E contribua. Tmj s2.