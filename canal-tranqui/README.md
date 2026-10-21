# Tranqui: canal de YouTube animado hecho con IA

> Preguntas locas, respuestas tranquilas.

Un carpincho llamado Tranqui responde preguntas de "¿Qué pasaría si...?" sobre ciencia sin perder nunca la calma.
Canal en español latino neutro, para curiosos de 12 años en adelante, producido de punta a punta con IA.

## Qué hay en esta carpeta

| Archivo | Qué contiene |
|---|---|
| `01-biblia-del-canal.md` | Personaje, personalidad, paleta, estructura de cada vídeo y reglas de calidad |
| `02-titulos-y-calendario.md` | Los 10 primeros títulos, el calendario de 90 días y las metas |
| `03-guion-piloto.md` | Guion completo del primer vídeo con la tabla de datos verificables |
| `04-pipeline-de-produccion.md` | Herramientas, prompts, costos y el paso a paso de cada vídeo |
| `assets/` | Hoja maestra del personaje, avatar, banner, miniatura, fotograma, clip animado, voz y música |
| `piloto/` | **El primer vídeo terminado**, más las escenas, clips y voces usadas para armarlo |
| `herramientas/` | Scripts de ffmpeg que arman el vídeo automáticamente a partir de imágenes, clips y voces |

## Assets generados

| Archivo | Uso |
|---|---|
| `assets/tranqui-hoja-maestra.png` | Referencia oficial del personaje. Se conecta en cada generación de imagen |
| `assets/avatar-canal.png` | Foto de perfil del canal |
| `assets/banner-canal.png` | Banner del canal |
| `assets/miniatura-piloto.png` | Miniatura del piloto |
| `assets/fotograma-cierre-piloto.png` | Escena final del piloto |
| `assets/clip-cierre-piloto.mp4` | Prueba de animación de 5 segundos del cierre |
| `assets/voz-apertura-piloto-toma1.mp3` y `toma2` | Apertura del piloto narrada con la voz del canal |
| `assets/tema-musical-opcion1.mp3` a `opcion3` | Tres opciones de música de fondo. Escúchalas y quédate con una |

Todo está también en el lienzo de ElevenLabs llamado "Canal Qué pasaría si - Personajes", donde se puede seguir generando.

## El piloto

`piloto/piloto-tierra-deja-de-girar.mp4` es el primer vídeo completo, listo para revisar.

| Dato | Valor |
|---|---|
| Duración | 5 min 10 s |
| Resolución | 1280×720 |
| Volumen | -15 LUFS, el estándar de YouTube |
| Imágenes de escena | 17 |
| Planos animados | 8 |
| Costo en créditos | unos 12 USD |

Incluye voz, música, efectos, textos con los datos y el contador de Clementinas.

## Pendiente antes de publicar

- **Duración.** El guion dio 5 minutos con esta voz, no los 8 a 9 previstos. Con menos de 8 minutos YouTube no permite anuncios a mitad del vídeo. Los próximos guiones deben tener unas 1.700 palabras.
- **Música.** El piloto usa la opción 1. Escucha las tres y cámbiala si alguna te gusta más o si trae voz.
- **Subtítulos.** No están grabados en el vídeo. Activa los automáticos de YouTube en español y revísalos.
- **Escucha completa.** Revisa que la voz pronuncie bien números y nombres antes de subirlo.

## Próximos pasos

1. Crear el canal de YouTube "Tranqui" y reservar el identificador @tranqui o el más parecido disponible.
2. Subir avatar y banner.
3. Producir el piloto completo siguiendo el pipeline.
4. Producir los vídeos 2, 3 y 4 antes de publicar el primero.
