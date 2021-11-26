# Tools
En esta carpeta encontrarás distintos módulos con herramientas para utilizar directamente con el robot.
## Gcode to XYZ on robot
- ```gcode_to_IK.py``` permite invocar un archivo tipo .gcode con posiciones XYZ que son logradas mediante la cinematica inversa del robot
- Debes entregar el archivo como argumento ej: ```python gcode_to_IK.py test_gcode.gcode```
## Jog robot with command line
- ```manual_jogging.py``` permite mover con la consola, con opciones de usar con angulos (ang, q0,q1,q2)  o posiciones XYZ
- ```python manual_jogging.py```
