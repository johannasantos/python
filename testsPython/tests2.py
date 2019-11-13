from pyfix import test, run_tests
import pyassert
import carrito


@test
def test_agregar_carrito():
    carrito.agregar_articulo("jabon", 10.78)
    precio = carrito.carrito["jabon"]
    pyassert.assert_that(precio).is_less_than(8)


if __name__ == "__main__":
    run_tests()
