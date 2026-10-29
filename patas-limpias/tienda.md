# Kit Patas Limpias: plataforma y plan para arrancar

*Datos al 29/10/2026. Los montos están en pesos argentinos salvo que diga US$. Los precios oficiales los leí a través del buscador porque las páginas estaban bloqueadas en esta sesión. Solo los dos CLI los verifiqué directo en npm.*

## 1. Respuesta corta

**Elegiría Tiendanube Impulso con pago mensual: $79.999/mes, precio de octubre de 2026.** Es el plan más barato de Tiendanube que da acceso al código del tema. El CLI oficial `@tiendanube/cli` (v3.0.0, publicado el 27/10/2026) trabaja desde tu repo de git y trae skills oficiales para Claude Code. Además ya trae resuelto lo que en Argentina es crítico: Mercado Pago con cuotas, Andreani con Envío Nube sin abono, Meta Pixel con API de Conversiones nativa y todo facturado en pesos. Con 20 pedidos por mes cuesta parecido a Shopify Basic, y menos si a Shopify le sumás una app para Andreani. La condición es usar los 7 días de prueba para confirmar que `theme fork` funciona en tu cuenta, porque es lo único que no está confirmado por escrito.

**Cuándo conviene otra opción:**
- **Shopify Basic (US$25/mes):** si el fork de Tiendanube no te funciona en la prueba, si priorizás herramientas de código maduras (carrito AJAX documentado, sincronización con GitHub en los dos sentidos, vista previa local) o si pensás vender fuera de Argentina. La contra es que pagás en dólares con impuestos y Andreani va por una app paga.
- **Tiendanube Esencial ($27.999/mes) con la landing alojada aparte:** si querés salir a pautar esta semana con el menor gasto. La landing sigue en tu repo, pero no tocás el código de la tienda y perdés tu carrito propio.

Arrancá en mensual. Tiendanube ajusta los precios cada trimestre y el próximo aumento es en enero de 2027.

## 2. Comparación

| | Tiendanube Esencial + landing aparte | **Tiendanube Impulso (mi elección)** | Shopify Basic |
|---|---|---|---|
| Precio publicado | $27.999/mes ($20.999 en pago anual) | $79.999/mes ($59.999 en pago anual) | US$25/mes (US$19 en pago anual). Precio regional para Argentina según terceros |
| Costo mensual real en ARS | $27.999. Si se factura más IVA, $33.879 (no confirmado) | $79.999. Si se factura más IVA, $96.799 (no confirmado) | Estimado: unos $47.970 pagando con dólares propios o unos $59.670 pagando el resumen en pesos (dólar oficial a $1.560) |
| Comisión por venta con Mercado Pago | 2% de Tiendanube + Mercado Pago | 1% de Tiendanube + Mercado Pago | 2% de Shopify (en US$, cifra de terceros) + Mercado Pago |
| Edición de código | No. Solo CSS avanzado (hasta 58.000 caracteres) | Sí. Ipanema por fork con el CLI, o un tema clásico por FTP | Sí, completo desde Basic: Liquid, CSS, JS y layouts |
| Flujo con git y Claude Code | Solo la landing, alojada aparte. La tienda no | CLI con `pull`, `diff`, `check`, `push`, `preview` y `publish`. Ignora `.git`, trae skills para Claude Code y el fork es permanente | Shopify CLI 5.0.0 (`theme dev` con vista previa local) y sincronización con GitHub en los dos sentidos. Es lo más maduro |
| Envíos Andreani | Envío Nube sin abono: pagás solo la etiqueta | Envío Nube (Andreani y Correo Argentino) | Por app: Shipy desde US$30/mes. El envío gratis a sucursal se arma con una tarifa manual de $0 |
| Meta Pixel y CAPI | Nativo dentro de la tienda. En la landing externa el pixel lo ponés vos | Nativo: AddToCart, InitiateCheckout y Purchase salen por navegador y por servidor | App Facebook & Instagram en nivel "Máximo": gratis y con deduplicación |
| Checkout editable | No | No. Solo los colores de la tienda y algunas opciones | No, salvo en Plus. Se cambian logo, colores y tipografías. Los bloques solo van en "Gracias" y "Estado del pedido" |

