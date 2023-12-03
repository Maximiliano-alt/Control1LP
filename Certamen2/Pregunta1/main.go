package main

import (
	"fmt"
)

// Estado representa los posibles estados de un proceso.
type Estado int
type Cola struct {
	procesos []*Proceso
}

// Encolar añade un proceso al final de la cola.
func (c *Cola) Encolar(proceso *Proceso) {
	c.procesos = append(c.procesos, proceso)
}

// Desencolar elimina y retorna el primer proceso de la cola.
func (c *Cola) Desencolar() *Proceso {
	if len(c.procesos) == 0 {
		return nil
	}
	proceso := c.procesos[0]
	c.procesos = c.procesos[1:]
	return proceso
}

// Verifica si la cola está vacía.
func (c *Cola) EstaVacia() bool {
	return len(c.procesos) == 0
}

const (
	Nuevo = iota // iota se incrementa automáticamente para cada constante
	Listo
	Ejecutando
	Bloqueado
	Saliente
)

// Proceso es la estructura que representa un proceso en el sistema.
type Proceso struct {
	ID            int      // Identificador único del proceso
	Estado        Estado   // Estado actual del proceso
	PC            int      // Contador de programa (Program Counter)
	Instrucciones []string // Lista de instrucciones a ejecutar
	// Aquí puedes añadir más campos según sea necesario, como tiempo de llegada, prioridad, etc.
}

func main() {
	// Ejemplo de creación de un proceso
	procesoEjemplo := Proceso{
		ID:            1,
		Estado:        Nuevo,
		PC:            0,
		Instrucciones: []string{"INSTRUCCION1", "INSTRUCCION2", "INSTRUCCION3"},
	}
	colaListos := Cola{}
	colaBloqueados := Cola{}

	// Ejemplo de cómo encolar y desencolar procesos
	proceso1 := &Proceso{ID: 1, Estado: Listo}
	proceso2 := &Proceso{ID: 2, Estado: Bloqueado}

	colaListos.Encolar(proceso1)
	colaBloqueados.Encolar(proceso2)

	// Ejemplo de desencolado
	p := colaListos.Desencolar()
	fmt.Printf("Proceso desencolado de la cola de listos: ID %d\n", p.ID)

	p = colaBloqueados.Desencolar()
	fmt.Printf("Proceso desencolado de la cola de bloqueados: ID %d\n", p.ID)

	// Imprime la información del proceso
	fmt.Printf("Proceso ID: %d, Estado: %d, PC: %d, Instrucciones: %v\n",
		procesoEjemplo.ID, procesoEjemplo.Estado, procesoEjemplo.PC, procesoEjemplo.Instrucciones)
}
