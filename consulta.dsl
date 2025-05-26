load "inventario.csv";
filter column "cantidad_stock" > 350;
aggregate count column "id_producto";
aggregate average column "precio_unitario";
print;

load "inventario.csv";
filter column "precio_unitario" > 1000;
aggregate count column "id_producto";
aggregate sum column "precio_unitario";
print;

load "inventario.csv";
filter column "categoria" = "Escolar";
aggregate average column "precio_unitario";
print;

load "inventario.csv";
filter column "precio_unitario" between 100 and 500;
aggregate sum column "precio_unitario";
print;

load "inventario.csv";
filter column "proveedor" = "ProveedorC";
aggregate sum column "cantidad_stock";
print;

load "inventario.csv";
filter column "categoria" = "Escolar";
filter column "precio_unitario" < 1000;
filter column "cantidad_stock" >= 100;
aggregate count column "id_producto";
aggregate sum column "cantidad_stock";
aggregate average column "precio_unitario";
print;

load "inventario.csv";
filter column "categoria" = "Oficina";
aggregate count column "id_producto";
aggregate average column "precio_unitario";
print;

load "inventario.csv";
filter column "estado_producto" = "Agotado";
aggregate sum column "precio_unitario";
print;

load "inventario.csv";
filter column "cantidad_stock" >= 400;
aggregate average column "precio_unitario";
print;

load "inventario.csv";
filter column "precio_unitario" >= 2000;
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "proveedor" = "ProveedorA";
aggregate sum column "cantidad_stock";
print;

load "inventario.csv";
filter column "categoria" = "Escolar";
filter column "cantidad_stock" > 300;
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "estado_producto" = "Agotado";
aggregate average column "cantidad_stock";
print;

load "inventario.csv";
filter column "ubicacion" = "A1";
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "cantidad_stock" < 200;
aggregate average column "precio_unitario";
print;

load "inventario.csv";
filter column "precio_unitario" = 300;
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "proveedor" = "ProveedorB";
aggregate average column "precio_unitario";
print;

load "inventario.csv";
filter column "estado_producto" = "Disponible";
aggregate sum column "cantidad_stock";
print;

load "inventario.csv";
filter column "cantidad_stock" >= 360;
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "categoria" = "Oficina";
filter column "estado_producto" = "Disponible";
aggregate average column "precio_unitario";
print;

load "inventario.csv";
filter column "precio_unitario" >= 1000;
filter column "estado_producto" = "Disponible";
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "proveedor" = "ProveedorC";
filter column "estado_producto" = "Agotado";
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "categoria" = "Escolar";
filter column "precio_unitario" < 1000;
aggregate average column "cantidad_stock";
print;

load "inventario.csv";
filter column "cantidad_stock" > 450;
print;

load "inventario.csv";
filter column "precio_unitario" > 1500;
aggregate sum column "cantidad_stock";
print;

load "inventario.csv";
filter column "ubicacion" = "C1";
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "estado_producto" = "Agotado";
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "categoria" = "Oficina";
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "categoria" = "Escolar";
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "cantidad_stock" < 100;
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "proveedor" = "ProveedorB";
filter column "estado_producto" = "Disponible";
aggregate average column "precio_unitario";
print;

load "inventario.csv";
filter column "ubicacion" = "B2";
aggregate sum column "precio_unitario";
print;

load "inventario.csv";
filter column "precio_unitario" <= 500;
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "cantidad_stock" >= 375;
aggregate average column "precio_unitario";
print;

load "inventario.csv";
filter column "proveedor" = "ProveedorC";
filter column "precio_unitario" = 2000;
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "estado_producto" = "Disponible";
filter column "cantidad_stock" > 380;
aggregate count column "id_producto";
print;

load "inventario.csv";
filter column "categoria" = "Oficina";
filter column "precio_unitario" > 1500;
aggregate average column "cantidad_stock";
print;

load "inventario.csv";
filter column "cantidad_stock" >= 390;
filter column "estado_producto" = "Agotado";
print;

load "inventario.csv";
filter column "precio_unitario" = 1200;
aggregate count column "id_producto";
print;