**Notas:**
- **Mercado Pago cobra lo mismo en las tres:** 6,29% + IVA con acreditación al instante (unos 7,61% en total) o 1,49% + IVA a 35 días. Si ofrecés cuotas sin interés, el costo extra lo pagás vos: 7,79% en 2 cuotas, 10,49% en 3, 18,69% en 6 y 32,29% en 12, todo más IVA.
- **Cuota Simple ya no existe:** terminó el 30/06/2025. Hoy las cuotas sin interés se configuran en Mercado Pago o en Pago Nube y las absorbés vos.
- **Planes descartados:**
  - Tiendanube Inicial (gratis) no acepta Mercado Pago, solo Pago Nube.
  - Shopify Starter no se ofrece a tiendas nuevas y no da acceso al código.
- **Recargos sobre la factura de Shopify en dólares:**
  - IVA del 21%.
  - Percepción de Ingresos Brutos de alrededor del 2% en CABA (es un dato de 2025, sin confirmar para 2026).
  - Si pagás el resumen en pesos, una percepción del 30%, que según la prensa de octubre de 2026 sigue vigente. Como monotributista podés pedir que te la devuelvan, pero mientras tanto te saca plata.
  - La promo de 3 meses a US$1 varía según la cuenta.

## 3. Cuánto te cuesta cada pedido (20 pedidos/mes, kit de $56.900)

**Supuestos del cálculo:**
- 20 × $56.900 = $1.138.000 por mes.
- Mercado Pago en 1 pago con acreditación al instante: 6,29% + IVA = $4.331 por pedido.
- No incluye el envío gratis a sucursal: es igual en las tres opciones y se cotiza en el panel.
- Shopify convertido al dólar oficial de $1.560 (BNA, 29/10/2026).

| Opción | Plan prorrateado | Comisión de la plataforma | Mercado Pago | Total por pedido | % del kit |
|---|---|---|---|---|---|
| Tiendanube Esencial | $1.400 | $1.138 (2%) | $4.331 | **$6.869** | 12,1% |
| Tiendanube Impulso | $4.000 | $569 (1%) | $4.331 | **$8.900** | 15,6% |
| Shopify Basic, con dólares propios (estimado) | $2.399 | $1.400 (2% + impuestos, estimado) | $4.331 | **$8.130** | 14,3% |
| Shopify Basic, pagando en pesos (estimado) | $2.984 | $1.741 (2% + impuestos, estimado) | $4.331 | **$9.056** | 15,9% |
| Shopify Basic + Shipy para Andreani (estimado) | $5.277 a $6.564 | $1.400 a $1.741 | $4.331 | **$11.008 a $12.636** | 19,3% a 22,2% |

**Cómo leer la tabla:**
- **Las cuotas pesan más que la plataforma.** Entre plataformas la diferencia va de unos $1.000 a $4.000 por pedido. Las cuotas sin interés suman alrededor de $7.222 por pedido en 3 cuotas y $12.868 en 6, en cualquiera de las tres.
- **Si podés esperar 35 días para cobrar,** Mercado Pago baja a unos $1.026 por pedido.
- **Si el plan de Tiendanube se factura más IVA,** sumá $294 por pedido en Esencial o $840 en Impulso.
- **Con la promo de Shopify (3 meses a US$1),** el plan prorrateado baja a unos $96 a $119 por pedido. Mientras dure, Shopify es la opción más barata.
- **Impulso solo se paga por comisión** si vendés más de unos $5,2 millones por mes. Con tu volumen, los $52.000 de diferencia con Esencial los pagás por el acceso al código.
- **Pago Nube en lugar de Mercado Pago:** en Tiendanube el 1% de la plataforma pasa a 0%. Pago Nube cobra su propia tasa: 5,89% + IVA a 1 día en Impulso, según una calculadora de terceros.

## 4. Cómo llevar la landing a Tiendanube Impulso

1. **Cargá el catálogo pensando en la landing.** Un producto "Kit Patas Limpias" con 4 variantes:
   - Kit: $56.900
   - Kit doble: $99.900
   - Kit + toalla: $63.899
   - Kit doble + toalla: $106.899

   Cargá peso y medidas en cada variante, porque Envío Nube los necesita. Ojo: el stock es por variante, así que lo vas a ajustar a mano (con 5 a 40 pedidos se maneja). Si querés vender la toalla sola, cargala también como producto aparte.
2. **Prepará el repo y el CLI.**
   - Instalá Node 24.22.1 o superior y después `npm i -g @tiendanube/cli`.
   - Corré `nuvemshop skills install --project` para que las skills queden en el repo y Claude Code las lea.
   - Corré `tiendanube auth login`.
   - Hacé `theme clone --published`, después `theme fork` sobre el clon y `theme pull` a una carpeta `tienda/`.
   - Hacé commit del pull antes de tocar nada. El HTML original queda en `landing/` como referencia.
