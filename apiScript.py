
import requests
import argparse
import json


def read_arguments():
    """
    [summary]
    
    reading arguments from console
    """
    parser = argparse.ArgumentParser(description='Custom Search Engine API')
    parser.add_argument('query', type=str, help='Search Query')
    args = parser.parse_args()
    return args


def get_config(config_file):
    """[summary]

    Args:
        config_file ([string]): [configuration file name]

    Returns:
        [string, string]: [the api key and the engine id]
    """
    file = open(config_file) 
    config = json.load(file)
    
    return config.get('apiKey'), config.get('engineId')
    
def get_query(args):
    """[summary]
    extracting the search query from the arguments
    Args:
        args ([list]): [arguments list]

    Returns:
        [string]: [search query]
    """
    query = args.query
    return query

def search_api(api_key, engine_id, query):
    """[summary]

    Args:
        api_key ([string]): [secret key for api]
        engine_id ([string]): [search engine id]
        query ([string]): [search query]

    Returns:
        [list]: [search results]
    """
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={engine_id}&q={query}"
    results = requests.get(url).json()
    search_results = results.get('items')
    
    return search_results

def write_data_to_file(file_name,search_results): 
    """[summary]
    creating a file and proccesing the results then writing them to the file 
    
    Args:
        file_name ([string]): [the file to store the results]
        searchResults ([list]): [list of search results]
    """
         
    with open('results.text','w', newline='') as file:
        for result in search_results:
            file.write('\n' + 'Title: ' + result.get('title')+'\n')
            file.write('Description: ' + result.get('snippet')+'\n')
            file.write('URL: ' + result.get('link') + '\n')
            file.write('\n' +'---------------------------------------------------------' + '\n')
            
def main():
    
    #reading arguments from console
    arguments = read_arguments()
    #getting api key and search engine id values
    api_key, engine_id = get_config('config.json')
    # get search query from arguments
    query = get_query(arguments);
    # pass api details to get search results
    results = search_api(api_key, engine_id, query)
    # write results to a file
    write_data_to_file('results.txt', results)
    
if __name__ == "__main__":
    
    main()

    
    
    


