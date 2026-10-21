# Pipeline de producción con IA

Todo el canal se produce con IA y casi todo dentro de ElevenLabs, que ya tienes conectado.
Tu trabajo humano se reduce a tres decisiones por vídeo: aprobar el ángulo, verificar los datos y elegir entre variantes.
Esas tres decisiones son las que YouTube busca para no considerar el canal "contenido inauténtico".

## Herramientas y modelos elegidos

| Paso | Herramienta | Modelo | Por qué este |
|---|---|---|---|
| Guion | Claude | El más reciente disponible | Mejor redacción en español y respeta la biblia del canal |
| Personaje en escenas | ElevenLabs, imagen | Nano Banana 2 con la hoja maestra conectada como referencia | Mantiene al personaje igual y cuesta un tercio que la versión Pro |
| Miniaturas | ElevenLabs, imagen | Nano Banana Pro con la hoja maestra como referencia | La miniatura decide los clics, ahí vale gastar más |
| Animación | ElevenLabs, vídeo | Kling 2.5 Turbo, imagen a vídeo de 5 segundos | Siete veces más barato que Seedance 2.5 con buen resultado en 2D |
| Voz | ElevenLabs, voz | Eleven v4 con la voz "Max - Calm & Friendly" | Acepta indicaciones de actuación como pausas y tono seco |
| Música | ElevenLabs, música | Eleven Music v2.5 con la opción "instrumental" activada en el nodo | Un tema propio sin problemas de derechos. Sin esa opción el modelo puede agregar voz aunque el prompt diga lo contrario |
| Efectos | ElevenLabs, efectos | Sound Effects v2 | Chirrido de frenos, caída de Clementina, viento |
| Montaje | CapCut o DaVinci Resolve | | Subtítulos automáticos, zooms y cortes |
| Doblaje al inglés | ElevenLabs, doblaje | Dubbing v2 | Misma voz y mismo vídeo, a partir del mes 4 |

## Costo estimado por vídeo de 9 minutos

Precios obtenidos de las estimaciones reales de tu cuenta de ElevenLabs en octubre de 2026.

| Concepto | Cantidad | Costo aproximado |
|---|---|---|
| Imágenes de escena con Nano Banana 2 | 35 escenas con 2 variantes cada una. Pide 2, no las 4 que salen por defecto | 8,40 USD |
| Clips animados con Kling 2.5 Turbo | 8 clips de 5 segundos | 3,40 USD |
| Voz completa | 9 minutos, 2 tomas | 3 USD |
| Miniatura con Nano Banana Pro | 4 variantes | 1,50 USD |
| Efectos de sonido | 5 a 10 efectos | 0,50 USD |
| **Total por vídeo** | | **unos 17 USD** |

Costo real del piloto: unos 12 USD por 5 minutos, con 17 escenas a 4 variantes y 8 clips. Las variantes extra fueron el gasto más grande.

A 2 vídeos largos por semana son unos 140 USD al mes en créditos.
Los Shorts salen recortados de los vídeos largos y no suman costo.
El tema musical del canal se genera una sola vez y se reutiliza.

**Por qué no animar todo el vídeo:** un vídeo de 9 minutos totalmente animado con IA costaría más de 300 USD. Los canales grandes de este nicho usan animación limitada: imágenes fijas con movimiento de cámara y solo algunos planos animados. Es lo que hace este pipeline.

## Paso a paso de un vídeo

### 1. Elegir el tema

Sale de la lista de títulos. Antes de escribir, busca el tema en YouTube y mira los tres vídeos más vistos. Anota qué ángulo no cubrieron. Ese es tu giro.

### 2. Escribir el guion con Claude

Usa este prompt, pegando antes la biblia del canal completa:

```
Eres el guionista del canal de YouTube "Tranqui". Arriba tienes la biblia del canal.
Escribe el guion de "¿Qué pasaría si [TEMA]?" siguiendo exactamente la estructura de 7 partes.
Duración: 8 a 9 minutos, unas 1.700 palabras de narración.
Español latino neutro, tratamiento de "tú", sin regionalismos.
Escribe para curiosos de 12 años en adelante: nunca un tono infantil.
Incluye 3 caídas de Clementina en los momentos más fuertes.
Incluye al menos una comparación con algo cotidiano en cada bloque.
Para cada escena escribe "Visual:" con lo que se ve y "Voz:" con la narración.
Usa indicaciones de actuación en inglés entre corchetes: [short pause], [long pause], [deadpan].
Escribe los números en palabras para que la voz los lea bien.
Al final agrega una tabla con cada dato numérico y una fuente confiable para verificarlo.
El ángulo que no cubren otros vídeos es: [TU GIRO].
```

