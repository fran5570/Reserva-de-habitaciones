# gestion de reservas de habitaciones

## Descripción

Este proyecto es una aplicación de gestión de reservas que permite a los clientes reservar habitaciones en un hotel. La aplicación gestiona información de clientes, habitaciones y reservas, y permite la confirmación de reservas y el procesamiento de pagos.

## Herencia y Polimorfismo

### Principios Solid

### modo de ejecucion por consola python main.py

### interface grafica python gui.py

### Cada clase en nuestro proyecto tiene una única responsabilidad. Por ejemplo, la clase Cliente solo maneja la información del cliente (Single Responsibility Principle)

### si queremos añadir un nuevo tipo de habitación, podemos crear una nueva clase que herede de Habitacion sin necesidad de modificar el código existente(Open/Closed Principle)

### Las clases derivadas (HabitacionDoble, Suite) pueden ser utilizadas en lugar de la clase base (Habitacion) sin causar problemas en el programa (Liskov Substitution Principle)

### Hemos utilizado el patrón de fábrica para crear habitaciones, lo que permite que el código dependa de abstraccion en lugar de implementaciones concretas (Dependency Inversion Principle)
