# Análisis de caso de estudio: IEEE-CIS Fraud Detection

La detección de fraudes en transacciones es un problema crítico en el sector financiero. En este caso de estudio, se aborda la tarea de la predicción de transacciones fraudulentas en tarjetas de crédito. El dataset utilizado es provisto por Vesta Corporation. 

## Descripción del problema

El objetivo de este caso de estudio es predecir si una transacción es fraudulenta o no. Para ello, se implementarán diferentes modelos de aprendizaje automático que cuenten con la capacidad de clasificar transacciones en dos categorías: fraudulentas o no fraudulentas.

### Importancia del Problema

La detección de fraudes es esencial para minimizar las pérdidas financieras y mantener la confianza de los clientes en los sistemas de pago. Un sistema efectivo de detección de fraudes puede:

- Reducir las pérdidas económicas debidas a transacciones no autorizadas.
- Proteger a los clientes y a las instituciones financieras.
- Mejorar la seguridad y la reputación de las plataformas de comercio electrónico.
- Cumplir con regulaciones financieras y prevenir actividades ilícitas.

## Descripción del Dataset

El dataset provisto contiene información detallada de transacciones electrónicas, incluyendo variables categóricas y numéricas que describen aspectos de cada transacción.

### Tabla Transacciones

- **TransactionDT**: timedelta desde una referencia de datetime dada.
- **TransactionAMT**: monto del pago de la transacción en USD.
- **ProductCD**: código del producto, el producto para cada transacción.
- **card1 - card6**: información de la tarjeta de pago, como tipo de tarjeta, categoría de tarjeta, banco emisor, país, etc. Información enmascarada.
- **addr**: dirección, información enmascarada.
- **dist**: distancia, información enmascarada.
- **P_ y R_ emaildomain**: dominio de correo electrónico del comprador y del destinatario.
- **C1-C14**: conteo, como cuántas direcciones se encuentran asociadas con la tarjeta de pago, etc. El significado real está enmascarado.
- **D1-D15**: timedelta, como días entre transacciones anteriores, etc.
- **M1-M9**: coincidencia, como nombres en la tarjeta y la dirección, etc.
- **Vxxx**: características enrriquecidas diseñadas por Vesta, el significado real está enmascarado.

### Tabla Identidad
Las variables en esta tabla son información de identidad: información de conexión a la red (IP, ISP, Proxy, etc) y firma digital (UA/browser/os/version, etc) asociadas con las transacciones.
- Estas son recolectadas por el sistema de protección contra fraudes de Vesta y sus socios de seguridad digital.
- Los nombres de los campos están enmascarados y no se proporcionará un diccionario de pares para proteger la privacidad y por acuerdo contractual.

## Métrica de Evaluación objetivo

Para trabajar con el dataset IEEE-CIS Fraud Detection, la métrica de evaluación principal seleccionada es el Área Bajo la Curva de la Característica Operativa del Receptor (**ROC AUC**). Esta métrica es esencial en problemas de clasificación binaria como la detección de fraudes, ya que permite equilibrar correctamente las tasas de verdaderos positivos y falsos positivos. El **ROC AUC** mide la capacidad del modelo para distinguir entre clases, proporcionando una evaluación robusta y objetiva del rendimiento del modelo, especialmente en contextos con desbalanceo de clases significativos; como es el caso del presente problema.

Si bien el **ROC AUC** es la métrica principal, también se evaluarán otras métricas secundarias como la **Exactitud**, **Precisión**, **Recall** y **F1-Score** para obtener una visión más completa del rendimiento de los modelos.
