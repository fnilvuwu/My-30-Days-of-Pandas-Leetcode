import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame(columns=['customer_number'])
    
    order_counts = orders.customer_number.value_counts()
    
    max_orders = order_counts.max()
    
    customers_with_max_orders = order_counts[order_counts == max_orders].index.tolist()
    
    result = pd.DataFrame({'customer_number': customers_with_max_orders})
    
    return result