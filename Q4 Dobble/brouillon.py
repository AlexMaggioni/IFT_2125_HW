        # Generate the n groups of n cards
        for i in range(n):
            for j in range(n):
                # Each card will contain one symbol from the base card
                card = [base_card[i + 1]]
                # Add n symbols to the card, ensuring no repeats and each symbol is unique across the deck
                for k in range(n):
                    symbol = (n + 1) + (n * k) + ((i * k + j) % n)
                    if symbol >= total_symbols:
                        symbol -= total_symbols
                    card.append(symbol)
                cards.append(card)

        # Generate the n remaining cards, each sharing one symbol with the base card
        for j in range(n):
            card = [base_card[0]]
            for k in range(1, n + 1):
                symbol = (n + 1) + (n * (k - 1)) + ((k * j) % n)
                if symbol >= total_symbols:
                    symbol -= total_symbols
                card.append(symbol)
            cards.append(card)



        # Generate the n groups of n cards
        for i in range(n):
            for j in range(n):
                # Each card will contain one symbol from the base card
                #card = [base_card[i + 1]]
                card = [base_card[i]]
                # Add n symbols to the card, ensuring no repeats and each symbol is unique across the deck
                for k in range(n):
                    # symbol = (n + 1) + (n * k) + ((i * k + j) % n)
                    symbol = (n + 2) + (n * k) + ((i * k + j) % n)
                    if symbol >= total_symbols:
                        symbol -= total_symbols
                    card.append(symbol)
                cards.append(card)



# Generate the n groups of n cards
        for i in range(n+1):
            for j in range(n):
                # Each card will contain one symbol from the base card
                #card = [base_card[i + 1]]
                card = [base_card[i]]
                # Add n symbols to the card, ensuring no repeats and each symbol is unique across the deck
                for k in range(n):
                    # symbol = (n + 1) + (n * k) + ((i * k + j) % n)
                    symbol = (n + 2) + (n * k) + ((i * k + j) % n)
                    if symbol >= total_symbols:
                        symbol -= total_symbols
                    card.append(symbol)
                cards.append(card)