3. **La landing pasa a ser la página de producto.** Como vendés un solo producto, la plantilla de producto de Ipanema (`templates/pages/product.json`, según las skills del CLI) apunta a una sección propia con el HTML de la landing. El CSS, el JS, las imágenes, las animaciones y la tipografía 3D van a `static/` y quedan casi iguales. Lo que cambia: los precios, los nombres y los IDs de variante salen del objeto producto del tema y dejan de estar escritos a mano.
4. **Selector de packs.** Cada radio card representa una variante. Al elegirla, cambia la variante seleccionada en el formulario nativo del producto. El botón "Comprar" envía ese formulario o llama a la función de agregar al carrito del tema.
5. **Order bump de la toalla.** El checkbox cambia de "Kit" a "Kit + toalla" (o de "Kit doble" a "Kit doble + toalla"). Así se agrega una sola cosa al carrito por compra. Si preferís la toalla como producto aparte, el bump hace un segundo agregado cuando termina el primero.
6. **Carrito.** Tu drawer deja de manejar un carrito propio. Lo más seguro es reestilizar el panel de carrito nativo del tema con tu CSS, o abrir tu drawer después del agregado nativo mostrando lo que devuelve el tema. No uses endpoints no documentados como `/cart/update`: devuelven 405 en Patagonia y soporte avisó que los pueden bloquear sin aviso. "Finalizar compra" va al checkout nativo.
7. **Barra fija en el celular y tracking.**
   - La barra queda igual, y su botón dispara el mismo formulario nativo.
   - Sacá el pixel de Meta que está escrito en la landing y conectá Meta en Canales de venta > Instagram y Facebook.
   - No actives el CAPI Gateway ni cargues el evento Purchase a mano, porque se duplica.
   - Mostrá "3 cuotas sin interés de $X" calculado sobre el precio, pero solo si las configuraste en Mercado Pago.
8. **Publicá con red de seguridad.** El flujo de Claude Code es `theme check`, `theme diff`, `theme push`, `theme preview` (link para mirarlo en el celular) y, cuando vos lo apruebes, `theme publish`.
   - Para volver atrás se republica el tema anterior. Dejalo instalado, aunque el plan limita la cantidad de temas.
   - El fork no tiene historial propio: git es tu único respaldo.
   - Si el tema no está forkeado, el push saltea los archivos de código pero igual dice "éxito". Revisá la lista de omitidos.
   - Si el fork no anda durante la prueba, el plan B dentro de Impulso es un tema clásico por FTP (`theme ftp pull/push`). Ahí cada push va directo a producción.

**Lo que NO se puede personalizar: el checkout.** No acepta CSS ni HTML. Solo tiene el switch "usar colores de la tienda" y las opciones de Configuración > Opciones del checkout. Además, desde el 30/10/2026 solo entran al checkout scripts de apps con NubeSDK. Cómo convivir con eso:
- **Vendé todo antes del checkout:** pack, toalla, cuotas, garantía y envío gratis van en la landing.
- **Elegí cómo se ve Mercado Pago:** con Checkout Pro el cliente pasa al sitio de Mercado Pago; con Checkout API paga sin salir de la tienda. Solo puede haber un checkout transparente activo a la vez, así que choca con Pago Nube transparente.
- **Probá con plata real:** hacé una compra chica desde el celular, porque el plugin de Mercado Pago no tiene modo de prueba.
- **Meta ya está cubierto:** el Purchase lo manda la integración nativa.

**Caminos alternativos:**
- **Tiendanube Esencial con la landing aparte:** la landing va en Vercel o GitHub Pages y sus botones apuntan a `/cart-link/{variante}-{cantidad}`. Cada link agrega un solo producto, así que las variantes combinadas son obligatorias y tu drawer no puede mostrar el carrito real. Los precios quedan duplicados a mano y el tracking queda repartido entre dos dominios: usá el mismo pixel y un subdominio. Estimo de 0,5 a 1,5 días de trabajo.
- **Shopify Basic:** una plantilla `templates/product.patas-limpias.json` con la sección `sections/landing-patas.liquid`.
  - Los radio cards cambian el ID de variante.
  - El bump usa `POST /cart/add.js` con `items[]` para meter kit y toalla en una sola llamada.
  - Tu drawer lee `/cart.js` casi sin cambios.
  - La rama `main` se conecta al tema publicado y `staging` a un borrador.
  - En CI, publicar sobre el tema en vivo requiere `--allow-live` desde el CLI 5.0.0.
  - Con una cuenta gratis de Shopify Partner podés armar todo en una "client transfer store" y pagar recién cuando la transferís.

