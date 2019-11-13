import unittest
import carrito


class TestCarrito(unittest.TestCase):

    def test_agregar_producto(self):
        carrito.agregar_articulo("jabon", 10.78)
        precio = carrito.carrito["jabon"]
        self.assertTrue(precio == 10.78, "El precio no es correcto")

    def test_eliminar_producto(self):
        carrito.agregar_articulo("jabon", 10.78)
        self.assertEqual(carrito.calcular_total(), 10.78)
        carrito.sacar_articulo("jabon")
        self.assertEqual(carrito.calcular_total(), 0)


if __name__ == '__main__':
    unittest.main()
