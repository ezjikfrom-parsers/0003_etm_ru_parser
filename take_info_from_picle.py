import pickle;

with open('products_links_list.pickle', 'rb') as f:
     all_list_of_products = pickle.load(f);     
     
     
print(len(all_list_of_products));
