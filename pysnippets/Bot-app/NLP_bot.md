# Domino's Pizza Ordering Chatbot

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technical Architecture](#technical-architecture)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Components](#components)
7. [NLP Techniques](#nlp-techniques)
8. [Testing](#testing)
9. [Future Improvements](#future-improvements)

## Overview

The Domino's Pizza Ordering Chatbot is an advanced Natural Language Processing (NLP) based system that simulates a pizza ordering experience. The chatbot understands natural language inputs, maintains conversation context, and guides users through the complete pizza ordering process.

## Features

- Natural language understanding for pizza ordering
- Context-aware conversation management
- Support for multiple pizza types, sizes, and toppings
- Dynamic price calculation
- Order confirmation and summary generation
- Robust error handling and input validation
- Comprehensive unit testing suite

## Technical Architecture

### Core Components

1. **State Management**
   - Uses an `OrderState` enum for tracking conversation flow
   - States: INITIAL → PIZZA_SELECTION → SIZE_SELECTION → TOPPINGS_SELECTION → CRUST_SELECTION → CONFIRMATION → COMPLETED

2. **Data Models**
   ```python
   @dataclass
   class MenuItem:
       name: str
       price: float
       description: str
       variations: List[str]

   @dataclass
   class Order:
       pizza_type: Optional[str]
       size: Optional[str]
       toppings: List[str]
       crust: Optional[str]
       total_price: float
   ```

3. **NLP Pipeline**
   - Uses spaCy for natural language understanding
   - Custom intent detection using regex patterns
   - Entity extraction for pizza types, sizes, and toppings

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dominos-chatbot.git
   cd dominos-chatbot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

### Running the Chatbot

```python
from dominos_chatbot import DominosChatbot

chatbot = DominosChatbot()
response = chatbot.process_message("I want to order a pizza")
print(response)
```

### Example Conversation

```
User: Hello
Bot: Hello! Welcome to Domino's. Would you like to place an order?

User: Yes, I'd like to order a pizza
Bot: What type of pizza would you like? We have Margherita and Pepperoni.

User: Margherita please
Bot: What size would you like? (Small/Medium/Large)

User: Large with mushrooms and extra cheese
Bot: What type of crust would you like? (Thin/Thick/Stuffed/Regular)

User: Thin crust
Bot: Order Summary:
Pizza: Margherita
Size: Large
Toppings: mushrooms, extra cheese
Crust: thin
Total Price: $25.48

Would you like to confirm this order?

User: Yes
Bot: Thank you for your order! Your pizza will be ready in 30 minutes.
```

## Components

### 1. Intent Detection
The chatbot recognizes several types of intents:
- Greeting: "hello", "hi", "hey"
- Order: "order", "place order", "want pizza"
- Confirm: "confirm", "yes", "correct"
- Cancel: "cancel", "no", "stop"

```python
def _detect_intent(self, text: str) -> str:
    text = text.lower()
    for intent, patterns in self.intent_patterns.items():
        if any(re.search(pattern, text) for pattern in patterns):
            return intent
    return "unknown"
```

### 2. Entity Extraction
Specialized functions extract different types of entities:
- Pizza types using menu matching
- Sizes using predefined options
- Toppings using available options list
- Crust types using predefined options

### 3. Price Calculation
Dynamic price calculation based on:
- Base pizza price
- Size multipliers (small: 1x, medium: 1.5x, large: 2x)
- Topping prices ($1.50 per topping)
- Crust premiums (stuffed: +$3, thick: +$2)

## NLP Techniques

1. **Text Preprocessing**
   - Lowercase transformation
   - Pattern matching
   - Entity recognition

2. **Intent Classification**
   - Regular expression patterns
   - Keyword matching
   - Context awareness

3. **Entity Extraction**
   - Named Entity Recognition (NER)
   - Pattern matching
   - Custom entity recognition rules

4. **Context Management**
   - State machine implementation
   - Order tracking
   - Conversation flow management

## Testing

The chatbot includes a comprehensive test suite covering:

1. **Intent Detection Tests**
   - Greeting detection
   - Order intent detection
   - Confirmation detection
   - Cancellation detection

2. **Entity Extraction Tests**
   - Pizza type extraction
   - Size extraction
   - Toppings extraction
   - Crust type extraction

3. **Price Calculation Tests**
   - Base price calculation
   - Size multiplier effects
   - Topping price addition
   - Crust premium addition

4. **Order Flow Tests**
   - Complete order process
   - State transitions
   - Error handling

Run tests using:
```bash
python -m unittest test_dominos_chatbot.py
```

## Future Improvements

1. **Enhanced NLP Capabilities**
   - Implementation of more advanced NLP models
   - Support for more complex queries
   - Better handling of ambiguous inputs

2. **Extended Features**
   - Multiple pizza orders
   - Delivery address handling
   - Payment processing
   - Order tracking

3. **Technical Enhancements**
   - Database integration
   - API integration with actual ordering system
   - Performance optimizations
   - Multi-language support

4. **User Experience**
   - More natural conversation flow
   - Better error recovery
   - Personalization based on order history
   - Dietary preference handling
