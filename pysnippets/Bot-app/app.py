import spacy
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import re

# Load SpaCy model with error handling
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    print("SpaCy model 'en_core_web_sm' not found. Downloading now...")
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

class OrderState(Enum):
    INITIAL = "initial"
    PIZZA_SELECTION = "pizza_selection"
    SIZE_SELECTION = "size_selection"
    TOPPINGS_SELECTION = "toppings_selection"
    CRUST_SELECTION = "crust_selection"
    CONFIRMATION = "confirmation"
    COMPLETED = "completed"

@dataclass
class MenuItem:
    name: str
    price: float
    description: str
    variations: List[str]
    
@dataclass
class Order:
    pizza_type: Optional[str] = None
    size: Optional[str] = None
    toppings: List[str] = None
    crust: Optional[str] = None
    total_price: float = 0.0
    
    def __post_init__(self):
        if self.toppings is None:
            self.toppings = []

class DominosChatbot:
    def __init__(self):
        # Load menu data
        self.menu = self._load_menu()
        self.order = Order()
        self.state = OrderState.INITIAL
        
        # Intent patterns
        self.intent_patterns = {
            'greeting': [r'hello', r'hi', r'hey', r'start'],
            'order': [r'order', r'place.*order', r'want.*pizza'],
            'confirm': [r'confirm', r'yes', r'correct'],
            'cancel': [r'cancel', r'no', r'stop'],
        }
        
    def _load_menu(self) -> Dict[str, MenuItem]:
        # Sample menu data
        menu_data = {
            "Margherita": MenuItem(
                name="Margherita",
                price=10.99,
                description="Classic tomato and mozzarella",
                variations=["margherita", "plain cheese"]
            ),
            "Pepperoni": MenuItem(
                name="Pepperoni",
                price=12.99,
                description="Pepperoni and cheese",
                variations=["pepperoni"]
            ),
        }
        return menu_data
    
    def _detect_intent(self, text: str) -> str:
        text = text.lower()
        for intent, patterns in self.intent_patterns.items():
            if any(re.search(pattern, text) for pattern in patterns):
                return intent
        return "unknown"
    
    def _extract_pizza_type(self, text: str) -> Optional[str]:
        doc = nlp(text.lower())
        for pizza_name, item in self.menu.items():
            if pizza_name.lower() in text.lower() or \
               any(variation in text.lower() for variation in item.variations):
                return pizza_name
        return None
    
    def _extract_size(self, text: str) -> Optional[str]:
        sizes = {"small": 1, "medium": 1.5, "large": 2}
        doc = nlp(text.lower())
        for size in sizes:
            if size in text.lower():
                return size
        return None
    
    def _extract_toppings(self, text: str) -> List[str]:
        available_toppings = [
            "mushrooms", "onions", "peppers", "olives", 
            "extra cheese", "bacon", "chicken"
        ]
        doc = nlp(text.lower())
        found_toppings = []
        for topping in available_toppings:
            if topping in text.lower():
                found_toppings.append(topping)
        return found_toppings
    
    def _extract_crust(self, text: str) -> Optional[str]:
        crust_types = ["thin", "thick", "stuffed", "regular"]
        doc = nlp(text.lower())
        for crust in crust_types:
            if crust in text.lower():
                return crust
        return None
    
    def _calculate_price(self) -> float:
        base_price = self.menu[self.order.pizza_type].price if self.order.pizza_type else 0
        size_multiplier = {"small": 1, "medium": 1.5, "large": 2}
        topping_price = len(self.order.toppings) * 1.5
        crust_extra = {"thin": 0, "thick": 2, "stuffed": 3, "regular": 0}
        
        total = base_price
        if self.order.size:
            total *= size_multiplier[self.order.size]
        total += topping_price
        if self.order.crust:
            total += crust_extra[self.order.crust]
        
        return round(total, 2)
    
    def process_message(self, message: str) -> str:
        intent = self._detect_intent(message)
        
        if intent == "cancel":
            self.state = OrderState.INITIAL
            self.order = Order()
            return "Order cancelled. How can I help you?"
            
        if self.state == OrderState.INITIAL:
            if intent == "greeting":
                return "Hello! Welcome to Domino's. Would you like to place an order?"
            elif intent == "order":
                self.state = OrderState.PIZZA_SELECTION
                return "What type of pizza would you like? We have Margherita and Pepperoni."
                
        elif self.state == OrderState.PIZZA_SELECTION:
            pizza_type = self._extract_pizza_type(message)
            if pizza_type:
                self.order.pizza_type = pizza_type
                self.state = OrderState.SIZE_SELECTION
                return "What size would you like? (Small/Medium/Large)"
            else:
                return "I didn't catch that. Please choose from Margherita or Pepperoni."
                
        elif self.state == OrderState.SIZE_SELECTION:
            size = self._extract_size(message)
            if size:
                self.order.size = size
                self.state = OrderState.TOPPINGS_SELECTION
                return "Would you like any extra toppings? Available options: mushrooms, onions, peppers, olives, extra cheese, bacon, chicken"
            else:
                return "Please specify a valid size (Small/Medium/Large)."
                
        elif self.state == OrderState.TOPPINGS_SELECTION:
            if "no" in message.lower():
                self.state = OrderState.CRUST_SELECTION
                return "What type of crust would you like? (Thin/Thick/Stuffed/Regular)"
            
            toppings = self._extract_toppings(message)
            if toppings:
                self.order.toppings.extend(toppings)
                self.state = OrderState.CRUST_SELECTION
                return "What type of crust would you like? (Thin/Thick/Stuffed/Regular)"
            else:
                return "I didn't catch any toppings. Please specify from the available options or say 'no' for no toppings."
                
        elif self.state == OrderState.CRUST_SELECTION:
            crust = self._extract_crust(message)
            if crust:
                self.order.crust = crust
                self.order.total_price = self._calculate_price()
                self.state = OrderState.CONFIRMATION
                return self._generate_order_summary()
            else:
                return "Please specify a valid crust type (Thin/Thick/Stuffed/Regular)."
                
        elif self.state == OrderState.CONFIRMATION:
            if intent == "confirm":
                self.state = OrderState.COMPLETED
                return "Thank you for your order! Your pizza will be ready in 30 minutes."
            elif intent == "cancel":
                self.state = OrderState.INITIAL
                self.order = Order()
                return "Order cancelled. Would you like to start a new order?"
                
        return "I'm not sure what you mean. Could you please rephrase that?"
    
    def _generate_order_summary(self) -> str:
        summary = "\nOrder Summary:\n"
        summary += f"Pizza: {self.order.pizza_type}\n"
        summary += f"Size: {self.order.size}\n"
        summary += f"Toppings: {', '.join(self.order.toppings) if self.order.toppings else 'No extra toppings'}\n"
        summary += f"Crust: {self.order.crust}\n"
        summary += f"Total Price: ${self.order.total_price}\n"
        summary += "\nWould you like to confirm this order?"
        return summary

if __name__ == "__main__":
    chatbot = DominosChatbot()
    print("Welcome to Domino's Pizza Chatbot! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        response = chatbot.process_message(user_input)
        print(f"Bot: {response}")