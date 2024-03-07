import requests

def getRelevantFoodOutlets(city, maxCost):
    url_template = 'https://jsonmock.hackerrank.com/api/food_outlets?city={}&page={}'
    page = 1
    relevant_outlets = []
    
    try:
        while True:
            response = requests.get(url_template.format(city, page)).json()
            print(f"Response for page {page}: {response}")  # Debug: print the response
            outlets = response.get('data', [])
            print(f'outlets: {outlets}')
            # Filter outlets by maxCost
            relevant_outlets.extend([outlet['name'] for outlet in outlets if outlet['estimated_cost'] <= maxCost])
            
            # Check if there are more pages
            if page >= response['total_pages']:
                break
            page += 1
        
        return relevant_outlets

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []

if __name__ == '__main__':
    city = "Denver"
    maxCost = 50
    result = getRelevantFoodOutlets(city, maxCost)

    print(f'For {city} and {maxCost}: {result}')

    city = "Houston"
    maxCost = 30
    result = getRelevantFoodOutlets(city, maxCost)

    print(f'For {city} and {maxCost}: {result}')

    
    # if result:
    #     print('\n'.join(result))
    # else:
    #     print("No food outlets found or there was an error in the API request.")