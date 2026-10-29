# Patas Limpias

Landing de un solo producto para el limpiador eléctrico de patas, con carrito.

- `landing/index.html`: la página. Se abre directo en el navegador.
- `landing/img/`: fotos del producto.

## Antes de salir a pautar

- Cargar el número de WhatsApp en la constante `WHATSAPP` del script, con código de país y sin "+" (y el usuario de Instagram sin "@" en `INSTAGRAM`, si hay). Sin esto el pedido final no tiene a dónde ir: con cualquiera de los dos cargado aparece el botón de WhatsApp y el contacto en el pie y en la FAQ del talle.
- Los precios salen de `PRODUCTS` en el script; el HTML trae una copia para cuando no corre JS. Si cambian, actualizá también esa copia.
- Confirmar o ajustar las promesas operativas de la FAQ: seguimiento del envío y garantía de 30 días.
- Confirmar que la toalla de las fotos del kit es la que se envía. Si es así, se puede sacar la etiqueta "Imagen ilustrativa" de esas fotos.
- Cargar reseñas reales cuando lleguen las primeras ventas. La página no muestra reseñas inventadas a propósito.
- El checkout arma el pedido y lo manda por WhatsApp. Para cobrar online hay que pasar la página a Tiendanube o conectar Mercado Pago.
