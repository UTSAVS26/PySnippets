import unittest
from app import DominosChatbot, OrderState, Order

class TestDominosChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = DominosChatbot()
        
    def test_intent_detection(self):
        # Test greeting intent
        self.assertEqual(self.chatbot._detect_intent("hello there"), "greeting")
        self.assertEqual(self.chatbot._detect_intent("hi"), "greeting")
        
        # Test order intent
        self.assertEqual(self.chatbot._detect_intent("I want to order a pizza"), "order")
        self.assertEqual(self.chatbot._detect_intent("place order"), "order")
        
        # Test confirm intent
        self.assertEqual(self.chatbot._detect_intent("yes please"), "confirm")
        self.assertEqual(self.chatbot._detect_intent("confirm"), "confirm")
        
        # Test cancel intent
        self.assertEqual(self.chatbot._detect_intent("no thanks"), "cancel")
        self.assertEqual(self.chatbot._detect_intent("cancel"), "cancel")
        
        # Test unknown intent
        self.assertEqual(self.chatbot._detect_intent("random text"), "unknown")
    
    def test_pizza_type_extraction(self):
        # Test exact match
        self.assertEqual(self.chatbot._extract_pizza_type("I want a Margherita"), "Margherita")
        self.assertEqual(self.chatbot._extract_pizza_type("Pepperoni please"), "Pepperoni")
        
        # Test variations
        self.assertEqual(self.chatbot._extract_pizza_type("plain cheese pizza"), "Margherita")
        
        # Test no match
        self.assertIsNone(self.chatbot._extract_pizza_type("I want something else"))
    
    def test_size_extraction(self):
        # Test valid sizes
        self.assertEqual(self.chatbot._extract_size("I want a small pizza"), "small")
        self.assertEqual(self.chatbot._extract_size("medium size please"), "medium")
        self.assertEqual(self.chatbot._extract_size("large"), "large")
        
        # Test no size
        self.assertIsNone(self.chatbot._extract_size("I want a pizza"))
    
    def test_toppings_extraction(self):
        # Test single topping
        self.assertEqual(
            self.chatbot._extract_toppings("add mushrooms"),
            ["mushrooms"]
        )
        
        # Test multiple toppings
        self.assertEqual(
            set(self.chatbot._extract_toppings("mushrooms and onions with extra cheese")),
            {"mushrooms", "onions", "extra cheese"}
        )
        
        # Test no toppings
        self.assertEqual(self.chatbot._extract_toppings("no toppings"), [])
    
    def test_crust_extraction(self):
        # Test valid crust types
        self.assertEqual(self.chatbot._extract_crust("thin crust"), "thin")
        self.assertEqual(self.chatbot._extract_crust("thick crust please"), "thick")
        self.assertEqual(self.chatbot._extract_crust("stuffed"), "stuffed")
        self.assertEqual(self.chatbot._extract_crust("regular crust"), "regular")
        
        # Test no crust
        self.assertIsNone(self.chatbot._extract_crust("no preference"))
    
    def test_price_calculation(self):
        # Test basic pizza price
        self.chatbot.order = Order(
            pizza_type="Margherita",
            size="small",
            toppings=[],
            crust="regular"
        )
        self.assertEqual(self.chatbot._calculate_price(), 10.99)
        
        # Test with size multiplier
        self.chatbot.order.size = "large"
        self.assertEqual(self.chatbot._calculate_price(), 21.98)
        
        # Test with toppings
        self.chatbot.order.toppings = ["mushrooms", "onions"]
        self.assertEqual(self.chatbot._calculate_price(), 24.98)
        
        # Test with premium crust
        self.chatbot.order.crust = "stuffed"
        self.assertEqual(self.chatbot._calculate_price(), 27.98)
    
    def test_order_flow(self):
        # Test initial greeting
        response = self.chatbot.process_message("hello")
        self.assertEqual(self.chatbot.state, OrderState.INITIAL)
        self.assertIn("Welcome to Domino's", response)
        
        # Test starting order
        response = self.chatbot.process_message("I want to order")
        self.assertEqual(self.chatbot.state, OrderState.PIZZA_SELECTION)
        self.assertIn("What type of pizza", response)
        
        # Test pizza selection
        response = self.chatbot.process_message("Margherita")
        self.assertEqual(self.chatbot.state, OrderState.SIZE_SELECTION)
        self.assertIn("What size", response)
        
        # Test size selection
        response = self.chatbot.process_message("large")
        self.assertEqual(self.chatbot.state, OrderState.TOPPINGS_SELECTION)
        self.assertIn("extra toppings", response)
        
        # Test toppings selection
        response = self.chatbot.process_message("mushrooms and onions")
        self.assertEqual(self.chatbot.state, OrderState.CRUST_SELECTION)
        self.assertIn("type of crust", response)
        
        # Test crust selection
        response = self.chatbot.process_message("thin")
        self.assertEqual(self.chatbot.state, OrderState.CONFIRMATION)
        self.assertIn("Order Summary", response)
        
        # Test confirmation
        response = self.chatbot.process_message("confirm")
        self.assertEqual(self.chatbot.state, OrderState.COMPLETED)
        self.assertIn("Thank you for your order", response)

if __name__ == '__main__':
    unittest.main()