Después revisa tú tres cosas: que cada dato de la tabla coincida con su fuente, que haya al menos un chiste que te haga gracia de verdad, y que no suene a lista de datos.

### 3. Generar la voz

En ElevenLabs genera la narración por escenas, no todo junto. Así puedes rehacer una sola escena si una frase sale mal.
Modelo Eleven v4, voz "Max - Calm & Friendly". Escucha cada toma y quédate con la mejor.

### 4. Generar las imágenes de escena

En el lienzo "Canal Qué pasaría si - Personajes" de ElevenLabs está el nodo "Tranqui - hoja maestra". Conéctalo siempre como referencia.
Plantilla de prompt para cada escena:

```
Animation keyframe, 16:9, flat 2D vector cartoon, thick dark outlines, no gradients.
Use the exact capybara character from the reference sheet: same chubby caramel-brown body,
half-closed relaxed eyes, small orange tangerine on its head, blue scarf, small backpack.
Scene: [DESCRIPCIÓN DE LA ESCENA EN INGLÉS].
Palette: caramel, orange, sky blue, cream, plus the colors the scene needs.
Leave empty space on the [left/right] for on-screen text. Kids TV quality, no text.
```

Si una escena no lleva a Tranqui, igual mantén el estilo: "flat 2D vector cartoon, thick dark outlines, no gradients".

### 5. Animar los planos clave

Elige los 8 planos más importantes: el gancho, cada caída de Clementina y el cierre.
Conecta la imagen como primer fotograma en Kling 2.5 Turbo con este prompt base:

```
Use the connected image as the first frame. Flat 2D cartoon animation, keep the exact art style,
outlines and colors. [ACCIÓN CONCRETA Y LENTA]. Static camera, no cuts, calm smooth motion.
```

Las acciones simples funcionan mejor: tomar un sorbo, parpadear, una mandarina que cae, agua que se mueve.

No pongas flechas, textos ni gráficos dentro de una imagen que vas a animar. En la prueba del piloto la flecha de rotación desapareció a mitad del clip. Esos elementos se agregan después, en el montaje.

### 6. Montar

En CapCut o DaVinci Resolve:

- Pon la voz completa en la línea de tiempo y coloca cada imagen bajo su frase.
- A las imágenes fijas aplica un zoom lento o un desplazamiento suave. Nunca dejes una imagen quieta más de 4 segundos.
- Agrega el tema musical bajito, entre el 10 % y el 15 % del volumen de la voz.
- Agrega los efectos de sonido en los momentos cómicos.
- Agrega el contador de Clementinas en la esquina superior derecha.
- Genera subtítulos automáticos y revísalos.

### 7. Miniatura y título

Genera 4 miniaturas con Nano Banana Pro. Reglas: la cara de Tranqui grande, una catástrofe clara, máximo cuatro palabras de texto.
Sube el vídeo con la mejor y activa "Probar y comparar" en YouTube Studio con la segunda.

### 8. Shorts

De cada vídeo largo corta 3 Shorts verticales de 30 a 50 segundos. Los mejores momentos suelen ser el gancho, el dato más loco y el giro final.
Cada Short termina con Tranqui diciendo la pregunta del vídeo largo.

### 9. Publicar

- Marca el vídeo como "No, no es para niños".
- En "Contenido alterado o sintético" responde "No": el contenido es animación evidente, no imagen realista. YouTube solo exige la etiqueta para contenido que parezca real.
- Descripción: un párrafo, las fuentes de la tabla de datos y el enlace al vídeo siguiente.

## Lo que todavía no está automatizado

- **Montaje.** El piloto se armó de forma automática con los scripts de la carpeta `herramientas`, sin editor. Hacen zooms lentos sobre las imágenes, intercalan los clips, mezclan voz, música y efectos, y agregan los textos. Para cada vídeo nuevo hay que cambiar en los scripts la lista de escenas, los tiempos y los textos. Con CapCut sigue siendo más fácil ajustar a mano, sobre todo los subtítulos.
- **Verificación de datos.** No se automatiza a propósito. Es tu valor añadido y tu seguro contra la desmonetización.