## 5. Qué hacés vos y qué hace Claude Code

**Vos (no se puede delegar):**
1. **ARCA:** CUIT, clave fiscal, alta de monotributo y punto de venta para Factura C. Con 5 a 40 pedidos podés facturar a mano en "Comprobantes en línea" o con una app (en Shopify, Emitio cuesta desde US$15/mes).
2. **Mercado Pago:** cuenta de vendedor a nombre de tu CUIT. En "Tu negocio > Costos y cuotas" elegís el plazo de acreditación y si ofrecés cuotas sin interés. Decidilo con la tabla de la sección 3.
3. **Tiendanube:**
   - Creá la cuenta, hacé la prueba de 7 días y contratá Impulso mensual con tu tarjeta.
   - Conectá Mercado Pago y activá Envío Nube.
   - Configurá el envío gratis a sucursal en Descuentos > Envío gratis.
   - El login del CLI lo hacés vos una vez.
4. **Dominio:** registrás el .com.ar en NIC Argentina con tu clave fiscal y lo apuntás a la tienda. El dominio propio solo funciona en planes pagos.
5. **Meta:** portafolio comercial, cuenta publicitaria, verificación del dominio y conexión desde Tiendanube.
6. **Legales y control:** políticas de privacidad y de cambios, botón de arrepentimiento, compras de prueba reales y la aprobación de cada `theme publish`.

**Claude Code, en el repo:**
- **Herramientas:** instala el CLI y las skills, y hace el pull, el fork y el primer commit.
- **Landing:** la porta a una sección, conecta los radio cards y el bump a las variantes, adapta el carrito nativo y la barra fija, y calcula el texto de cuotas.
- **Tracking:** saca el pixel duplicado y revisa que no se repitan eventos.
- **Antes de publicar:** corre `theme check`, `theme performance`, `diff`, `push` y `preview`, y te deja el link para revisar.
- **Documentación y automatización:** escribe en el README el flujo de deploy y el rollback. Si querés, arma un GitHub Action con `auth login --token`.
- **Lo que no puede hacer:** crear cuentas, aceptar términos, pagar, configurar lo que solo está en los paneles (Mercado Pago, Envío Nube, dominio, Meta) ni publicar sin tu OK.

## 6. Fuentes (consultadas el 29/10/2026)

**Tiendanube**
- Planes y precios (Esencial $27.999, Impulso $79.999; versión de octubre de 2026 vista a través del buscador; coincide con Open24 al 13/10/2026): https://www.tiendanube.com/planes-y-precios
- Ajuste trimestral de precios (artículo actualizado el 20/01/2026): https://ayuda.tiendanube.com/es_AR/123482-planes/como-se-ajusta-el-precio-de-los-planes-de-tiendanube
- Costo por transacción (2%, 1% y 0,7%; fecha no visible): https://ayuda.tiendanube.com/es_AR/123484-costos-por-transaccion/que-son-los-costos-por-transaccion-de-tiendanube
- Plan Inicial sin Mercado Pago y dominio solo en planes pagos: https://ayuda.tiendanube.com/es_AR/123482-planes/que-funcionalidades-incluye-el-plan-gratuito-de-tiendanube
- Código del tema desde Impulso: https://ayuda.tiendanube.com/es_AR/123227-editar-el-codigo-de-diseno/como-modificar-el-diseno-desde-el-codigo-de-mi-tienda
- Bloque "Código" de Ipanema (plan sin confirmar): https://ayuda.tiendanube.com/es_MX/diseno-ipanema/como-personalizar-mi-diseno-ipanema
- CLI v3.0.0 (27/10/2026, verificado en el registro de npm): https://www.npmjs.com/package/@tiendanube/cli y https://github.com/TiendaNube/cli
- Issue #7 del CLI, "fork chegando em breve" (septiembre de 2026): https://github.com/TiendaNube/cli/issues/7
- Checkout no editable: https://ayuda.tiendanube.com/es_MX/123367-opciones-del-checkout/como-adaptar-el-checkout-a-los-colores-de-mi-marca
- Cart-link: https://ayuda.tiendanube.com/es_ES/ventas/como-compartir-el-link-de-un-producto-al-carrito
- Carrito en el tema: https://docs.tiendanube.com/help/carrito-de-compras-rpidas-jq-nuvem y https://github.com/TiendaNube/base-theme (commit del 04/11/2025)
- Draft Orders con `checkout_url`: https://tiendanube.github.io/api-documentation/resources/draft-order
- API de Conversiones de Meta: https://ayuda.tiendanube.com/es_ES/pixel-de-facebook/como-activar-la-api-de-conversiones-de-facebook
- Envío Nube (ayuda de alrededor de febrero de 2026): https://ayuda.tiendanube.com/es_ES/envio-nube/que-es-envio-nube-y-como-activarlo-en-mi-tienda
- Envío gratis: https://ayuda.tiendanube.com/es_ES/122907-envio-gratis/como-ofrecer-envio-gratuito
- Prueba de 7 días: https://www.tiendanube.com/blog/tiendanube-gratis/
- Costos de Pago Nube (2026; las tasas por plan salen de una calculadora de terceros): https://www.tiendanube.com/blog/pago-nube-costos/
- Fin de Cuota Simple (30/06/2025): https://www.tiendanube.com/blog/que-es-cuota-simple/
- Umbral de unos $5,2 millones (tercero, octubre de 2026): https://tupaginaya.net.ar/alternativa-tiendanube

