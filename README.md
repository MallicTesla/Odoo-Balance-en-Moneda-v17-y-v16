Balance Moneda

Este repositorio contiene el módulo Balance Moneda, desarrollado para extender las funcionalidades del modelo account.move.line en Odoo. El módulo agrega un nuevo campo llamado Balance en Moneda (balance_currency), que calcula y muestra el saldo (Debe - Haber) en la moneda definida en la cuenta contable asociada. Además, incluye mejoras en las vistas Tree y Pivot para un análisis contable más detallado.

Estructura del Repositorio

El repositorio contiene dos versiones del módulo, una para Odoo 16 y otra para Odoo 17:

├── balance_moneda_v16
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py
│   ├── security
│   │   └── ir.model.access.csv
│   ├── views
│   │   └── account_move_line_views.xml
│   ├── __init__.py
│   └── __manifest__.py
└── balance_moneda_v17
    ├── models
    │   ├── __init__.py
    │   └── models.py
    ├── security
    │   └── ir.model.access.csv
    ├── views
    │   └── account_move_line_views.xml
    ├── __init__.py
    └── __manifest__.py

Características del Módulo

Campo nuevo: Balance en Moneda (balance_currency)

Calcula y muestra el saldo (Debe - Haber) en la moneda definida en la cuenta contable asociada.

Usa la moneda de la cuenta (account_id.currency_id) para realizar las conversiones necesarias.

Herencia y mejora de vistas:

Se extienden las vistas Tree y Pivot para incluir los campos:

balance_currency: Balance en la moneda de la cuenta.

amount_currency: Importe en divisa.

currency_id: Divisa utilizada.

Compatibilidad:

balance_moneda_v16: Compatible con Odoo 16.

balance_moneda_v17: Compatible con Odoo 17.

Requisitos

Odoo 16 o 17, dependiendo de la versión del módulo.

Módulo base de contabilidad (account) instalado.

Instalación

Clona este repositorio en la carpeta de addons de tu instalación de Odoo:

git clone https://github.com/tu_usuario/balance_moneda.git

Reinicia el servidor de Odoo:

./odoo-bin -u all -d <nombre_de_base_de_datos>

Activa el módulo desde la interfaz de Odoo:

Ve a Aplicaciones.

Busca "Balance Moneda".

Instálalo.

Uso del Módulo

Accede al menú de Contabilidad.

Visualiza los apuntes contables en las vistas Tree y Pivot.

Observa los nuevos campos:

Balance en Moneda: Muestra el saldo calculado en la moneda de la cuenta contable.

Importe en Divisa y Divisa: Permiten un análisis más detallado.

Notas para Desarrolladores

El módulo extiende el modelo account.move.line usando _inherit.

Se asegura compatibilidad con la configuración de monedas de Odoo, incluyendo monedas de la cuenta y de la compañía.

El archivo ir.model.access.csv garantiza permisos de lectura adecuados para los campos añadidos.

Licencia

Este módulo se distribuye bajo la licencia LGPL-3. Consulta el archivo LICENSE para más información.