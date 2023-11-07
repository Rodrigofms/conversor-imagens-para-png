# Modo de usar:

Para usar tem que se abrir o programa e o mesmo irá criar uma pasta e pedir para abri-lo novamente. Dentro da pasta se coloca as imagens que deseja converter e apenas abra o programa e ele fará a conversão automaticamente
<br>

# Informações:

Deixei disponível o arquivo em .exe caso queira ter o aplicativo funcionando localmente sem precisar compilar o codig. Tambem pode usar o código a vontade para compilar você mesmo.

## Como compilar:
<b>Antes de fazer isso, se certifique que tambem baixou a pasta assets e seu conteúdo e que tem o ```pyinstaller``` instalado.</b>
<br>
<br>
Para instalar o pyinstaller: ```pip install pyinstaller```
<br>
<br>
Abrir o cmd na pasta onde esta baixado o arquivo ```toPNG.py``` e digitar ```pyinstaller --name="Conversor de imagens" --onefile --icon=".\assets\favicon.ico" toPNG.py```. E assim você terá o executável dentro da pasta ```dist```
