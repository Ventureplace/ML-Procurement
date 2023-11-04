from requests_html import HTMLSession
from database_manager import connect_to_db, insert_product
from machine_components import get_components

def get_user_input():
    """
    Get the desired machine name from the user.
    """
    machine_name = input("Enter the name of the desired machine: ")
    return machine_name.strip()  # Remove any leading or trailing whitespace.

def scrape_alibaba_for_component(component):
    """
    Scrapes Alibaba for the given component and returns a list of product details.
    """
    session = HTMLSession()
    base_url = "https://www.alibaba.com"
    search_url = f"{base_url}/wholesale?SearchText={component}"

    response = session.get(search_url)
    
    products = response.html.find('.m-gallery-product-item-v2')
    product_details = []

    for product in products:
        name = product.find('.elements-title-normal__content', first=True).text
        price_range = product.find('.elements-offer-price-normal__price', first=True).text
        product_details.append({'name': name, 'price_range': price_range})

    return product_details

def store_data_in_db(machine, component, product_details):
    """
    Stores the scraped product details in the database.
    """
    conn = connect_to_db()

    for product in product_details:
        insert_product(conn, machine, component, product['name'], product['price_range'])

    conn.close()

if __name__ == "__main__":
    machine = get_user_input()
    components = get_components(machine)

    if not components:
        print(f"No components found for {machine}. Please ensure it's in our database or check the spelling.")
    else:
        print(f"Key components for {machine}: {', '.join(components)}")

        for component in components:
            print(f"Scraping data for {component} from Alibaba...")
            product_details = scrape_alibaba_for_component(component)
            
            if product_details:
                store_data_in_db(machine, component, product_details)
                print(f"Stored data for {component} in the database.")
            else:
                print(f"No products found for {component} on Alibaba.")
