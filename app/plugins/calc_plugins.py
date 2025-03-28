"""
A plugin that provides all calculator operations.
"""
import logging
import math
from app.calculator import Calculator

class AddCommand:
    def __init__(self, history_manager=None):
        self.history_manager = history_manager
        self.calculator = Calculator()
    def execute(self, a, b):
        result = self.calculator.add(a, b)
        logging.info(f"AddCommand: {a} + {b} = {result}")
        if self.history_manager:
            self.history_manager.add_record("add", a, b, result)
        return result

class SubtractCommand:
    def __init__(self, history_manager=None):
        self.history_manager = history_manager
        self.calculator = Calculator()
    def execute(self, a, b):
        result = self.calculator.subtract(a, b)
        logging.info(f"SubtractCommand: {a} - {b} = {result}")
        if self.history_manager:
            self.history_manager.add_record("subtract", a, b, result)
        return result

class MultiplyCommand:
    def __init__(self, history_manager=None):
        self.history_manager = history_manager
        self.calculator = Calculator()
    def execute(self, a, b):
        result = self.calculator.multiply(a, b)
        logging.info(f"MultiplyCommand: {a} * {b} = {result}")
        if self.history_manager:
            self.history_manager.add_record("multiply", a, b, result)
        return result

class DivideCommand:
    def __init__(self, history_manager=None):
        self.history_manager = history_manager
        self.calculator = Calculator()
    def execute(self, a, b):
        result = self.calculator.divide(a, b)
        logging.info(f"DivideCommand: {a} / {b} = {result}")
        if self.history_manager:
            self.history_manager.add_record("divide", a, b, result)
        return result

def register(history_manager=None):
    """
    Register all calculator operation commands as plugins.
    """
    return {
        "add": AddCommand(history_manager),
        "subtract": SubtractCommand(history_manager),
        "multiply": MultiplyCommand(history_manager),
        "divide": DivideCommand(history_manager),
    }
