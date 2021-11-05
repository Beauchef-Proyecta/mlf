# mlf - Repositorio a utilizar por curso CD2201

## Cómo conectarse vía remota al robot a través de Ngrok
- Entrar a ngrok https://ngrok.com/
- Ingresar (login) credenciales de cada grupo cc2201mlf+<project group>@gmail.com ; ngrok pass
- Ir a Endpoints->Status, donde se encontrarán las opciones de conexión (TCP para ssh, HTTP para ver stream de la cámara)
- Si el stream está corriendo basta con entrar a la dirección HTTP para ver la imagen captada por la cámara del robot
### Conexión al robot vía SSH con Ngrok
- Si tienes Windows, instalar mobaxterm en https://mobaxterm.mobatek.net/
- Para conectarse debes tener la dirección de Ngrok
  ``` tcp://<dir>:<port> ```
  
### Correr ssh en terminal (mobaxterm para Windows)
```
ssh pi@dir -p <port>
```
Ahora tendrás una terminal dentro del robot y tendrás acceso a este repositorio
  
## Mover el robot

- Activar el ambiente virtual ```workon mlf```
- Ir al directorio del repositorio ```cd mlf/```
- Correr algún test de la carpeta ```test/``` (ej:```python test/test_IK.py```)
- Ver el robot a través del stream c:
