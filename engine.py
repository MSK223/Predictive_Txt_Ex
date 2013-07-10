from model import parse_file

'''
Generate a sorted list of predictions.  
 
'''

def predict(so_far, num_predictions=10):

    prediction_list = [] #List to capture pred words & frequencies.
    pred_word_list = [] #Just prediciton words.
    counter = 0

    #Create model trie.
    word_trie = parse_file("data.txt")

    result = sorted(word_trie.search(so_far, prediction_list), key=lambda tup: int(tup[1]), reverse = True)

    #Strips out frequences from prediction list.
    for word in result:
        if counter < num_predictions:
            pred_word_list.append(word[0])
            counter += 1
        else:
            break

    return pred_word_list
