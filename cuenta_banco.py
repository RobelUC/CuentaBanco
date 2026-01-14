class CuentaBanco:
    """
    Clase que representa una cuenta bancaria simple.
    Maneja depósitos, retiros y transferencias con validaciones.
    """

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        """
        Inicializa la cuenta bancaria.

        Args:
            titular (str): Nombre del dueño de la cuenta.
            saldo_inicial (float): Monto inicial (debe ser positivo).
        """
        if not isinstance(saldo_inicial, (int, float)):
            raise TypeError("El saldo inicial debe ser un número.")
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")

        self.titular = titular
        self.saldo = float(saldo_inicial)

    def deposito_cuenta(self, monto: float) -> None:
        """
        Realiza un depósito en la cuenta.

        Args:
            monto (float): Cantidad a depositar (debe ser > 0).
        """
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser numérico.")
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")

        self.saldo += monto
        print(f" Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")

    def retiro_cuenta(self, monto: float) -> None:
        """
        Realiza un retiro de la cuenta si hay fondos suficientes.

        Args:
            monto (float): Cantidad a retirar (debe ser > 0).
        """
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser numérico.")
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.saldo:
            raise ValueError(f"Fondos insuficientes. Saldo actual: ${self.saldo:.2f}")

        self.saldo -= monto
        print(f" Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")

    def transferencia_cuenta(self, monto: float, cuenta_destino: 'CuentaBanco') -> None:
        """
        Transfiere fondos de esta cuenta a otra.

        Args:
            monto (float): Cantidad a transferir.
            cuenta_destino (CuentaBanco): Objeto de la cuenta receptora.
        """
        if not isinstance(cuenta_destino, CuentaBanco):
            raise TypeError("La cuenta destino no es válida.")
        
        if cuenta_destino == self:
            raise ValueError("No puedes transferirte a la misma cuenta.")

        # Reutilizamos la lógica de retiro para validar saldo y monto
        print(f" Iniciando transferencia a {cuenta_destino.titular}...")
        self.retiro_cuenta(monto)

        # Si el retiro no falló, depositamos en la otra cuenta
        cuenta_destino.deposito_cuenta(monto)
        print(" Transferencia completada.")

    def saldo_cuenta(self) -> float:
        """
        Retorna el saldo actual de la cuenta.

        Returns:
            float: El saldo disponible.
        """
        return self.saldo