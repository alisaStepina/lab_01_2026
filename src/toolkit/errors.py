class ToolkitError(Exception):
    """Базовая ошибка для всего пакета."""


class ExpressionError(ToolkitError):
    """Базовая ошибка для калькулятора."""


class EmptyExpressionError(ExpressionError):
    """Пустое выражение."""


class InvalidCharacterError(ExpressionError):
    """Недопустимый символ."""


class InvalidNumberError(ExpressionError):
    """Недопустимое число."""


class MissingOperandError(ExpressionError):
    """Нехватает операнда."""


class DoubleOperatorError(ExpressionError):
    """Два оператора подряд."""


class DivisionByZeroError(ExpressionError):
    """Деление на ноль."""


class ConversionError(ToolkitError):
    """Базовая ошибка для конвертора."""


class UnknownUnitError(ConversionError):
    """Еденица измерения не поддерживется."""


class IncompatibleUnitsError(ConversionError):
    """Несовместимые еденицы измерения."""


class BelowAbsoluteZeroError(ConversionError):
    """Температура ниже абсолютного нуля."""



