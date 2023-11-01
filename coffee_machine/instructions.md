# Coffee Machine Program Requirements

1. **Prompt User:**

   - Ask: “What would you like? (espresso/latte/cappuccino):”
     - Check the user’s input to decide what to do next.
     - The prompt should reappear post-action completion, e.g., after the drink is dispensed, to serve the next customer.

2. **Turn Off the Coffee Machine:**

   - Enter “off” at the prompt.
     - For maintainers, “off” is the secret word to turn off the machine. Your code should end execution when this happens.

3. **Print Report:**

   - Enter “report” at the prompt to generate a report showing the current resource values.
     - e.g.,
       ```
       Water: 100ml
       Milk: 50ml
       Coffee: 76g
       Money: $2.5
       ```

4. **Check Resources Sufficient?**

   - On drink selection, check resource availability.
     - e.g., if Latte requires 200ml water but only 100ml is left, print: “Sorry there is not enough water.”
     - The same should happen if another resource is depleted, e.g., milk or coffee.

5. **Process Coins:**

   - If resources are sufficient, prompt the user to insert coins.
     - Note: quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
     - Calculate the monetary value of the coins inserted.
       - e.g., 1 quarter, 2 dimes, 1 nickel, 2 pennies = $0.52

6. **Check Transaction Successful?**

   - Ensure the user has inserted enough money for the selected drink.
     - e.g., Latte cost $2.50, but they only inserted $0.52, then print: “Sorry that's not enough money. Money refunded.”
     - If enough money is inserted, add the drink cost to the machine profit, reflected in the next “report”.
     - If excess money is inserted, offer change rounded to 2 decimal places.
       - e.g., “Here is $2.45 dollars in change.”

7. **Make Coffee:**
   - On successful transaction and sufficient resources, deduct the ingredients from the coffee machine resources.
     - e.g.,
       - Report before purchasing latte:
         ```
         Water: 300ml
         Milk: 200ml
         Coffee: 100g
         Money: $0
         ```
       - Report after purchasing latte:
         ```
         Water: 100ml
         Milk: 50ml
         Coffee: 76g
         Money: $2.5
         ```
     - Once resources are deducted, inform the user: “Here is your latte. Enjoy!” (if latte was their choice).