**Mercado Pago**
- Comisiones del Checkout (6,29%, 4,39%, 3,39% y 1,49% + IVA; página oficial, fecha no visible): https://www.mercadopago.com.ar/herramientas-para-vender/check-out
- Costo de las cuotas sin interés (7,79% a 41,59% + IVA; vigente desde el 10/02/2026 según un resumen de la ayuda): https://www.mercadopago.com.ar/herramientas-para-vender/link-de-pago
- App para Shopify: https://www.mercadopago.com.ar/developers/es/docs/shopify/integration-configuration/checkout-cards

**Shopify**
- Precio para Argentina, US$25 y US$19 (terceros: G2Rocket 11/09/2026, Pointweb agosto de 2026, Tupaginaya 12/10/2026): https://g2rocket.com/shopify-argentina-costos-conviene/ · https://pointweb.com.ar/guias/tiendanube-woocommerce-o-shopify/ · https://tupaginaya.net.ar/alternativa-shopify
- Cargo por pasarela externa (el Help Center dice que depende del país; el 2% sale de terceros): https://help.shopify.com/en/manual/payments/third-party-providers
- Starter no disponible para tiendas nuevas: https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features/shopify-starter-plan
- Promo de 3 meses a US$1 (hilo de la comunidad, sin fecha): https://community.shopify.com/t/3-meses-por-1-al-mes/180586
- Integración con GitHub: https://shopify.dev/docs/storefronts/themes/tools/github
- Shopify CLI 5.0.0 y `--allow-live` (27/10/2026, verificado en npm): https://registry.npmjs.org/@shopify/cli
- CI/CD de temas: https://shopify.dev/docs/storefronts/themes/tools/cli/ci-cd
- AJAX Cart API: https://shopify.dev/docs/api/ajax/reference/cart
- Plantillas JSON: https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates
- Límites del checkout fuera de Plus (tercero, 2026): https://www.flatlineagency.com/blog/shopify-checkout-extensibility-2026
- Meta Pixel y CAPI: https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/meta-data-sharing
- Shipy, desde US$30/mes (octubre de 2026): https://apps.shopify.com/shipy-app
- Emitio, facturación ARCA desde US$15/mes: https://apps.shopify.com/emitio

**Impuestos y tipo de cambio**
- Dólar oficial BNA a $1.560 (venta) y dólar tarjeta a $2.028 (29/10/2026): https://www.lanacion.com.ar/economia/dolar/dolar-hoy-y-dolar-blue-en-vivo-a-cuanto-cotiza-el-oficial-y-cual-es-el-precio-del-paralelo-este-nid29102026/
- Recargos de +53% y +23% (estimación de terceros, 2026): https://impuestito.org/blog/que-impuestos-cobra-arca-al-pagar-juegos-y-suscripciones-con-tarjeta-en-dolares
- Percepción del 30% vigente (octubre de 2026): https://www.eldestapeweb.com/economia/pagar-dolares-tarjeta-octubre-2026-ahorrar-evitar-recargos-202610611469 · https://www.cronista.com/economia-politica/por-que-no-se-elimino-el-dolar-tarjeta-cuanto-recaudo-arca-en-lo-que-va-de-2026/

**Sin confirmar, a revisar antes de pagar:**
- Si los planes de Tiendanube incluyen IVA.
- Qué plan exige el `theme fork` del CLI.
- Si el bloque "Código" de Ipanema funciona en Esencial.
- El precio exacto de Shopify Basic para Argentina y su cargo del 2%.
- La percepción de Ingresos Brutos de CABA en 2026.
